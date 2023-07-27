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

CREATE DATABASE IF NOT EXISTS `activity_log` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `activity_log`;

DROP TABLE IF EXISTS `activity_log`;
CREATE TABLE IF NOT EXISTS `activity_log` (
  `activityID` int NOT NULL AUTO_INCREMENT,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `activity_details` varchar(30) NOT NULL,
  PRIMARY KEY (`activityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


INSERT INTO `activity_log` (`activityID`, `created`, `activity_details`) VALUES
(1,'2023-03-26 21:43:02','Order not found.');
ALTER TABLE activity_log
