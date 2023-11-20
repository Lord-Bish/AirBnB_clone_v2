-- Preparses a MySQL server with DB hbnb_dev_db & user hbnb_dev in localhost
-- Password should be hbnb_dev_pwd. hbnb_dev should have all+SELECT privileges
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
