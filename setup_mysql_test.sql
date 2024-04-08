-- Prepare a MySQL server
-- Create a database hbnb_test_db:
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user hbnb_test (in localhost) with the password be set to hbnb_test_pwd:
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Set all privileges on the database hbnb_test_db for hbnb_test:
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Set SELECT privilege on the database performance_schema for hbnb_test:
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
