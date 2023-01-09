-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 15-12-2022 a las 00:12:51
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `luchadores`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gladiador`
--

CREATE TABLE `gladiador` (
  `Vida` int(11) NOT NULL,
  `Lucha` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `gladiador`
--

INSERT INTO `gladiador` (`Vida`, `Lucha`) VALUES
(80, 'EL luchador se puede Lucha'),
(300, 'EL gladiador si puede Lucha'),
(20000, 'EL gladiador no puede Lucha'),
(50, 'EL gladiador no puede Luchar'),
(80, 'EL luchador se puede Lucha'),
(300, 'EL gladiador si puede Lucha'),
(20000, 'EL gladiador no puede Lucha'),
(50, 'EL gladiador no puede Luchar'),
(199, 'EL gladiador si puede Luchar'),
(80, 'EL luchador se puede Lucha'),
(300, 'EL gladiador si puede Lucha'),
(20000, 'EL gladiador no puede Lucha'),
(50, 'EL gladiador no puede Luchar'),
(80, 'EL luchador se puede Lucha'),
(300, 'EL gladiador si puede Lucha'),
(20000, 'EL gladiador no puede Lucha'),
(50, 'EL gladiador no puede Luchar'),
(199, 'EL gladiador si puede Luchar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `user` varchar(55) NOT NULL,
  `password` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`user`, `password`) VALUES
('Andres', '37693cfc748049e45d87b8c7d8b9aacd'),
('walo', '4d186321c1a7f0f354b297e8914ab240'),
('walo', '149815eb972b3c370dee3b89d645ae14'),
('asd', '202cb962ac59075b964b07152d234b70'),
('we', 'ff1ccf57e98c817df1efcd9fe44a8aeb'),
('mati', '37693cfc748049e45d87b8c7d8b9aacd'),
('andres', '37693cfc748049e45d87b8c7d8b9aacd');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
