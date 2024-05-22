-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: transporter
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `name` varchar(128) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('agadir',1,'2024-05-20 01:02:47','2024-05-20 02:02:47'),('agadir',2,'2024-05-20 01:03:18','2024-05-20 02:03:18'),('agadir',3,'2024-05-20 01:04:22','2024-05-20 02:04:22'),('agadir',4,'2024-05-20 01:05:35','2024-05-20 02:05:35'),('agadir',5,'2024-05-20 01:05:42','2024-05-20 02:05:42'),('agadir',6,'2024-05-20 01:06:01','2024-05-20 02:06:01'),('agadir',9,'2024-05-20 01:08:37','2024-05-20 02:08:37'),('agadir',10,'2024-05-20 01:22:45','2024-05-20 02:22:46'),('agadir',11,'2024-05-20 01:23:48','2024-05-20 02:23:48'),('agadir',12,'2024-05-20 01:27:08','2024-05-20 02:27:08'),('agadir',13,'2024-05-20 01:27:21','2024-05-20 02:27:21'),('agadir',14,'2024-05-20 01:27:48','2024-05-20 02:27:48'),('agadir',15,'2024-05-20 01:28:44','2024-05-20 02:28:44'),('agadir',16,'2024-05-20 01:28:50','2024-05-20 02:28:50'),('agadir',17,'2024-05-20 01:28:51','2024-05-20 02:28:51'),('agadir',18,'2024-05-20 01:28:52','2024-05-20 02:28:52'),('agadir',19,'2024-05-20 01:37:38','2024-05-20 02:37:38'),('agadir',20,'2024-05-20 01:40:20','2024-05-20 02:40:20'),('agadir',21,'2024-05-20 01:41:37','2024-05-20 02:41:37'),('agadir',22,'2024-05-20 01:41:59','2024-05-20 02:41:59'),('agadir',23,'2024-05-20 01:42:34','2024-05-20 02:42:34'),('agadir',24,'2024-05-20 01:42:59','2024-05-20 02:43:00'),('agadir',25,'2024-05-20 01:43:16','2024-05-20 02:43:16'),('agadir',26,'2024-05-20 01:43:49','2024-05-20 02:43:49'),('agadir',27,'2024-05-20 01:44:40','2024-05-20 02:44:41'),('agadir',28,'2024-05-20 01:47:09','2024-05-20 02:47:09'),('agadir',29,'2024-05-20 01:57:42','2024-05-20 02:57:42'),('agadir',30,'2024-05-20 01:58:20','2024-05-20 02:58:21'),('agadir',31,'2024-05-20 02:18:36','2024-05-20 03:18:36'),('agadir',32,'2024-05-20 02:19:43','2024-05-20 03:19:43'),('agadir',33,'2024-05-20 02:20:15','2024-05-20 03:20:15'),('agadir',34,'2024-05-20 02:20:40','2024-05-20 03:20:40'),('agadir',35,'2024-05-20 02:21:19','2024-05-20 03:21:19'),('agadir',36,'2024-05-20 02:22:04','2024-05-20 03:22:05'),('agadir',37,'2024-05-20 02:26:24','2024-05-20 03:26:24'),('agadir',38,'2024-05-20 02:27:23','2024-05-20 03:27:23'),('agadir',39,'2024-05-20 02:28:48','2024-05-20 03:28:48'),('agadir',40,'2024-05-20 02:29:42','2024-05-20 03:29:42'),('agadir',41,'2024-05-20 02:29:53','2024-05-20 03:29:54'),('agadir',42,'2024-05-20 02:31:23','2024-05-20 03:31:23'),('agadir',43,'2024-05-20 02:32:55','2024-05-20 03:32:55'),('agadir',44,'2024-05-20 02:33:04','2024-05-20 03:33:04'),('agadir',45,'2024-05-20 02:43:32','2024-05-20 03:43:33'),('agadir',46,'2024-05-20 02:45:20','2024-05-20 03:45:20'),('agadir',47,'2024-05-20 02:45:49','2024-05-20 03:45:49'),('agadir',48,'2024-05-20 02:46:13','2024-05-20 03:46:13'),('agadir',49,'2024-05-20 03:02:08','2024-05-20 04:02:08'),('agadir',50,'2024-05-20 03:03:00','2024-05-20 04:03:00'),('agadir',51,'2024-05-20 03:03:26','2024-05-20 04:03:26'),('agadir',52,'2024-05-20 03:05:29','2024-05-20 04:05:29'),('agadir',53,'2024-05-20 03:05:50','2024-05-20 04:05:50'),('agadir',54,'2024-05-20 03:06:05','2024-05-20 04:06:05'),('agadir',55,'2024-05-20 03:06:14','2024-05-20 04:06:14'),('agadir',56,'2024-05-20 03:26:57','2024-05-20 04:26:57'),('agadir',57,'2024-05-20 03:28:16','2024-05-20 04:28:16'),('agadir',58,'2024-05-20 03:28:43','2024-05-20 04:28:43'),('agadir',59,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `company` varchar(128) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,8,NULL,'2024-05-20 02:46:13','2024-05-20 03:46:13'),(2,9,NULL,'2024-05-20 03:02:08','2024-05-20 04:02:08'),(3,10,NULL,'2024-05-20 03:03:00','2024-05-20 04:03:00'),(4,11,NULL,'2024-05-20 03:03:26','2024-05-20 04:03:26'),(5,12,NULL,'2024-05-20 03:05:29','2024-05-20 04:05:29'),(6,13,NULL,'2024-05-20 03:05:50','2024-05-20 04:05:50'),(7,14,NULL,'2024-05-20 03:06:05','2024-05-20 04:06:05'),(8,15,NULL,'2024-05-20 03:06:14','2024-05-20 04:06:14'),(9,16,NULL,'2024-05-20 03:26:57','2024-05-20 04:26:57'),(10,17,NULL,'2024-05-20 03:28:16','2024-05-20 04:28:16'),(11,18,NULL,'2024-05-20 03:28:43','2024-05-20 04:28:43'),(12,19,NULL,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drivers`
--

DROP TABLE IF EXISTS `drivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drivers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `vehicle_id` int NOT NULL,
  `current_location_id` int NOT NULL,
  `license_num` varchar(128) DEFAULT NULL,
  `status` enum('enroute','inactive','available') DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `vehicle_id` (`vehicle_id`),
  KEY `current_location_id` (`current_location_id`),
  CONSTRAINT `drivers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `drivers_ibfk_2` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`id`),
  CONSTRAINT `drivers_ibfk_3` FOREIGN KEY (`current_location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drivers`
--

LOCK TABLES `drivers` WRITE;
/*!40000 ALTER TABLE `drivers` DISABLE KEYS */;
INSERT INTO `drivers` VALUES (1,19,7,47,NULL,NULL,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `drivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `img_path` varchar(300) DEFAULT NULL,
  `img_url` varchar(300) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 01:58:20','2024-05-20 02:58:21'),(2,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:18:36','2024-05-20 03:18:36'),(3,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:20:15','2024-05-20 03:20:16'),(4,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:20:40','2024-05-20 03:20:41'),(5,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:21:19','2024-05-20 03:21:19'),(6,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:22:04','2024-05-20 03:22:05'),(7,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:26:24','2024-05-20 03:26:24'),(8,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:27:23','2024-05-20 03:27:23'),(9,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:28:48','2024-05-20 03:28:48'),(10,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:29:42','2024-05-20 03:29:42'),(11,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:29:53','2024-05-20 03:29:54'),(12,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:31:23','2024-05-20 03:31:23'),(13,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:32:55','2024-05-20 03:32:55'),(14,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:33:04','2024-05-20 03:33:04'),(15,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:43:32','2024-05-20 03:43:33'),(16,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:45:20','2024-05-20 03:45:20'),(17,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:45:49','2024-05-20 03:45:49'),(18,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 02:46:13','2024-05-20 03:46:13'),(19,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:02:08','2024-05-20 04:02:08'),(20,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:03:00','2024-05-20 04:03:00'),(21,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:03:26','2024-05-20 04:03:26'),(22,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:05:29','2024-05-20 04:05:29'),(23,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:05:50','2024-05-20 04:05:50'),(24,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:06:05','2024-05-20 04:06:05'),(25,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:06:14','2024-05-20 04:06:14'),(26,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:26:57','2024-05-20 04:26:57'),(27,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:28:16','2024-05-20 04:28:16'),(28,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:28:43','2024-05-20 04:28:43'),(29,'/tmp/images/cat.png','https://files.com/marara5','2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `name` varchar(128) NOT NULL,
  `city_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES ('amzil',12,1,'2024-05-20 01:27:08','2024-05-20 02:27:08'),('amzil',13,2,'2024-05-20 01:27:21','2024-05-20 02:27:21'),('amzil',2,4,'2024-05-20 01:28:44','2024-05-20 02:28:44'),('amzil',2,5,'2024-05-20 01:28:50','2024-05-20 02:28:50'),('amzil',2,6,'2024-05-20 01:28:51','2024-05-20 02:28:51'),('amzil',2,7,'2024-05-20 01:28:52','2024-05-20 02:28:52'),('amzil',2,8,'2024-05-20 01:37:38','2024-05-20 02:37:38'),('amzil',2,9,'2024-05-20 01:40:20','2024-05-20 02:40:20'),('amzil',2,10,'2024-05-20 01:41:37','2024-05-20 02:41:37'),('amzil',2,11,'2024-05-20 01:41:59','2024-05-20 02:41:59'),('amzil',2,12,'2024-05-20 01:42:34','2024-05-20 02:42:34'),('amzil',2,13,'2024-05-20 01:42:59','2024-05-20 02:43:00'),('amzil',2,14,'2024-05-20 01:43:16','2024-05-20 02:43:16'),('amzil',2,15,'2024-05-20 01:43:49','2024-05-20 02:43:49'),('amzil',2,16,'2024-05-20 01:44:40','2024-05-20 02:44:41'),('amzil',2,17,'2024-05-20 01:47:09','2024-05-20 02:47:09'),('amzil',2,18,'2024-05-20 01:57:42','2024-05-20 02:57:42'),('amzil',2,19,'2024-05-20 01:58:20','2024-05-20 02:58:21'),('amzil',2,20,'2024-05-20 02:18:36','2024-05-20 03:18:36'),('amzil',2,21,'2024-05-20 02:20:15','2024-05-20 03:20:16'),('amzil',2,22,'2024-05-20 02:20:40','2024-05-20 03:20:40'),('amzil',35,23,'2024-05-20 02:21:19','2024-05-20 03:21:19'),('amzil',36,24,'2024-05-20 02:22:04','2024-05-20 03:22:05'),('amzil',37,25,'2024-05-20 02:26:24','2024-05-20 03:26:24'),('amzil',38,26,'2024-05-20 02:27:23','2024-05-20 03:27:23'),('amzil',39,27,'2024-05-20 02:28:48','2024-05-20 03:28:48'),('amzil',40,28,'2024-05-20 02:29:42','2024-05-20 03:29:42'),('amzil',41,29,'2024-05-20 02:29:53','2024-05-20 03:29:54'),('amzil',42,30,'2024-05-20 02:31:23','2024-05-20 03:31:23'),('amzil',43,31,'2024-05-20 02:32:55','2024-05-20 03:32:55'),('amzil',44,32,'2024-05-20 02:33:04','2024-05-20 03:33:04'),('amzil',45,33,'2024-05-20 02:43:32','2024-05-20 03:43:33'),('amzil',46,34,'2024-05-20 02:45:20','2024-05-20 03:45:20'),('amzil',47,35,'2024-05-20 02:45:49','2024-05-20 03:45:49'),('amzil',48,36,'2024-05-20 02:46:13','2024-05-20 03:46:13'),('amzil',49,37,'2024-05-20 03:02:08','2024-05-20 04:02:08'),('amzil',50,38,'2024-05-20 03:03:00','2024-05-20 04:03:00'),('amzil',51,39,'2024-05-20 03:03:26','2024-05-20 04:03:26'),('amzil',52,40,'2024-05-20 03:05:29','2024-05-20 04:05:29'),('amzil',53,41,'2024-05-20 03:05:50','2024-05-20 04:05:50'),('amzil',54,42,'2024-05-20 03:06:05','2024-05-20 04:06:05'),('amzil',55,43,'2024-05-20 03:06:14','2024-05-20 04:06:14'),('amzil',56,44,'2024-05-20 03:26:57','2024-05-20 04:26:57'),('amzil',57,45,'2024-05-20 03:28:16','2024-05-20 04:28:16'),('amzil',58,46,'2024-05-20 03:28:43','2024-05-20 04:28:43'),('amzil',59,47,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `img_id` int DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `img_id` (`img_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`img_id`) REFERENCES `images` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'king@thewarroot.tech','08f8a5b7dfc310ac8ffccb95727e8a68',NULL,NULL,NULL,NULL,NULL,'2024-05-20 02:28:48','2024-05-20 03:28:48'),(2,'king@thewarroot.tech','08f8a5b7dfc310ac8ffccb95727e8a68',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:31:23','2024-05-20 03:31:23'),(3,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:32:55','2024-05-20 03:32:55'),(4,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:33:04','2024-05-20 03:33:04'),(5,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:43:32','2024-05-20 03:43:33'),(6,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:45:20','2024-05-20 03:45:20'),(7,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:45:49','2024-05-20 03:45:50'),(8,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 02:46:13','2024-05-20 03:46:13'),(9,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:02:08','2024-05-20 04:02:08'),(10,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:03:00','2024-05-20 04:03:00'),(11,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:03:26','2024-05-20 04:03:26'),(12,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:05:29','2024-05-20 04:05:29'),(13,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:05:50','2024-05-20 04:05:50'),(14,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:06:05','2024-05-20 04:06:05'),(15,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:06:14','2024-05-20 04:06:14'),(16,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:26:57','2024-05-20 04:26:57'),(17,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:28:16','2024-05-20 04:28:16'),(18,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:28:43','2024-05-20 04:28:43'),(19,'king@thewarroot.tech','9e106d4dac5674f04aebc8f4de3a9f45',NULL,NULL,NULL,'2024-05-20',NULL,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `model` varchar(300) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  CONSTRAINT `vehicles_chk_1` CHECK (((`year` >= 1900) and (`year` <= 2100)))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES (1,NULL,2004,NULL,'2024-05-20 03:03:26','2024-05-20 04:03:26'),(2,NULL,2100,NULL,'2024-05-20 03:06:05','2024-05-20 04:06:06'),(3,NULL,2100,NULL,'2024-05-20 03:06:14','2024-05-20 04:06:14'),(4,NULL,2100,NULL,'2024-05-20 03:26:57','2024-05-20 04:26:57'),(5,NULL,2100,NULL,'2024-05-20 03:28:16','2024-05-20 04:28:16'),(6,NULL,2100,NULL,'2024-05-20 03:28:43','2024-05-20 04:28:43'),(7,NULL,2100,NULL,'2024-05-20 03:29:16','2024-05-20 04:29:16');
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-20  4:31:18
