-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 31-10-2024 a las 02:08:41
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_final`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

DROP TABLE IF EXISTS `administrador`;
CREATE TABLE IF NOT EXISTS `administrador` (
  `idAdministrador` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `permisos` text NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`idAdministrador`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`idAdministrador`, `nombre`, `permisos`, `email`) VALUES
(1, 'hola mundo\r\n', 'Gestionar usuarios y empleados', 'pruebas@gmail.com'),
(3, 'loquito', 'otras pruebas fallidas \r\n', 'loco@email.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

DROP TABLE IF EXISTS `departamento`;
CREATE TABLE IF NOT EXISTS `departamento` (
  `id_departamento` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `gerente` varchar(50) NOT NULL,
  PRIMARY KEY (`id_departamento`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre`, `gerente`) VALUES
(1, 'Recursos Humanos', 'Ana López'),
(2, 'Desarrollo Sostenible', 'Carlos Ramírez'),
(4, 'poo', 'rojo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `idEmpleado` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fechaInicioContrato` date NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  `idDepartamento` int NOT NULL,
  `idRol` int NOT NULL DEFAULT '2',
  PRIMARY KEY (`idEmpleado`),
  UNIQUE KEY `email` (`email`),
  KEY `idDepartamento` (`idDepartamento`),
  KEY `idRol` (`idRol`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`idEmpleado`, `nombre`, `direccion`, `telefono`, `email`, `password`, `fechaInicioContrato`, `salario`, `idDepartamento`, `idRol`) VALUES
(1, 'Juan Pérez', 'Av. Siempre Viva 123', '123456789', 'juan.perez@example.com', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '2023-01-15', 30000.00, 2, 2),
(4, 'Carla López', 'Calle Secundaria 456', '123456789', 'carla.lopez@correo.com', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', '2022-05-10', 3200.00, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

DROP TABLE IF EXISTS `informe`;
CREATE TABLE IF NOT EXISTS `informe` (
  `idInforme` int NOT NULL AUTO_INCREMENT,
  `tipoInforme` varchar(50) NOT NULL,
  `fechaGeneracion` date NOT NULL,
  `idAdministrador` int NOT NULL,
  PRIMARY KEY (`idInforme`),
  KEY `idAdministrador` (`idAdministrador`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `informe`
--

INSERT INTO `informe` (`idInforme`, `tipoInforme`, `fechaGeneracion`, `idAdministrador`) VALUES
(1, 'Informe Mensual de Recursos Humanos', '2024-09-30', 1),
(2, 'Informe de Progreso de Desarrollo', '2024-10-10', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
CREATE TABLE IF NOT EXISTS `proyecto` (
  `idProyecto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  `fechaInicio` date NOT NULL,
  `fechaTermino` date NOT NULL,
  PRIMARY KEY (`idProyecto`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`idProyecto`, `nombre`, `descripcion`, `fechaInicio`, `fechaTermino`) VALUES
(1, 'Sistema de Gestión de Empleados', 'Desarrollo de un sistema para gestionar empleados y sus horas de trabajo', '2024-01-15', '0000-00-00'),
(2, 'eva2_poo', 'esto es una prueba de funcionamiento', '2024-02-01', '2023-12-03'),
(5, 'poo', 'eva 2', '2024-12-01', '2025-01-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

DROP TABLE IF EXISTS `registro_tiempo`;
CREATE TABLE IF NOT EXISTS `registro_tiempo` (
  `idRegistro` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `horasTrabajadas` decimal(5,2) NOT NULL,
  `descripcion` text,
  `idEmpleado` int NOT NULL,
  `idProyecto` int NOT NULL,
  PRIMARY KEY (`idRegistro`),
  KEY `idEmpleado` (`idEmpleado`),
  KEY `idProyecto` (`idProyecto`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `registro_tiempo`
--

INSERT INTO `registro_tiempo` (`idRegistro`, `fecha`, `horasTrabajadas`, `descripcion`, `idEmpleado`, `idProyecto`) VALUES
(1, '2024-10-01', 4.50, 'Revisión de diseño y estructura de base de datos', 1, 1),
(2, '2024-10-02', 6.00, 'Implementación del módulo de autenticación', 2, 1),
(3, '2024-12-15', 9.00, 'ahora funciona todo', 3, 2),
(4, '2024-04-12', 10.00, 'cambie las bases de datos otraves ', 1, 1),
(5, '2023-12-08', 9.00, 'nada que acotar ', 3, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

DROP TABLE IF EXISTS `rol`;
CREATE TABLE IF NOT EXISTS `rol` (
  `idRol` int NOT NULL DEFAULT '2',
  `nombreRol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`idRol`),
  UNIQUE KEY `nombre_rol` (`nombreRol`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`idRol`, `nombreRol`) VALUES
(1, 'Administrador'),
(2, 'Empleado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `idRol` int NOT NULL DEFAULT '2',
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `username` (`username`),
  KEY `idRol` (`idRol`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `username`, `password`, `idRol`) VALUES
(1, 'admin1', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 1),
(2, 'empleado1', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 2),
(3, 'empleado2', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
