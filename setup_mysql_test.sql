-- Prepares MySQL serve, DB hnbn_test_db, user hbnb_test in localhost
-- Password should be hbnb_test_pwd, hbnb_test must have SELECT+all privileges
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL ON hbnb_test_db.* TO 'hnbn_test'@'localhost';
