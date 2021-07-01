/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - oliveprediction
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `oliveprediction`;

USE `oliveprediction`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `dataset` */

DROP TABLE IF EXISTS `dataset`;

CREATE TABLE `dataset` (
  `State_Name` varchar(30) DEFAULT NULL,
  `District_Name` varchar(30) DEFAULT NULL,
  `Crop_Year` varchar(30) DEFAULT NULL,
  `Season` varchar(30) DEFAULT NULL,
  `Area` varchar(30) DEFAULT NULL,
  `Production` varchar(30) DEFAULT NULL,
  `Result` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dataset` */

/*Table structure for table `m_dataset` */

DROP TABLE IF EXISTS `m_dataset`;

CREATE TABLE `m_dataset` (
  `State_Name` varchar(30) DEFAULT NULL,
  `District_Name` varchar(30) DEFAULT NULL,
  `Crop_Year` varchar(30) DEFAULT NULL,
  `Season` varchar(30) DEFAULT NULL,
  `Area` varchar(30) DEFAULT NULL,
  `Production` varchar(30) DEFAULT NULL,
  `Result` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `m_dataset` */

/*Table structure for table `performance` */

DROP TABLE IF EXISTS `performance`;

CREATE TABLE `performance` (
  `Algorithm` varchar(50) DEFAULT NULL,
  `Accuracy` varchar(50) DEFAULT NULL,
  `precision` varchar(50) DEFAULT NULL,
  `recall` varchar(50) DEFAULT NULL,
  `F1score` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `performance` */

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `Name` varchar(100) DEFAULT NULL,
  `UserId` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `MobNo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
