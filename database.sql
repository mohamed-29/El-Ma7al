CREATE DATABASE mobile_shop;
USE mobile_shop;

CREATE TABLE ids (
	id VARCHAR(255) PRIMARY KEY,
	num INt NOT NULL DEFAULT 1
);

CREATE TABLE mobile_devices (
   serial_id VARCHAR(255) PRIMARY KEY,
   brand VARCHAR(255) NOT NULL,
   model VARCHAR(255) NOT NULL,
   battary INT NOT NULL,
   gb INT NOT NULL,
   ram INT NOT NULL,
   color VARCHAR(125) NOT NULL,
   price_in INt NOT NULL,
   is_used BOOL NOT NULL,
   price_out INT NOT NULL,
   release_date DATETIME NOT NULL,
   FOREIGN KEY(serial_id) REFERENCES ids(id)
);

CREATE TABLE accessories (
   acc_id VARCHAR(255) PRIMARY KEY,
   acc_name VARCHAR(255) NOT NULL,
   brand VARCHAR(255) NOT NULL,
   kind VARCHAR(255) NOT NULL,
   color VARCHAR(125) NOT NULL,
   price_in INT NOT NULL,
   price_out INT NOT NULL,
   release_date DATETIME NOT NULL,
   FOREIGN KEY(acc_id) REFERENCES ids(id)
);

CREATE TABLE receipt (
   rec_id INT NOT NULL,
   pro_id VARCHAR(255) NOT NULL,
   cos_name VARCHAR(255),
   cos_num VARCHAR(15),
   price_in INT NOT NULL,
   profit INT NOT NULL,
   num INT NOT NULL,
   release_date DATETIME NOT NULL,
   primary key(rec_id,pro_id),
   FOREIGN KEY(pro_id) REFERENCES ids(id)
);

CREATE TABLE cost (
	c_id INT NOT NULL,
	c_name VARCHAR(510) NOT NULL,
    much INT NOT NULL,
    release_date DATETIME NOT NULL,
    primary key(c_id)
);

CREATE TABLE returned(
	rec_id INT NOT NULL,
	pro_id VARCHAR(255) NOT NULL,
    cos_name VARCHAR(255),
    cos_num VARCHAR(15),
    price_in INT NOT NULL,
    profit INT NOT NULL,
    num INT NOT NULL,
    note VARCHAR(510),
    release_date DATETIME NOT NULL,
    primary key(rec_id,pro_id)
);
