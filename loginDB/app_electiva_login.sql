CREATE DATABASE IF NOT EXISTS app_electiva_login;
USE app_electiva_login;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id int NOT NULL AUTO_INCREMENT,
  username varchar(50) NOT NULL,
  password varchar(255) NOT NULL,
  rol varchar(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES users WRITE;
INSERT INTO users VALUES (1000,'test','$2b$12$TfoVbED2upULpgSfwEDNf.0XywK0E0kEZpa6yGAOUL4HyOH7.q48a','test');
UNLOCK TABLES;