drop database if exists eagle;
create database eagle charset=utf8;

use eagle
create table `user` (
    `id` int(11) not null auto_increment,
    `username` varchar(128) not null default '' comment 'username',
    `password` varchar(128) not null default '' comment 'password',
    `email` varchar(128) not null default '' comment 'email',
    `salt` varchar(128) not null default '' comment 'salt',
    `create_time` datetime not null default '0000-00-00 00:00' comment 'create_time',
    `update_time` datetime not null default '0000-00-00 00:00' comment 'update_time',
    `is_deleted` tinyint(3) not null default '0' comment '1:deleted',
    primary key (`id`),
    key `idx_email` (`email`),
    key `idx_is_deleted` (`is_deleted`)
)engine=InnoDB DEFAULT CHARSET=utf8 comment 'user';

create table `image` (
    `id` int(11) not null auto_increment,
    `hashcode` varchar(128) not null default '' comment 'image hashcode',
    `description` varchar(512) not null default '' comment 'image description',
    `create_time` datetime not null default '0000-00-00 00:00' comment 'create_time',
    `update_time` datetime not null default '0000-00-00 00:00' comment 'update_time',
    `is_deleted` tinyint(3) not null default '0' comment '1:deleted',
    primary key (`id`),
    key `idx_hash` (`hashcode`),
    key `idx_is_deleted` (`is_deleted`)
)engine=InnoDB DEFAULT CHARSET=utf8 comment 'image';

create table `instance` (
    `id` int(11) not null auto_increment,
    `image_id` int(11) not null default '0' comment 'image id fk of image',
    `user_id` int(11) not null default '0' comment 'user id fk of user',
    `container_serial` varchar(128) not null default '' comment 'container serial',
    `status` tinyint(3) not null default '0' comment '0:running 1:stop 2:unknown',
    `create_time` datetime not null default '0000-00-00 00:00' comment 'create_time',
    `update_time` datetime not null default '0000-00-00 00:00' comment 'update_time',
    `is_deleted` tinyint(3) not null default '0' comment '1:deleted',
    primary key (`id`),
    key `idx_container_serial` (`container_serial`),
    key `idx_is_deleted` (`is_deleted`)
)engine=InnoDB DEFAULT CHARSET=utf8 comment 'instance';