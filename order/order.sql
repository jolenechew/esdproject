

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- Once a transaction has been started, any subsequent SQL statements executed as part of that transaction will not be visible to other database users until the transaction has been completed. This ensures that the database remains in a consistent state, even if multiple users are accessing and modifying the data simultaneously.

-- In addition to START TRANSACTION, SQL also provides other transaction control statements such as COMMIT and ROLLBACK, which are used to either commit the changes made in a transaction or to roll back the changes made in the event of an error or exception.

--
-- Database: `order`
--
CREATE DATABASE IF NOT EXISTS `order` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `order`;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_number` int NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  `restaurant_id` int NOT NULL,
  `boxID` int NOT NULL,
  `charge_id` varchar(50) NOT NULL,
  `refund_id` varchar(50) NOT NULL,
  `quantity` int,
  `total_bill` decimal(5,2),
  `transaction_no` int,
  `payment_method` varchar(50),
  `currency` varchar(50),
  `status` varchar(10) NOT NULL DEFAULT 'NEW',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order`
--

INSERT INTO `orders` (`order_id`,`customer_number`, `customer_id`, `restaurant_id`, `boxID`, `charge_id`, `refund_id`, `quantity`, `total_bill`, `transaction_no`, `payment_method`, `currency`, `status`, `created`, `modified`) VALUES
(1, 90219935, 'abc100', 02020202 , 1, '908', 'NULL', 3, 9.00, 908070605, 'Credit Card', 'SGD', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');

INSERT INTO `orders` (`order_id`, `customer_number`, `customer_id`, `restaurant_id`, `boxID`, `charge_id`, `refund_id`, `quantity`, `total_bill`, `transaction_no`, `payment_method`, `currency`, `status`, `created`, `modified`) VALUES
(2, 90219935, 'abc100', 02020202 , 2, '908', 'NULL', 3, 9.00, 908070605, 'Credit Card', 'SGD', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');
COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

select * from orders
