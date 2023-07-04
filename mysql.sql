show databases;

use blog_db;

SHOW TABLES;

select * from user_info;
select * from blog_list;

-- 사용자 테이블 --
CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);

DROP TABLE user_info;

CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL UNIQUE,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);

CREATE TABLE blog_list (
    post_number INT NOT NULL AUTO_INCREMENT,
    post_title VARCHAR(255),
    post_content TEXT,
    author VARCHAR(100),
    PRIMARY KEY (post_number),
    FOREIGN KEY (author) REFERENCES user_info(USER_EMAIL)
);
