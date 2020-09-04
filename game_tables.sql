CREATE DATABASE db_pygame

CREATE TABLE tbl_user(
    user_id INT AUTO_INCREMENT,
    username VARCHAR(100) unique,
    password VARCHAR(200),
    full_name VARCHAR(200),
    gender VARCHAR(200),
    PRIMARY KEY(user_id)
);


CREATE TABLE tbl_score(
    score_id INT AUTO_INCREMENT,
    fk_user_id INT,
    score INT,
    game_day_time TIMESTAMP,
    PRIMARY KEY(score_id),
    FOREIGN KEY (fk_user_id) REFERENCES tbl_user(user_id)
);
