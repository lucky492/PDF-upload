-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2022 at 03:18 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lib`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `sno` int(200) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `title` text,
  `subtitle` text,
  `content` text,
  `date_created` text,
  `file` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`sno`, `slug`, `title`, `subtitle`, `content`, `date_created`, `file`) VALUES
(2, '', 'helo learn', 'learn about stock market for free', 'nnnnnlorem323', '2022-02-10 02:13:58.492641', ''),
(3, '', 'this is finance books', 'ttttttttttttttttttttttttttttttttttt', 'errrrrrrrrrrefddddddddddddd333333333333333333ddddddddddddddc ', '2022-02-10 02:14:18.546788', ''),
(4, '', 'e3e3e', '3q3xced', 'wdedegeer', '2022-02-10 02:14:59.664140', ''),
(5, '', 'this is my last blog bro', 'last blog', 'pups kkke nwhwh shwen ahrne wowe wqow wwow wow wjss', '2022-02-14 02:07:18.386137', 'IMG-20200924-WA0001.jpg'),
(6, '', 'blog with secong image', 'image bog', 'wdeuidue', '2022-02-14 06:13:24.044611', 'IMG20191107094936.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `finance_books`
--

CREATE TABLE `finance_books` (
  `sno` int(11) NOT NULL,
  `finance_books_data` text,
  `finance_books_image` text,
  `finance_books_name` text,
  `finance_books_content` text,
  `date_created` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `finance_books`
--

INSERT INTO `finance_books` (`sno`, `finance_books_data`, `finance_books_image`, `finance_books_name`, `finance_books_content`, `date_created`) VALUES
(3, 'PDF Gallery_20211202_120801.pdf', 'IMG_20200725_094413.jpg', 'pdf', 'pfd', NULL),
(5, 'IMG_20201104_095728.jpg', 'IMG_20200801_121029.jpg', 'PDF3', 'PDF3', NULL),
(6, 'IMG20190815091556.jpg', 'IMG20190814163825.jpg', 'yhgggrfd', 'grewwr', '2022-02-14 06:14:50.530557');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `name` text,
  `message` text,
  `date_created` text,
  `sno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `school_books`
--

CREATE TABLE `school_books` (
  `sno` int(11) NOT NULL,
  `school_books_data` text,
  `school_books_image` text,
  `school_books_name` text,
  `school_books_content` text,
  `date_created` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school_books`
--

INSERT INTO `school_books` (`sno`, `school_books_data`, `school_books_image`, `school_books_name`, `school_books_content`, `date_created`) VALUES
(10, 'IMG-20200924-WA0017.jpg', 'IMG-20201110-WA0000.jpg', 'pdf2', 'pdf2', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `special_books`
--

CREATE TABLE `special_books` (
  `special_books_data` text,
  `special_books_image` text,
  `special_books_name` text,
  `special_books_content` text,
  `sno` int(11) NOT NULL,
  `date_created` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `special_books`
--

INSERT INTO `special_books` (`special_books_data`, `special_books_image`, `special_books_name`, `special_books_content`, `sno`, `date_created`) VALUES
('Phil_Good_-_Be_Somebody_(Lyric_Video).mp3', 'IMG-20200924-WA0012.jpg', 'song', 'songmp3', 2, NULL),
('IMG_20201104_095422.jpg', 'IMG_20201104_095205.jpg', 'songddd', 'sonhh', 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `uncategorised_books`
--

CREATE TABLE `uncategorised_books` (
  `sno` int(11) NOT NULL,
  `uncategorised_books_data` text,
  `uncategorised_books_image` text,
  `uncategorised_books_name` text,
  `uncategorised_books_content` text,
  `date_created` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `uncategorised_books`
--

INSERT INTO `uncategorised_books` (`sno`, `uncategorised_books_data`, `uncategorised_books_image`, `uncategorised_books_name`, `uncategorised_books_content`, `date_created`) VALUES
(2, 'IMG_20201104_085514.jpg', 'IMG-20201109-WA0000.jpg', 'song2', 'sonfgf', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `finance_books`
--
ALTER TABLE `finance_books`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `school_books`
--
ALTER TABLE `school_books`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `special_books`
--
ALTER TABLE `special_books`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `uncategorised_books`
--
ALTER TABLE `uncategorised_books`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `finance_books`
--
ALTER TABLE `finance_books`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `school_books`
--
ALTER TABLE `school_books`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `special_books`
--
ALTER TABLE `special_books`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `uncategorised_books`
--
ALTER TABLE `uncategorised_books`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
