-- Solo procedimientos almacenados de bd_libros.
-- NO borra ni modifica tablas ni datos: se puede ejecutar sobre la base existente.

USE bd_libros;

DELIMITER $$

-- ---------- Autenticación ----------
DROP PROCEDURE IF EXISTS sp_obtener_usuario_por_username$$
CREATE PROCEDURE sp_obtener_usuario_por_username(
    IN p_username VARCHAR(100)
)
BEGIN
    SELECT
        u.id_usuario,
        u.numero_documento,
        u.nombres,
        u.apellidos,
        u.username,
        u.password_hash,
        CONCAT(u.nombres, ' ', u.apellidos) AS nombre_completo,
        u.rol_id,
        r.nombre_rol AS rol,
        u.es_activo
    FROM usuarios u
    INNER JOIN roles r ON u.rol_id = r.id_rol
    WHERE u.username = p_username
      AND u.es_activo = 1
    LIMIT 1;
END$$

-- ---------- Roles ----------
-- Usado por el combo del formulario de empleados
DROP PROCEDURE IF EXISTS sp_roles_listar$$
CREATE PROCEDURE sp_roles_listar()
BEGIN
    SELECT id_rol, nombre_rol, descripcion
    FROM roles
    ORDER BY nombre_rol;
END$$

-- Catálogo de roles con buscador y número de usuarios asignados
DROP PROCEDURE IF EXISTS sp_roles_buscar$$
CREATE PROCEDURE sp_roles_buscar(
    IN p_criterio VARCHAR(100)
)
BEGIN
    DECLARE v_termino VARCHAR(102);
    SET v_termino = CONCAT('%', IFNULL(TRIM(p_criterio), ''), '%');

    SELECT
        r.id_rol,
        r.nombre_rol,
        r.descripcion,
        COUNT(u.id_usuario) AS total_usuarios
    FROM roles r
    LEFT JOIN usuarios u ON u.rol_id = r.id_rol
    WHERE r.nombre_rol LIKE v_termino
       OR IFNULL(r.descripcion, '') LIKE v_termino
    GROUP BY r.id_rol, r.nombre_rol, r.descripcion
    ORDER BY r.id_rol;
END$$

DROP PROCEDURE IF EXISTS sp_rol_obtener_por_id$$
CREATE PROCEDURE sp_rol_obtener_por_id(
    IN p_id_rol INT
)
BEGIN
    SELECT id_rol, nombre_rol, descripcion
    FROM roles
    WHERE id_rol = p_id_rol;
END$$

DROP PROCEDURE IF EXISTS sp_rol_registrar$$
CREATE PROCEDURE sp_rol_registrar(
    IN  p_nombre_rol  VARCHAR(50),
    IN  p_descripcion VARCHAR(150),
    OUT p_id_generado INT
)
BEGIN
    IF EXISTS (SELECT 1 FROM roles WHERE nombre_rol = TRIM(p_nombre_rol)) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Ya existe un rol registrado con ese nombre.';
    END IF;

    INSERT INTO roles (nombre_rol, descripcion)
    VALUES (TRIM(p_nombre_rol), NULLIF(TRIM(p_descripcion), ''));

    SET p_id_generado = LAST_INSERT_ID();
END$$

DROP PROCEDURE IF EXISTS sp_rol_actualizar$$
CREATE PROCEDURE sp_rol_actualizar(
    IN p_id_rol      INT,
    IN p_nombre_rol  VARCHAR(50),
    IN p_descripcion VARCHAR(150)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM roles WHERE id_rol = p_id_rol) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El rol que intenta actualizar no existe.';
    END IF;

    IF EXISTS (SELECT 1 FROM roles
               WHERE nombre_rol = TRIM(p_nombre_rol)
                 AND id_rol <> p_id_rol) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Ya existe otro rol registrado con ese nombre.';
    END IF;

    UPDATE roles SET
        nombre_rol  = TRIM(p_nombre_rol),
        descripcion = NULLIF(TRIM(p_descripcion), '')
    WHERE id_rol = p_id_rol;
END$$

DROP PROCEDURE IF EXISTS sp_rol_eliminar$$
CREATE PROCEDURE sp_rol_eliminar(
    IN p_id_rol INT
)
BEGIN
    DECLARE v_total INT DEFAULT 0;

    IF NOT EXISTS (SELECT 1 FROM roles WHERE id_rol = p_id_rol) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El rol que intenta eliminar no existe.';
    END IF;

    -- No se puede borrar un rol que todavía tienen usuarios
    SELECT COUNT(*) INTO v_total FROM usuarios WHERE rol_id = p_id_rol;
    IF v_total > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: hay usuarios asignados a este rol. Reasígnelos primero.';
    END IF;

    DELETE FROM roles WHERE id_rol = p_id_rol;
END$$

-- ---------- Programas de estudio ----------
DROP PROCEDURE IF EXISTS sp_programas_listar$$
CREATE PROCEDURE sp_programas_listar()
BEGIN
    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    ORDER BY id_programa DESC;
END$$

DROP PROCEDURE IF EXISTS sp_programas_buscar$$
CREATE PROCEDURE sp_programas_buscar(
    IN p_criterio VARCHAR(100)
)
BEGIN
    DECLARE v_termino VARCHAR(102);
    SET v_termino = CONCAT('%', IFNULL(TRIM(p_criterio), ''), '%');

    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    WHERE codigo_programa LIKE v_termino
       OR nombre_programa LIKE v_termino
    ORDER BY id_programa DESC;
END$$

-- ---------- Empleados ----------
DROP PROCEDURE IF EXISTS sp_empleados_listar$$
CREATE PROCEDURE sp_empleados_listar(
    IN p_criterio VARCHAR(100)
)
BEGIN
    DECLARE v_criterio VARCHAR(100);
    SET v_criterio = IFNULL(TRIM(p_criterio), '');

    SELECT
        u.id_usuario,
        u.numero_documento,
        u.nombres,
        u.apellidos,
        u.username,
        CONCAT(u.apellidos, ', ', u.nombres) AS nombre_completo,
        e.codigo_empleado,
        e.cargo,
        e.turno,
        r.nombre_rol,
        r.nombre_rol AS rol,
        IF(u.es_activo = 1, 'Activo', 'Inactivo') AS estado
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    INNER JOIN roles r     ON u.rol_id = r.id_rol
    WHERE v_criterio = ''
       OR u.numero_documento LIKE CONCAT('%', v_criterio, '%')
       OR u.nombres          LIKE CONCAT('%', v_criterio, '%')
       OR u.apellidos        LIKE CONCAT('%', v_criterio, '%')
       OR u.username         LIKE CONCAT('%', v_criterio, '%')
       OR e.codigo_empleado  LIKE CONCAT('%', v_criterio, '%')
    ORDER BY u.id_usuario DESC
    LIMIT 20;
END$$

DROP PROCEDURE IF EXISTS sp_empleado_obtener_por_id$$
CREATE PROCEDURE sp_empleado_obtener_por_id(
    IN p_id_usuario INT
)
BEGIN
    SELECT
        u.id_usuario,
        u.numero_documento,
        u.nombres,
        u.apellidos,
        u.username,
        u.rol_id,
        e.codigo_empleado,
        e.cargo,
        e.turno
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    WHERE u.id_usuario = p_id_usuario;
END$$

DROP PROCEDURE IF EXISTS sp_empleado_registrar$$
CREATE PROCEDURE sp_empleado_registrar(
    IN  p_numero_documento VARCHAR(15),
    IN  p_nombres          VARCHAR(80),
    IN  p_apellidos        VARCHAR(80),
    IN  p_username         VARCHAR(100),
    IN  p_password_hash    VARCHAR(255),
    IN  p_rol_id           INT,
    IN  p_codigo_empleado  VARCHAR(20),
    IN  p_cargo            VARCHAR(80),
    IN  p_turno            VARCHAR(30),
    OUT p_id_generado      INT
)
BEGIN
    -- Si algo falla, se deshace todo y el error llega a Python
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    IF EXISTS (SELECT 1 FROM usuarios WHERE numero_documento = p_numero_documento) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El documento ingresado ya pertenece a un usuario registrado.';
    END IF;

    IF EXISTS (SELECT 1 FROM usuarios WHERE username = p_username) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El correo o nombre de usuario ya está asignado a otra cuenta.';
    END IF;

    IF EXISTS (SELECT 1 FROM empleados WHERE codigo_empleado = p_codigo_empleado) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El código corporativo de empleado ya pertenece a otro trabajador.';
    END IF;

    INSERT INTO usuarios (numero_documento, nombres, apellidos, username, password_hash, rol_id, es_activo)
    VALUES (p_numero_documento, p_nombres, p_apellidos, p_username, p_password_hash, p_rol_id, 1);

    SET p_id_generado = LAST_INSERT_ID();

    INSERT INTO empleados (usuario_id, codigo_empleado, cargo, turno)
    VALUES (p_id_generado, p_codigo_empleado, p_cargo, p_turno);

    COMMIT;
END$$

DROP PROCEDURE IF EXISTS sp_empleado_actualizar$$
CREATE PROCEDURE sp_empleado_actualizar(
    IN p_id_usuario       INT,
    IN p_numero_documento VARCHAR(15),
    IN p_nombres          VARCHAR(80),
    IN p_apellidos        VARCHAR(80),
    IN p_username         VARCHAR(100),
    IN p_password_hash    VARCHAR(255),   -- '' o NULL = conservar la contraseña actual
    IN p_rol_id           INT,
    IN p_codigo_empleado  VARCHAR(20),
    IN p_cargo            VARCHAR(80),
    IN p_turno            VARCHAR(30)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM empleados WHERE usuario_id = p_id_usuario) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El empleado que intenta actualizar no existe.';
    END IF;

    IF EXISTS (SELECT 1 FROM usuarios
               WHERE numero_documento = p_numero_documento
                 AND id_usuario <> p_id_usuario) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El documento ingresado pertenece a otro usuario registrado.';
    END IF;

    IF EXISTS (SELECT 1 FROM usuarios
               WHERE username = p_username
                 AND id_usuario <> p_id_usuario) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El correo o nombre de usuario ya está asignado a otra cuenta.';
    END IF;

    IF EXISTS (SELECT 1 FROM empleados
               WHERE codigo_empleado = p_codigo_empleado
                 AND usuario_id <> p_id_usuario) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El código corporativo de empleado ya pertenece a otro trabajador.';
    END IF;

    -- Tabla padre: usuarios (la contraseña solo cambia si llega un hash nuevo)
    UPDATE usuarios SET
        numero_documento = p_numero_documento,
        nombres          = p_nombres,
        apellidos        = p_apellidos,
        username         = p_username,
        password_hash    = IF(IFNULL(p_password_hash, '') = '', password_hash, p_password_hash),
        rol_id           = p_rol_id
    WHERE id_usuario = p_id_usuario;

    -- Tabla hija: empleados
    UPDATE empleados SET
        codigo_empleado = p_codigo_empleado,
        cargo           = p_cargo,
        turno           = p_turno
    WHERE usuario_id = p_id_usuario;

    COMMIT;
END$$

-- ---------- Empleados: Eliminación (S23 - Acción 5) ----------
-- 1. BORRADO LÓGICO (Estándar Corporativo: desactiva el acceso conservando historial)
DROP PROCEDURE IF EXISTS sp_empleado_eliminar_logico $$
CREATE PROCEDURE sp_empleado_eliminar_logico(IN p_id_usuario INT)
BEGIN
    UPDATE usuarios 
    SET es_activo = 0 
    WHERE id_usuario = p_id_usuario;
END $$

-- 2. BORRADO FÍSICO (Destruye el registro; activa ON DELETE CASCADE hacia empleados,
-- pero falla con error 1451 si existen llaves foráneas en tablas de movimiento)
DROP PROCEDURE IF EXISTS sp_empleado_eliminar_fisico $$
CREATE PROCEDURE sp_empleado_eliminar_fisico(IN p_id_usuario INT)
sp_bloque: BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;
    DELETE FROM usuarios WHERE id_usuario = p_id_usuario;
    COMMIT;
END sp_bloque $$

DELIMITER ;
