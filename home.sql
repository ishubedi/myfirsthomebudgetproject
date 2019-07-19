-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.48 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5222
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for home_budget
DROP DATABASE IF EXISTS `home_budget`;
CREATE DATABASE IF NOT EXISTS `home_budget` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `home_budget`;

-- Dumping structure for table home_budget.expenses
DROP TABLE IF EXISTS `expenses`;
CREATE TABLE IF NOT EXISTS `expenses` (
  `ExTd` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `grocery` int(10) DEFAULT NULL,
  `medicines` int(10) DEFAULT NULL,
  `fuel` int(10) DEFAULT NULL,
  `clothes` int(10) DEFAULT NULL,
  `entertainment` int(10) DEFAULT NULL,
  `electricity` int(10) DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  PRIMARY KEY (`ExTd`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table home_budget.income
DROP TABLE IF EXISTS `income`;
CREATE TABLE IF NOT EXISTS `income` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `catname` text,
  `catamount` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
expensesexpensesincomeloginloginlogin