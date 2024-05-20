CREATE TABLE `user` (
	`id`	int	NOT NULL,
	`nick_name`	varchar(20)	NOT NULL,
	`password`	varchar(20)	NOT NULL,
	`phone_num`	varchar(15)	NOT NULL
);

CREATE TABLE `Untitled` (
	`content_id`	bigint	NOT NULL,
	`user_id`	int	NOT NULL,
	`blog_title`	varchar(30)	NOT NULL,
	`blog_content`	varchar(300)	NULL,
	`created_date`	timestamp	NOT NULL,
	`updated_date`	timestamp	NOT NULL,
	`likes`	bigint	NOT NULL,
	`kind`	varchar(10)	NOT NULL,
	`img`	varchar(500)	NULL
);

CREATE TABLE `Untitled2` (
	`pet_id`	VARCHAR(255)	NOT NULL,
	`content_id`	bigint	NOT NULL,
	`user_id`	int	NOT NULL,
	`pet_name`	varchar(30)	NOT NULL,
	`pet_type`	varchar(30)	NOT NULL,
	`sex`	boolean	NOT NULL,
	`img`	varchar(300)	NOT NULL
);

CREATE TABLE `Untitled3` (
	`x_val`	float	NOT NULL,
	`y_val`	float	NOT NULL,
	`place_name`	varchar(30)	NOT NULL,
	`category`	varchar(10)	NOT NULL
);

ALTER TABLE `user` ADD CONSTRAINT `PK_USER` PRIMARY KEY (
	`id`
);

ALTER TABLE `Untitled` ADD CONSTRAINT `PK_UNTITLED` PRIMARY KEY (
	`content_id`
);

ALTER TABLE `Untitled2` ADD CONSTRAINT `PK_UNTITLED2` PRIMARY KEY (
	`pet_id`
);

