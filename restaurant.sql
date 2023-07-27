-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurant`
--
CREATE DATABASE IF NOT EXISTS `restaurant` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `restaurant`;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
CREATE TABLE IF NOT EXISTS `restaurant` (
  `restaurant_id` int(11) NOT NULL AUTO_INCREMENT,
  `restaurant_name` varchar(100) NOT NULL,
  `restaurant_location` varchar(100) NOT NULL,
  `latitude` float(53) NOT NULL,
  `longitude` float(53) NOT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`restaurant_id`, `restaurant_name`, `restaurant_location`, `latitude`, `longitude`) VALUES
(82763492, 'Subway (Plaza Singapura)', '68 Orchard Rd, B2-33/34, Plaza Singapura Singapore 238839', '1.299953364', '103.845707596'),
(82763491, 'Sushi Express (PLQ Mall)', '10 Paya Lebar Rd, #04-12 PLQ Mall, Singapore 409057', '1.317472', '103.892616'),
(82763493, 'Yoshinoya (Bugis Junction)', '230 Victoria St, B1-10, Singapore 188024', '1.29991840776', '103.855588461'),
(82763494, 'Stuffd (Bedok Mall)', 'Bedok Mall, #B2-22, 311 New Upper Changi Road', '1.324733', '103.9292024'),
(82763495, 'Maki-San (Woodlands Drive)', '676 Woodlands Drive 71 #01-04 Kampung Admiralty, Singapore 730676', '1.43952', '103.79996'),
(82763496, 'PastaMania (City Square Mall)', '180 Kitchener Rd, #02-21/22, Singapore 208539', '1.31142', '103.85662'),
(82763497, 'Guzman y Gomez (Orchard Gateway)', '01-03 Orchard Gateway, 277 Orchard Road, Singapore 238858', '1.30204691192', '103.836534644'),
(82763498, 'Kanshoku Ramen Bar (Orchard Gateway)', '277 Orchard Road #01-06 Orchard Gateway, Singapore 238858', '1.304619', '103.83154'),
(82763499, 'Cedele (Wheelock Place)', '501 Orchard Road #03-14 Wheelock Place, Singapore 238880', '1.304325', '103.83119'),
(82863493, 'Green Signature (Waterway Point)', '83 Punggol Central #01-29 Waterway Point, Singapore 828761', '	1.4067234', '103.9028214'),
(82863491, 'Green Dot (Northpoint)', '930 Yishun Avenue 2, #B2-09/11, Northpoint City North Wing, Singapore 769098', '1.429318', '103.8361064'),
(82863492, 'Bornga (Suntec City)', '3 Temasek Boulevard Suntec City Mall #01-641/642, East Wing, Suntec City Mall, Singapore 038983', '1.293889', '103.859795'),
(82863494, 'Pizza Hut (Tampines Mall)', '4 Tampines Central 5, #02-02 Tampines Mall, Singapore 529510', '1.35241255823', '103.945386195'),
(82863490, 'Delifrance (JEM)', 'Jem 50, 16 Jurong Gateway Rd, #B1-K15, 608549', '1.33335890549', '103.743081114'),
(82863495, 'MOS Burger (JCube)', '2 Jurong East Central 1, #01-08 JCube, Singapore 609731', '1.33332', '103.74019'),
(82763490, 'Saizeriya (Changi City Point)', '5 Changi Business Park Central 1 #B1-44/45 Changi City Point Singapore 486038', '1.33433970956', '103.962364421'),
(82863496, 'Nakhon Kitchen Thai Restaurant (Kovan)', '212 Hougang St 21, #01-341, Singapore 530212', '1.359471884', '103.888512674'),
(82863497, 'Papparich (Parkway Parade)', '80 Marine Parade Road #01-17A Parkway Parade Shopping Complex, Singapore 449269', '1.30109', '103.90525'),
(82863498, 'NamNam Noodle Bar (Raffles City)', '252 North Bridge Road #B1-47, Raffles City Shopping Centre, Singapore 179103', '1.29382', '103.85278'),
(82863499, 'Astons Specialties (The Cathay)', '2 Handy Road, #04-03/04, Singapore 229233', '1.299086', '103.847664'),
(82963490, 'Tim Ho Wan (Jewel)', 'No 02-223, Jewel Changi Airport, 78 Airport Blvd., Changi Jewel, Singapore 819666', '1.360200502', '103.98907245'),
(82963491, 'Shin-Sapporo Ramen (Orchard Gateway)', '277 Orchard Road #B2-04A/05 Orchard Gateway Singapore 238858', '1.30011123701', '103.839363583'),
(82963492, 'Tori-Q (Junction 8)', '9 Bishan Pl., #B1-25 Junction 8 Shopping Centre, Singapore 579837', '1.35054874971', '103.848658527'),
(82963493, 'Four Leaves (Yew Tee Point)', '#B1-33/34, Yew Tee Point (21 Choa Chu Kang North 6), Singapore 689578', '1.3974994647779', '103.74691396612'),
(82963494, 'Breadtalk (Joo Koon Circle)', '1 Joo Koon Circle #01-44/45/46, Singapore 629117', '1.3274996', '103.678239'),
(82963495, 'Breadtalk (Nex)', '23 Serangoon Central, #B2-58 59 NEX, Singapore 556083', '1.35092236228', '103.87288154'),
(82963496, 'Lenu (Northpoint City)', '930 Yishun Ave 2, #B1-101, Singapore 768019', '1.42944', '103.83581'),
(82963497, 'Din Tai Fung (Jurong Point)', '63 Jurong West Central 3 #1-68 Jurong Point Shopping Centre, Singapore 648331', '1.338916', '103.70572'),
(82963498, 'Pepper Lunch Express (West Mall)', '1 Bukit Batok Central Link #04-01 West Mall Koufu Singapore 658713', '1.35018848947', '103.749255072'),
(82963499, "Swensen's (West Mall)", '1 Bukit Batok Central Link West Mall #02-05 West Mall, Singapore 658713', '1.35011', '103.74922'),
(83063490, "Swensen's (City Square Mall)", '180 Kitchener Rd, #03-37/38, Singapore 208539', '1.310897', '103.856613'),
(83063491, 'Genki Sushi (Waterway Point)', '83 Punggol Central, #02-23 Waterway Point, Singapore 828761', '1.406669', '103.902012'),
(83063492, 'Genki Sushi (Bugis Junction)', '201 Victoria Street Bugis+ #01-13, Bugis, Singapore 188067', '1.299974', '103.85381'),
(83063493, 'Genki Sushi (Chinatown Point)', '133 New Bridge Road Chinatown Point #02-33 Singapore 059413', '1.28516', '103.84485'),
(83063494, 'Big Fish Small Fish (Bugis Junction)', '200 Victoria Street, Bugis Junction #04-05, Singapore 188021', '1.29966', '103.85571'),
(83063495, 'MOS Burger (AMK Hub)', '53 Ang Mo Kio Avenue 3 Amk Hub 3 #01-33, Singapore 569933', '1.36941', '103.84841'),
(83063496, 'Krispy Kreme (Great World City)', '1 Kim Seng Promenade, #B1, K110 Great World, Singapore 237994', '1.29360125251', '103.831856753'),
(83063497, 'J.Co Donuts & Coffee (Paya Lebar Square)', '60 Paya Lebar Rd, #01-78, 79, K2, Singapore 409051', '1.31884719171', '103.892367201'),
(83063498, 'Eighteen Chefs (The Star Vista)', '	#02-22, The Star Vista (1 Vista Exchange Green), Singapore 138617', '1.3062043742121', '103.78931115646'),
(83063499, 'Eighteen Chefs (Eastpoint Mall)', '3 Simei Street 6 Eastpoint Mall #01-12, Singapore 528833', '1.34256', '103.9528'),
(83163490, 'Bonchon (Boat Quay)', '53 Boat Quay, Singapore 049842', '1.287185', '103.84944'),
(83163491, 'Thai Express (Tampines 1)', '10 Tampines Central 1, #04-09/#05-08, Singapore 529536', '1.35428', '103.94503'),
(83163492, 'Ichiban Boshi (Parkway Parade)', '80 Marine Parade Road, Parkway Parade #02-12, Singapore 449269', '1.30107', '103.90517'),
(83163493, 'Sakae Sushi (Parkway Parade)', '80 Marine Parade #B1-84C Parkway Parade, Singapore 449269', '1.30174309', '103.905778392'),
(83163494, 'Buddy Hoagies (Waterway Point)', '83 Punggol Central Watertown Waterway Point, 02-22, Singapore 828761', '1.40645', '103.90202'),
(83163495, 'Buddy Hoagies (Bukit Timah)', '170 Upper Bukit Timah Road Bukit Timah Shopping Centre #B1-05 Singapore 588179', '1.343163', '103.77572'),
(83163496, 'Toast Box (Changi City Point)', '#01-12 Changi Business Park Central 1, Singapore 486038', '1.33418', '103.96277'),
(83163497, 'Burger King (Plaza Singapura)', '68 Orchard Road Plaza Singapura B1-11, Singapore 238839', '1.30048', '103.84491'),
(83163498, 'Burger King (Leisure Park)', '5 Stadium Walk, #01-43, Leisure Park Kallang, 5 Stadium Walk, #01-43, Singapore 397693', '1.301980595', '103.87661834'),
(83163499, 'Subway (The Central)', '6 Eu Tong Sen Street The Central 01-66 The Central, Singapore 059817', '1.28882', '103.84662'),
(83263490, 'Subway (Far East Plaza)', '14 Scotts Road Far East Plaza #06-00, Singapore 228213', '1.30691', '103.83354'),
(83263491, 'Subway (Chinatown Point)', '5133 New Bridge road, B2-37 Chinatown Point, Singapore 059413', '1.28516', '103.8448499'),
(83263492, 'A-One Claypot House (Chinatown Point)', '133 New Bridge Road Chinatown Point B1-47, Singapore 059413', '1.285275', '103.844635'),
(83263493, 'Saizeriya (Clementi)', '321 Clementi Ave 3, #02-05/06/07 Singapore 129905', '1.312', '103.76503'),
(83263494, 'New Taiwan Porridge Restaurant (Amoy Street)', '110 Amoy St #01-00, Singapore 069930', '1.28205', '103.84748'),
(83263495, 'Fong Sheng Hao (PLQ Mall)', '#B2-04 PLQ Mall (10 Paya Lebar Road) Singapore 409057', '1.3173635249927', '103.89283418655'),
(83263496, 'Little Caesars (Thomson Plaza)', '301 Upper Thomson Rd, Thomson Plaza Singapore 574408 #01-108', '1.28387', '103.85229'),
(83263497, 'Little Caesars (Raffles)', '#01-05 Income at Raffles Singapore 049317', '1.2842109', '103.85249'),
(83263498, 'Seorae Korean Charcoal BBQ (JEM)', '50 Jurong Gateway Road Jem #b1-10 Singapore 608549', '1.33285', '103.74333'),
(83263499, 'Seorae Korean Charcoal BBQ (Plaza Singapura)', 'Plaza Singapura #02-01, 68 Orchard Road, Singapore 238839', '1.30001618556', '103.844865979'),
(83363490, 'Heavenly Wang (Changi Airport T3)', '80 Airport Blvd Changi Airport T3, #01-25, Singapore 819663', '1.3560897', '103.9863362'),
(83363491, 'Heavenly Wang (Raffles Place Clifford Centre)', '4 Raffles Place, #B1-08 Clifford Centre, Singapore 048621', '1.28389790163', '103.851889546'),
(83363492, 'Toast Box (Chinatown Point)', '133 New Bridge Road #01-45 Chinatown Point, Singapore 059413', '1.285726', '103.844734'),
(83363493, 'Toast Box (Bishan)', '9 Bishan Place #01-35/36 Singapore 579837', '1.35104180622', '103.848190968'),
(83363494, 'Tiong Bahru Bakery (Tiong Bahru)', '56 Eng Hoon St, #01-70', '1.293587', '103.853818'),
(83363495, 'Cedele (112 Katong)', '112 E East Coast Road 112 Katong #01-02, Singapore 428802', '1.30548', '103.90483'),
(83363496, 'Shilin Taiwan Street Snacks (NEX)', '23 Serangoon Central, #03-K12, Singapore 556083', '1.350285', '103.872712'),
(83363497, 'Lee Wee & Brothers (Jurong)', '50 Jurong Gateway Rd, B1-K12, Singapore 608549', '1.333462', '103.7434183'),
(83363498, 'Wok Hey (Hougang)', '90 Hougang Ave 10 #01-40, Singapore 538766', '1.37210269992', '103.893611044'),
(83363499, 'Wok Hey (Pasir Ris)', '1 Pasir Ris Central St 3, B1-K05 White Sands, Singapore 518457', '1.372316', '103.949925'),
(83463490, 'Pizza Hut (Ghim Moh)', 'Blk 21 Ghim Moh #01-215, Singapore 270021', '1.3106423', '103.7890755'),
(83463491, 'Pizza Hut (Causeway Point)', 'No 1 Woodlands Square #1-25 Causeway Point #B1-25 Singapore 738099', '1.4361', '103.78599'),
(83463492, 'Saladstop (Orchard)', '391 Orchard Road Ngee Ann City Tower a #b2 07-9-3, Singapore 238873', '1.30300312544', '103.834238718'),
(83463493, 'Saladstop (Capital Tower)', 'Robinson Road #01-05, Capital Tower 168, Singapore 068912', '1.277738', '103.847960'),
(83463494, 'The Rice Table (Orchard Road)', '360 Orchard Road International Building Floor 02 Unit 10 09, Singapore 238869', '1.305914', '103.83085');
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;