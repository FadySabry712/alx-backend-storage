-- Creates a table users with below attributes
-- id, integer
-- email
-- name
-- If table exists, script will not fail

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
