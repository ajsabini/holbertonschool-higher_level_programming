-- script that creates the database hbtn_0d_2 an user user_0d_2
CREATE DATABASE if not exists hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER if not exists 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'
GRANT SELECT ON * TO 'user_0d_2'@'localhost';
