create database bancoLed;

use bancoLed;

create table tbl_led(
id         int NOT NULL auto_increment primary key,
nome       varchar(150),
colorLed   varchar(50),
dataLigado datetime
);