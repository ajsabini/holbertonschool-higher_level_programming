-- script that creates the database hbtn_0d_2 an user user_0d_2
CREATE DATABASE if not exists hbtn_0d_2;
CREATE USER if not exists user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`;
GRANT SELECT ON `hbtn_0s_2`.* TO `user_0d_2`@`localhost`;
FLUSH PRIVILEGES;
