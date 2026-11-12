-- =====================================================================
--  RIOJA-BIBLIOTECA  -  Base de datos bd_libros (creación desde cero)
-- ---------------------------------------------------------------------
--  Ejecutar COMPLETO en MySQL 8 (Workbench: rayo ⚡ / Ctrl+Shift+Enter).
--  ATENCIÓN: borra la base bd_libros si ya existe y la vuelve a crear.
--
--  ¿Ya tienes datos y solo quieres actualizar los procedimientos almacenados?
--  Ejecuta en su lugar database/solo_procedimientos.sql (mismos 13
--  procedimientos de la sección 3, sin tocar tablas ni datos).
--
--  Usuarios de prueba (contraseña de todos: 123456)
--    admin@sistema.com            -> Administrador
--    ana.torres@sistema.com       -> Bibliotecario
--    carlos.mendoza@sistema.com   -> Estudiante
-- =====================================================================

DROP DATABASE IF EXISTS bd_libros;
CREATE DATABASE bd_libros CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bd_libros;

-- =====================================================================
--  1. TABLAS (en orden de dependencias: primero las padre)
-- =====================================================================

CREATE TABLE roles (
    id_rol       INT          NOT NULL AUTO_INCREMENT,
    nombre_rol   VARCHAR(50)  NOT NULL,
    descripcion  VARCHAR(150) NULL,
    PRIMARY KEY (id_rol),
    UNIQUE KEY uk_roles_nombre (nombre_rol)
) ENGINE=InnoDB;

CREATE TABLE programas_estudio (
    id_programa      INT          NOT NULL AUTO_INCREMENT,
    codigo_programa  VARCHAR(10)  NOT NULL,
    nombre_programa  VARCHAR(120) NOT NULL,
    estado           ENUM('Activo','Inactivo') NOT NULL DEFAULT 'Activo',
    creado_en        TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_programa),
    UNIQUE KEY uk_programas_codigo (codigo_programa),
    UNIQUE KEY uk_programas_nombre (nombre_programa)
) ENGINE=InnoDB;

CREATE TABLE usuarios (
    id_usuario        INT          NOT NULL AUTO_INCREMENT,
    numero_documento  VARCHAR(15)  NOT NULL,
    nombres           VARCHAR(80)  NOT NULL,
    apellidos         VARCHAR(80)  NOT NULL,
    username          VARCHAR(100) NOT NULL,
    password_hash     VARCHAR(255) NOT NULL,
    rol_id            INT          NOT NULL,
    es_activo         TINYINT(1)   NOT NULL DEFAULT 1,
    creado_en         TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario),
    UNIQUE KEY uk_usuarios_documento (numero_documento),
    UNIQUE KEY uk_usuarios_username (username),
    CONSTRAINT fk_usuarios_rol FOREIGN KEY (rol_id)
        REFERENCES roles (id_rol) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE empleados (
    usuario_id       INT         NOT NULL,
    codigo_empleado  VARCHAR(20) NOT NULL,
    cargo            VARCHAR(80) NOT NULL,
    turno            VARCHAR(30) NOT NULL DEFAULT 'Mañana',
    PRIMARY KEY (usuario_id),
    UNIQUE KEY uk_empleados_codigo (codigo_empleado),
    CONSTRAINT fk_empleados_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE estudiantes (
    usuario_id     INT         NOT NULL,
    carnet         VARCHAR(20) NOT NULL,
    programa_id    INT         NOT NULL,
    semestre       VARCHAR(10) NOT NULL DEFAULT 'I',
    tiene_sancion  TINYINT(1)  NOT NULL DEFAULT 0,
    PRIMARY KEY (usuario_id),
    UNIQUE KEY uk_estudiantes_carnet (carnet),
    CONSTRAINT fk_estudiantes_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_estudiantes_programa FOREIGN KEY (programa_id)
        REFERENCES programas_estudio (id_programa) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE autores (
    id_autor      INT          NOT NULL AUTO_INCREMENT,
    nombre        VARCHAR(100) NOT NULL,
    nacionalidad  VARCHAR(100) NOT NULL DEFAULT 'Desconocida',
    PRIMARY KEY (id_autor),
    UNIQUE KEY uk_autores_nombre (nombre)
) ENGINE=InnoDB;

CREATE TABLE editoriales (
    id_editorial  INT          NOT NULL AUTO_INCREMENT,
    nombre        VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_editorial),
    UNIQUE KEY uk_editoriales_nombre (nombre)
) ENGINE=InnoDB;

CREATE TABLE libros (
    id_libro           INT          NOT NULL AUTO_INCREMENT,
    isbn               VARCHAR(20)  NOT NULL,
    titulo             VARCHAR(150) NOT NULL,
    subtitulo          VARCHAR(150) NULL,
    editorial_id       INT          NOT NULL,
    programa_id        INT          NOT NULL,
    anio_publicacion   INT          NOT NULL,
    lugar_publicacion  VARCHAR(100) NULL,
    numero_paginas     INT          NOT NULL,
    ubicacion_estante  VARCHAR(50)  NOT NULL,
    PRIMARY KEY (id_libro),
    UNIQUE KEY uk_libros_isbn (isbn),
    CONSTRAINT fk_libros_editorial FOREIGN KEY (editorial_id)
        REFERENCES editoriales (id_editorial) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_libros_programa FOREIGN KEY (programa_id)
        REFERENCES programas_estudio (id_programa) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE libro_autor (
    id_libro_autor  INT         NOT NULL AUTO_INCREMENT,
    libro_id        INT         NOT NULL,
    autor_id        INT         NOT NULL,
    orden_autor     INT         NOT NULL DEFAULT 1,
    rol_autor       VARCHAR(50) NOT NULL DEFAULT 'Autor Principal',
    PRIMARY KEY (id_libro_autor),
    UNIQUE KEY uk_libro_autor (libro_id, autor_id),
    CONSTRAINT fk_la_libro FOREIGN KEY (libro_id)
        REFERENCES libros (id_libro) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_la_autor FOREIGN KEY (autor_id)
        REFERENCES autores (id_autor) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE ejemplares (
    id_ejemplar          INT         NOT NULL AUTO_INCREMENT,
    libro_id             INT         NOT NULL,
    codigo_patrimonial   VARCHAR(50) NOT NULL,
    estado_conservacion  VARCHAR(30) NOT NULL DEFAULT 'Bueno',
    esta_disponible      TINYINT(1)  NOT NULL DEFAULT 1,
    PRIMARY KEY (id_ejemplar),
    UNIQUE KEY uk_ejemplares_codigo (codigo_patrimonial),
    CONSTRAINT fk_ejemplar_libro FOREIGN KEY (libro_id)
        REFERENCES libros (id_libro) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE equipos (
    id_equipo           INT          NOT NULL AUTO_INCREMENT,
    codigo_patrimonial  VARCHAR(50)  NOT NULL,
    nombre_pc           VARCHAR(50)  NOT NULL,
    tipo_equipo         ENUM('BUSQUEDA','TRABAJO') NOT NULL DEFAULT 'TRABAJO',
    estado              ENUM('LIBRE','OCUPADO','BLOQUEADO','MANTENIMIENTO') NOT NULL DEFAULT 'LIBRE',
    ip_address          VARCHAR(45)  NULL,
    observaciones       VARCHAR(200) NULL,
    PRIMARY KEY (id_equipo),
    UNIQUE KEY uk_equipos_codigo (codigo_patrimonial),
    UNIQUE KEY uk_equipos_nombre_pc (nombre_pc)
) ENGINE=InnoDB;

CREATE TABLE prestamos (
    id_prestamo         INT          NOT NULL AUTO_INCREMENT,
    usuario_id          INT          NOT NULL,
    empleado_id         INT          NOT NULL,
    tipo_prestamo       ENUM('SALA','DOMICILIO') NOT NULL DEFAULT 'SALA',
    fecha_prestamo      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_dev_esperada  DATETIME     NOT NULL,
    fecha_dev_real      DATETIME     NULL,
    estado              ENUM('ACTIVO','DEVUELTO','VENCIDO') NOT NULL DEFAULT 'ACTIVO',
    observaciones       VARCHAR(250) NULL,
    PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_prestamos_usuario FOREIGN KEY (usuario_id)
        REFERENCES usuarios (id_usuario) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_prestamos_empleado FOREIGN KEY (empleado_id)
        REFERENCES usuarios (id_usuario) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE prestamo_detalles (
    id_detalle      INT NOT NULL AUTO_INCREMENT,
    prestamo_id     INT NOT NULL,
    tipo_recurso    ENUM('LIBRO','COMPUTADORA') NOT NULL,
    ejemplar_id     INT NULL,
    equipo_id       INT NULL,
    estado_recurso  ENUM('PRESTADO','DEVUELTO','CON_OBSERVACION') NOT NULL DEFAULT 'PRESTADO',
    PRIMARY KEY (id_detalle),
    CONSTRAINT fk_detalle_prestamo FOREIGN KEY (prestamo_id)
        REFERENCES prestamos (id_prestamo) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_detalle_ejemplar FOREIGN KEY (ejemplar_id)
        REFERENCES ejemplares (id_ejemplar) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_detalle_equipo FOREIGN KEY (equipo_id)
        REFERENCES equipos (id_equipo) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =====================================================================
--  2. DATOS INICIALES
-- =====================================================================

INSERT INTO roles (id_rol, nombre_rol, descripcion) VALUES
    (1, 'Administrador', 'Acceso total y configuración del sistema'),
    (2, 'Bibliotecario', 'Atención de préstamos y control de sala'),
    (3, 'Estudiante',    'Usuario lector estudiante');

INSERT INTO programas_estudio (id_programa, codigo_programa, nombre_programa, estado) VALUES
    (1, 'DSI', 'Desarrollo de Sistemas de Información', 'Activo'),
    (2, 'RSI', 'Redes y Seguridad Informática',         'Activo'),
    (3, 'DDS', 'Diseño y Desarrollo de Software',       'Activo');

-- Hash BCrypt (12 rondas) de la contraseña: 123456
INSERT INTO usuarios (id_usuario, numero_documento, nombres, apellidos, username, password_hash, rol_id, es_activo) VALUES
    (1, '11223344', 'Luis',   'Silva Ruiz',    'admin@sistema.com',          '$2b$12$CdCB0CnACg0zLwjqqPlEN.bgNLs5ZCSljyO/wu1IvLhpkbSSmJaQa', 1, 1),
    (2, '09876543', 'Ana',    'Torres López',  'ana.torres@sistema.com',     '$2b$12$CdCB0CnACg0zLwjqqPlEN.bgNLs5ZCSljyO/wu1IvLhpkbSSmJaQa', 2, 1),
    (3, '73528190', 'Carlos', 'Mendoza Pérez', 'carlos.mendoza@sistema.com', '$2b$12$CdCB0CnACg0zLwjqqPlEN.bgNLs5ZCSljyO/wu1IvLhpkbSSmJaQa', 3, 1);

INSERT INTO empleados (usuario_id, codigo_empleado, cargo, turno) VALUES
    (1, 'EMP-001', 'Administrador General',   'Completo'),
    (2, 'EMP-100', 'Bibliotecaria Encargada', 'Mañana');

INSERT INTO estudiantes (usuario_id, carnet, programa_id, semestre, tiene_sancion) VALUES
    (3, 'EST-2026-01', 1, 'V', 0);

-- =====================================================================
--  3. PROCEDIMIENTOS ALMACENADOS
--     (sin DEFINER, para que funcionen con cualquier usuario de MySQL)
-- =====================================================================

DELIMITER $$

-- ---------- Autenticación ----------
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
CREATE PROCEDURE sp_roles_listar()
BEGIN
    SELECT id_rol, nombre_rol, descripcion
    FROM roles
    ORDER BY nombre_rol;
END$$

-- Catálogo de roles con buscador y número de usuarios asignados
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

CREATE PROCEDURE sp_rol_obtener_por_id(
    IN p_id_rol INT
)
BEGIN
    SELECT id_rol, nombre_rol, descripcion
    FROM roles
    WHERE id_rol = p_id_rol;
END$$

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
CREATE PROCEDURE sp_programas_listar()
BEGIN
    SELECT id_programa, codigo_programa, nombre_programa, estado, creado_en
    FROM programas_estudio
    ORDER BY id_programa DESC;
END$$

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

-- ==============================================================================
-- 2. ACTUALIZACIÓN TRANSACCIONAL ATÓMICA DE EMPLEADOS (S22)
-- Modifica concurrentemente las tablas usuarios y empleados bajo control ACID
-- ==============================================================================
DROP PROCEDURE IF EXISTS sp_empleado_actualizar $$
CREATE PROCEDURE sp_empleado_actualizar(
    IN p_id_usuario       INT,
    IN p_numero_documento VARCHAR(15),
    IN p_nombres          VARCHAR(80),
    IN p_apellidos        VARCHAR(80),
    IN p_username         VARCHAR(100),
    IN p_password_hash    VARCHAR(255), -- Cadena vacía si se conserva la clave
    IN p_rol_id           INT,
    IN p_codigo_empleado  VARCHAR(20),
    IN p_cargo            VARCHAR(80),
    IN p_turno            VARCHAR(30)
)
sp_bloque: BEGIN
    -- Manejador de fallas: revierte cambios y propaga la excepción hacia Python
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    -- Validación defensiva: Evitar colisión de DNI con registros de otros usuarios
    IF EXISTS (
        SELECT 1 FROM usuarios 
        WHERE numero_documento = p_numero_documento 
          AND id_usuario != p_id_usuario
    ) THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'El documento ingresado pertenece a otro usuario registrado.';
    END IF;

    -- Validación defensiva: Evitar colisión de Username/Correo con otras cuentas
    IF EXISTS (
        SELECT 1 FROM usuarios 
        WHERE username = p_username 
          AND id_usuario != p_id_usuario
    ) THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'El correo o nombre de usuario ya está asignado a otra cuenta.';
    END IF;

    -- Validación defensiva: Evitar duplicidad de Código de Empleado
    IF EXISTS (
        SELECT 1 FROM empleados 
        WHERE codigo_empleado = p_codigo_empleado 
          AND usuario_id != p_id_usuario
    ) THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'El código corporativo de empleado ya pertenece a otro trabajador.';
    END IF;

    -- Paso A: Actualización condicional en la entidad Padre (usuarios)
    IF p_password_hash = '' THEN
        -- Se conservan las credenciales criptográficas previas
        UPDATE usuarios SET 
            numero_documento = p_numero_documento,
            nombres          = p_nombres,
            apellidos        = p_apellidos,
            username         = p_username,
            rol_id           = p_rol_id
        WHERE id_usuario = p_id_usuario;
    ELSE
        -- Se actualiza el hash criptográfico suministrado por el controlador
        UPDATE usuarios SET 
            numero_documento = p_numero_documento,
            nombres          = p_nombres,
            apellidos        = p_apellidos,
            username         = p_username,
            password_hash    = p_password_hash,
            rol_id           = p_rol_id
        WHERE id_usuario = p_id_usuario;
    END IF;

    -- Paso B: Actualización en la entidad Hija (empleados)
    UPDATE empleados SET 
        codigo_empleado = p_codigo_empleado,
        cargo           = p_cargo,
        turno           = p_turno
    WHERE usuario_id = p_id_usuario;

    -- Paso C: Consolidación física de la transacción
    COMMIT;
END sp_bloque $$

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

-- Comprobación rápida
SELECT 'bd_libros creada correctamente' AS resultado;
