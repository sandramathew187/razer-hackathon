SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE DATABASE IF NOT EXISTS `Sponsor` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Sponsor`;

DROP TABLE IF EXISTS `Sponsor`;
CREATE TABLE IF NOT EXISTS `Sponsor` (
  `companyname` varchar(128) NOT NULL,
  `depositid` varchar(256) NOT NULL,
  `companyid` varchar(128) NOT NULL,
  `percentagerevenue` varchar(128) NOT NULL,
  PRIMARY KEY (`depositid`)
  );