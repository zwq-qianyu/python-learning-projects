-- MySQL dump 10.13  Distrib 5.5.56, for Linux (x86_64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.5.56-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `abstract` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `uid` int(10) unsigned DEFAULT NULL,
  `pcount` int(10) unsigned DEFAULT '0',
  `flag` tinyint(3) unsigned DEFAULT '0',
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'wen1','this is the first blog','This is zhangsan\'s first blog.',1,0,0,'2018-03-24 14:14:08'),(2,'wen2','second blog','this is zhangsan\'s second blog.',1,0,0,'2018-03-24 14:14:40'),(3,'wen1 of lisi','first blog','this is lisi\'s first blog.',2,0,0,'2018-03-24 14:14:45'),(4,'wen2','second blog','this is lisi\'s second blog.',2,0,0,'2018-03-24 14:14:50'),(5,'wenzhang of wangwu','first blog','this is wangwu\'s first blog.',3,0,0,'2018-03-24 14:14:54'),(6,'blog of wangwu','first blog','this is wangwu\'s second blog.',3,0,0,'2018-03-24 14:14:57'),(7,'wen3 of wangwu','third blog','this is wangwu\'s third blog.',3,0,0,'2018-03-24 14:15:00'),(8,'wenzhang of lihua','first blog','this lihua\'s first blog.',5,0,0,'2018-03-24 14:15:04'),(9,'wen1 of zhaoliu','first blog','this zhaoliu\'s first blog.',4,0,0,'2018-03-24 14:15:07'),(10,'wen2','one blog','this zhaoliu\'s blog.',4,0,0,'2018-03-24 14:15:15');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'zhangsan','123@163.com','2018-03-24 12:59:32'),(2,'lisi','234@163.com','2018-03-24 13:08:16'),(3,'wangwu','345@163.com','2018-03-24 13:08:22'),(4,'zhaoliu','456@163.com','2018-03-24 13:08:28'),(5,'lihua','567@163.com','2018-03-24 13:08:33');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-24 14:19:49
