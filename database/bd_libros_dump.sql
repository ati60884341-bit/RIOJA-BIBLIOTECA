-- Dump generado automaticamente de bd_libros (estructura + datos + stored procedures)
-- Ejecutar completo en un MySQL nuevo para recrear la base de datos del proyecto RIOJA-BIBLIOTECA.

CREATE DATABASE IF NOT EXISTS bd_libros CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bd_libros;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `autores`;
CREATE TABLE `autores` (
  `id_autor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nacionalidad` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Desconocida',
  PRIMARY KEY (`id_autor`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `editoriales`;
CREATE TABLE `editoriales` (
  `id_editorial` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_editorial`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `ejemplares`;
CREATE TABLE `ejemplares` (
  `id_ejemplar` int NOT NULL AUTO_INCREMENT,
  `libro_id` int NOT NULL,
  `codigo_patrimonial` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado_conservacion` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Bueno',
  `esta_disponible` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_ejemplar`),
  UNIQUE KEY `codigo_patrimonial` (`codigo_patrimonial`),
  KEY `fk_ejemplar_libro` (`libro_id`),
  CONSTRAINT `fk_ejemplar_libro` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`id_libro`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `empleados`;
CREATE TABLE `empleados` (
  `usuario_id` int NOT NULL,
  `codigo_empleado` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cargo` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `turno` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Mañana',
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `codigo_empleado` (`codigo_empleado`),
  CONSTRAINT `fk_empleados_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `equipos`;
CREATE TABLE `equipos` (
  `id_equipo` int NOT NULL AUTO_INCREMENT,
  `codigo_patrimonial` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nombre_pc` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo_equipo` enum('BUSQUEDA','TRABAJO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'TRABAJO',
  `estado` enum('LIBRE','OCUPADO','BLOQUEADO','MANTENIMIENTO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'LIBRE',
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `observaciones` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_equipo`),
  UNIQUE KEY `codigo_patrimonial` (`codigo_patrimonial`),
  UNIQUE KEY `nombre_pc` (`nombre_pc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `estudiantes`;
CREATE TABLE `estudiantes` (
  `usuario_id` int NOT NULL,
  `carnet` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `programa_id` int NOT NULL,
  `semestre` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'I',
  `tiene_sancion` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `carnet` (`carnet`),
  KEY `fk_estudiantes_programa` (`programa_id`),
  CONSTRAINT `fk_estudiantes_programa` FOREIGN KEY (`programa_id`) REFERENCES `programas_estudio` (`id_programa`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_estudiantes_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `libro_autor`;
CREATE TABLE `libro_autor` (
  `id_libro_autor` int NOT NULL AUTO_INCREMENT,
  `libro_id` int NOT NULL,
  `autor_id` int NOT NULL,
  `orden_autor` int NOT NULL DEFAULT '1',
  `rol_autor` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Autor Principal',
  PRIMARY KEY (`id_libro_autor`),
  UNIQUE KEY `uk_libro_autor` (`libro_id`,`autor_id`),
  KEY `fk_la_autor` (`autor_id`),
  CONSTRAINT `fk_la_autor` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id_autor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_la_libro` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`id_libro`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `libros`;
CREATE TABLE `libros` (
  `id_libro` int NOT NULL AUTO_INCREMENT,
  `isbn` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `titulo` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subtitulo` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `editorial_id` int NOT NULL,
  `programa_id` int NOT NULL,
  `anio_publicacion` int NOT NULL,
  `lugar_publicacion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `numero_paginas` int NOT NULL,
  `ubicacion_estante` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_libro`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `fk_libros_editorial` (`editorial_id`),
  KEY `fk_libros_programa` (`programa_id`),
  CONSTRAINT `fk_libros_editorial` FOREIGN KEY (`editorial_id`) REFERENCES `editoriales` (`id_editorial`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_libros_programa` FOREIGN KEY (`programa_id`) REFERENCES `programas_estudio` (`id_programa`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `prestamo_detalles`;
CREATE TABLE `prestamo_detalles` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `prestamo_id` int NOT NULL,
  `tipo_recurso` enum('LIBRO','COMPUTADORA') COLLATE utf8mb4_unicode_ci NOT NULL,
  `ejemplar_id` int DEFAULT NULL,
  `equipo_id` int DEFAULT NULL,
  `estado_recurso` enum('PRESTADO','DEVUELTO','CON_OBSERVACION') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'PRESTADO',
  PRIMARY KEY (`id_detalle`),
  KEY `fk_detalle_prestamo` (`prestamo_id`),
  KEY `fk_detalle_ejemplar` (`ejemplar_id`),
  KEY `fk_detalle_equipo` (`equipo_id`),
  CONSTRAINT `fk_detalle_ejemplar` FOREIGN KEY (`ejemplar_id`) REFERENCES `ejemplares` (`id_ejemplar`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_detalle_equipo` FOREIGN KEY (`equipo_id`) REFERENCES `equipos` (`id_equipo`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_detalle_prestamo` FOREIGN KEY (`prestamo_id`) REFERENCES `prestamos` (`id_prestamo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `prestamos`;
CREATE TABLE `prestamos` (
  `id_prestamo` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `empleado_id` int NOT NULL,
  `tipo_prestamo` enum('SALA','DOMICILIO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'SALA',
  `fecha_prestamo` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_dev_esperada` datetime NOT NULL,
  `fecha_dev_real` datetime DEFAULT NULL,
  `estado` enum('ACTIVO','DEVUELTO','VENCIDO') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'ACTIVO',
  `observaciones` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_prestamo`),
  KEY `fk_prestamos_usuario` (`usuario_id`),
  KEY `fk_prestamos_empleado` (`empleado_id`),
  CONSTRAINT `fk_prestamos_empleado` FOREIGN KEY (`empleado_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_prestamos_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `programas_estudio`;
CREATE TABLE `programas_estudio` (
  `id_programa` int NOT NULL AUTO_INCREMENT,
  `codigo_programa` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nombre_programa` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` enum('Activo','Inactivo') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Activo',
  `creado_en` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_programa`),
  UNIQUE KEY `codigo_programa` (`codigo_programa`),
  UNIQUE KEY `nombre_programa` (`nombre_programa`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_rol`),
  UNIQUE KEY `nombre_rol` (`nombre_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `numero_documento` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nombres` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `apellidos` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rol_id` int NOT NULL,
  `es_activo` tinyint(1) NOT NULL DEFAULT '1',
  `creado_en` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_usuarios_rol` (`rol_id`),
  CONSTRAINT `fk_usuarios_rol` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id_rol`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos de `empleados`
INSERT INTO `empleados` (`usuario_id`, `codigo_empleado`, `cargo`, `turno`) VALUES (1, 'EMP-001', 'Administrador General', 'Completo');
INSERT INTO `empleados` (`usuario_id`, `codigo_empleado`, `cargo`, `turno`) VALUES (2, 'EMP-100', 'Bibliotecaria Encargada', 'Mañana');

-- Datos de `estudiantes`
INSERT INTO `estudiantes` (`usuario_id`, `carnet`, `programa_id`, `semestre`, `tiene_sancion`) VALUES (3, 'EST-2026-01', 1, 'V', 0);

-- Datos de `programas_estudio`
INSERT INTO `programas_estudio` (`id_programa`, `codigo_programa`, `nombre_programa`, `estado`, `creado_en`) VALUES (1, 'DSI', 'Desarrollo de Sistemas de Información', 'Activo', '2026-11-10 12:35:46');
INSERT INTO `programas_estudio` (`id_programa`, `codigo_programa`, `nombre_programa`, `estado`, `creado_en`) VALUES (2, 'RSI', 'Redes y Seguridad Informática', 'Activo', '2026-11-10 12:35:46');
INSERT INTO `programas_estudio` (`id_programa`, `codigo_programa`, `nombre_programa`, `estado`, `creado_en`) VALUES (3, 'DDS', 'Diseño y Desarrollo de Software', 'Activo', '2026-11-10 12:35:46');

-- Datos de `roles`
INSERT INTO `roles` (`id_rol`, `nombre_rol`, `descripcion`) VALUES (1, 'Administrador', 'Acceso total y configuración del sistema');
INSERT INTO `roles` (`id_rol`, `nombre_rol`, `descripcion`) VALUES (2, 'Bibliotecario', 'Atención de préstamos y control de sala');
INSERT INTO `roles` (`id_rol`, `nombre_rol`, `descripcion`) VALUES (3, 'Estudiante', 'Usuario lector estudiante');

-- Datos de `usuarios`
INSERT INTO `usuarios` (`id_usuario`, `numero_documento`, `nombres`, `apellidos`, `username`, `password_hash`, `rol_id`, `es_activo`, `creado_en`) VALUES (1, '11223344', 'Luis', 'Silva Ruiz', 'admin@sistema.com', '$2b$12$RwAFHeHd.d6XJVh7p4My..cB0Mw0LL5Wdf1PyjUb3/oSo3KXM7NTq', 1, 1, '2026-11-10 12:35:46');
INSERT INTO `usuarios` (`id_usuario`, `numero_documento`, `nombres`, `apellidos`, `username`, `password_hash`, `rol_id`, `es_activo`, `creado_en`) VALUES (2, '09876543', 'Ana', 'Torres López', 'ana.torres@sistema.com', '$2b$12$e8UvVpWvI.7rY9xPZq82.OJq9Yv1hXm58.Y9Zp7W2Q0v18.M9x8.', 2, 1, '2026-11-10 12:35:46');
INSERT INTO `usuarios` (`id_usuario`, `numero_documento`, `nombres`, `apellidos`, `username`, `password_hash`, `rol_id`, `es_activo`, `creado_en`) VALUES (3, '73528190', 'Carlos', 'Mendoza Pérez', 'carlos.mendoza@sistema.com', '$2b$12$e8UvVpWvI.7rY9xPZq82.OJq9Yv1hXm58.Y9Zp7W2Q0v18.M9x8.', 3, 1, '2026-11-10 12:35:46');

SET FOREIGN_KEY_CHECKS = 1;

DELIMITER $$

DROP PROCEDURE IF EXISTS `sp_empleados_listar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_empleados_listar`(
    IN p_criterio VARCHAR(100)
)
BEGIN
    SELECT
        u.id_usuario,
        u.numero_documento,
        u.nombres,
        u.apellidos,
        u.username,
        e.codigo_empleado,
        e.cargo,
        e.turno
    FROM usuarios u
    INNER JOIN empleados e ON u.id_usuario = e.usuario_id
    WHERE p_criterio = ''
       OR u.numero_documento LIKE CONCAT('%', p_criterio, '%')
       OR u.nombres          LIKE CONCAT('%', p_criterio, '%')
       OR u.apellidos        LIKE CONCAT('%', p_criterio, '%')
       OR u.username         LIKE CONCAT('%', p_criterio, '%')
       OR e.codigo_empleado  LIKE CONCAT('%', p_criterio, '%')
    ORDER BY u.id_usuario DESC
    LIMIT 20;
END$$

DROP PROCEDURE IF EXISTS `sp_empleado_actualizar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_empleado_actualizar`(
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
END sp_bloque$$

DROP PROCEDURE IF EXISTS `sp_empleado_obtener_por_id`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_empleado_obtener_por_id`(
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

DROP PROCEDURE IF EXISTS `sp_empleado_registrar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_empleado_registrar`(
    IN p_numero_documento VARCHAR(15),
    IN p_nombres          VARCHAR(80),
    IN p_apellidos        VARCHAR(80),
    IN p_username         VARCHAR(100),
    IN p_password_hash    VARCHAR(255),
    IN p_rol_id           INT,
    IN p_codigo_empleado  VARCHAR(20),
    IN p_cargo            VARCHAR(80),
    IN p_turno            VARCHAR(30),
    OUT p_id_generado     INT
)
sp_bloque: BEGIN
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
END sp_bloque$$

DROP PROCEDURE IF EXISTS `sp_obtener_usuario_por_username`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_obtener_usuario_por_username`(
    IN p_username VARCHAR(100)
)
BEGIN
    SELECT 
        u.id_usuario,
        u.username,
        u.password_hash,
        CONCAT(u.nombres, ' ', u.apellidos) AS nombre_completo,
        r.nombre_rol AS rol,
        u.es_activo
    FROM usuarios u
    INNER JOIN roles r ON u.rol_id = r.id_rol
    WHERE u.username = p_username 
      AND u.es_activo = 1
    LIMIT 1;
END$$

DROP PROCEDURE IF EXISTS `sp_programas_buscar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_programas_buscar`(
    IN p_criterio VARCHAR(100)
)
BEGIN
    -- Normalización defensiva del término de búsqueda
    SET @termino = CONCAT('%', IFNULL(p_criterio, ''), '%');

    SELECT 
        id_programa,
        codigo_programa,
        nombre_programa,
        estado,
        creado_en
    FROM programas_estudio
    WHERE (codigo_programa LIKE @termino OR nombre_programa LIKE @termino)
    ORDER BY id_programa DESC;
END$$

DROP PROCEDURE IF EXISTS `sp_programas_listar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_programas_listar`()
BEGIN
    SELECT 
        id_programa,
        codigo_programa,
        nombre_programa,
        estado,
        creado_en
    FROM programas_estudio
    ORDER BY id_programa DESC;
END$$

DROP PROCEDURE IF EXISTS `sp_roles_listar`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_roles_listar`()
BEGIN
    SELECT id_rol, nombre_rol
    FROM roles
    ORDER BY nombre_rol;
END$$

DELIMITER ;
