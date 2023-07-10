show databases;

use mujiclo_db;

SHOW TABLES;

select * from mujiclo_user_info;
select * from mujiclo_blog_list;

DROP TABLE mujiclo_user_info;

-- User 테이블 생성 --
CREATE TABLE mujiclo_user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL UNIQUE,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);

-- Board 테이블 생성 --
CREATE TABLE mujiclo_board_list (
    post_number INT NOT NULL AUTO_INCREMENT,
    post_title VARCHAR(255),
    post_content TEXT,
    author VARCHAR(100),
    PRIMARY KEY (post_number),
    FOREIGN KEY (author) REFERENCES mujiclo_user_info(USER_EMAIL)
);
