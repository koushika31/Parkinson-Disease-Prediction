-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 27, 2024 at 04:10 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1naildiseasedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `ctb`
--

CREATE TABLE `ctb` (
  `id` bigint(50) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Website` varchar(250) NOT NULL,
  `City` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `ctb`
--

INSERT INTO `ctb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `Website`, `City`) VALUES
(3, 'kmc', '9486365535', 'kmc@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'www.kmc.com', 'Trichy');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(50) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `City` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Age`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `City`) VALUES
(1, 'sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', ''),
(2, 'sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'muzammin', 'muzammin', ''),
(3, 'sangeeth Kumar', '20', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san12', 'san12', 'Trichy');
