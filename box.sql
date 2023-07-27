-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 17, 2023 at 01:38 PM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `box`
--

-- --------------------------------------------------------

--
-- Table structure for table `box`
--

CREATE DATABASE IF NOT EXISTS `box` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `box`;

DROP TABLE IF EXISTS `box`;
CREATE TABLE IF NOT EXISTS `box` (
  `boxID` int NOT NULL,
  `restaurant_id` int NOT NULL,
  `cust_id` varchar(30) NOT NULL,
  `postTime` datetime NOT NULL,
  `quantity` int,
  `collectionTime` datetime NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `description` varchar(64) DEFAULT NULL,
  `boxName` varchar(64) NOT NULL,
  `postDate` date NOT NULL,
  PRIMARY KEY (`boxID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `box` (`boxID`, `restaurant_id`, `cust_id`, `postTime`, `quantity`, `collectionTime`, `price`, `description`, `boxName`,`postDate`) VALUES
(1, 82763492, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-04-02 21:43:02', 2, '2023-04-02 21:43:02', 11, 'nil', 'Subway-PS A','2023-04-05'),
(2, 82763492, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-04-02 21:43:02', 2, '2023-04-02 21:43:02', 11, 'nil', 'Subway-PS B','2023-04-05'),
(3, 82763491, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-04-02 21:43:02', 2, '2023-04-02 21:43:02', 11, 'nil', 'Sushi Express-PLQ A','2023-04-05'),
(4, 82763491, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-04-02 21:43:02', 11, 'nil', 'Sushi Express-PLQ A','2023-04-05'),
(5, 82763491, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Sushi Express-PLQ C','2023-04-05'),
(6, 82763490, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Saizeriya-CCP A','2023-04-05'),
(7, 82763490, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Saizeriya-CCP B','2023-04-05'),
(8, 82763493, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Yoshinoya- BJ A','2023-04-05'),
(9, 82763493, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Yoshinoya- BJ B','2023-04-05'),
(10, 82763494, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Stuffd- BM A','2023-04-05'),
(11, 82763494, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Stuffd- BM B','2023-04-05'),
(12, 82763494, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Stuffd- BM C','2023-04-05'),
(13, 82763495, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Maki-San- WD A','2023-04-05'),
(14, 82763495, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Maki-San- WD B','2023-04-05'),
(15, 82763495, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Maki-San- WD C','2023-04-05'),
(16, 82763496, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'PastaMania- CSM A','2023-04-05'),
(17, 82763496, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'PastaMania- CSM B','2023-04-05'),
(18, 82763496, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'PastaMania- CSM C','2023-04-05'),
(19, 82763496, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'PastaMania- CSM D','2023-04-05'),
(20, 82763497, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Guzman y Gomez- OG A','2023-04-05'),
(21, 82763497, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Guzman y Gomez- OG B','2023-04-05'),
(22, 82763497, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Guzman y Gomez- OG C','2023-04-05'),
(23, 82763498, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Kanshoku Ramen Bar- OG A','2023-04-05'),
(24, 82763499, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Cedele- WP A','2023-04-05'),
(25, 82763499, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Cedele- WP B','2023-04-05'),
(26, 82863491, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Green Dot- NP A','2023-04-05'),
(27, 82863492, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Bornga- SC A','2023-04-05'),
(28, 82863493, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Green Signature- WP A','2023-04-05'),
(29, 82863494, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Pizza Hut- TM A','2023-04-05'),
(30, 82863495, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'MOS Burger- JC A','2023-04-05'),
(31, 82863496, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Nakhon Kitchen Thai Restaurant- K A','2023-04-05'),
(32, 82863497, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Papparich- PP A','2023-04-05'),
(33, 82863498, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'NamNam Noodle Bar- RC A','2023-04-05'),
(34, 82863499, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Astons Specialties- C A','2023-04-05'),
(35, 82963490, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Tim Ho Wan- J A','2023-04-05'),
(36, 82963491, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Shin-Sapporo Ramen - OG A','2023-04-05'),
(37, 82963492, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Tori-Q - J8 A','2023-04-05'),
(38, 82963493, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Four Leaves - YTP A','2023-04-05'),
(39, 82963494, '0cxmPeUd0xaFgebi0qrRF5nV4ot1', '2023-03-18 21:43:02', 2, '2023-03-18 21:43:02', 11, 'nil', 'Breadtalk - JKC A','2023-04-05');

ALTER TABLE box
MODIFY COLUMN quantity INT UNSIGNED NOT NULL DEFAULT 0;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


