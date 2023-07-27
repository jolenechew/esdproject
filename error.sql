SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `activity_log`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE DATABASE IF NOT EXISTS `error` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `error`;

DROP TABLE IF EXISTS `error`;
CREATE TABLE IF NOT EXISTS `error` (
  `errorID` int NOT NULL AUTO_INCREMENT,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `error_details` varchar(30) NOT NULL,
  PRIMARY KEY (`errorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


INSERT INTO `error` (`errorID`, `created`, `error_details`) VALUES
(1,'2023-03-26 21:43:02','Order not found.');
ALTER TABLE error