drop user if exists 'exelFlask'@'%';
flush privileges;
create user if not exists 'exelFlask'@'%' identified by 'exelFlask';
create database if not exists exelFlask character set utf8 collate utf8_unicode_ci;
grant all on exelFlask.* to 'exelFlask'@'%';
flush privileges;

use exelFlask;


drop table if exists invoice;
create table if not exists invoice(
	id int(11) not null primary key auto_increment,
	custommerID varchar(30) not null default '',
	name varchar(30) not null default '',
	email varchar(30) not null default '',
	phone varchar(30) not null default '',
	address varchar(30) not null default '',
	remarks varchar(30) not null default '',
	taxRate varchar(30) not null default '',
	category varchar(100) not null default '',
	insert_date timestamp default current_timestamp

);
drop table if exists products;
create table if not exists products(
	id int(11) not null primary key auto_increment,
	invoiceID int(11) not null default 0 comment 'id in envoice',
	productID varchar(100) not null default '',
	description varchar(255) not null default '',
	sellingPrice decimal(10,2) not null default 0.00,
	um varchar(30) not null default '',
	taxType varchar(30) not null default '',
	quantity tinyint(5) not null default 0,
	key invoiceID(invoiceID)
);





