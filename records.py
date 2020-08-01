from flask import Flask,render_template,request,redirect,url_for
import pymysql

CREATE TABLE `code-a-thon`.`records` ( `code` INT(11) NOT NULL , `name` VARCHAR(255) NOT NULL , `open` BIGINT(30) NOT NULL , `high` BIGINT(30) NOT NULL , `low` BIGINT( 30) NOT NULL , `close` BIGINT(30) NOT NULL , PRIMARY KEY (`code`)) ENGINE = InnoDB;
SELECT * FROM `records`