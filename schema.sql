
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username varchar(20) NOT NULL UNIQUE,
  pwd varchar(255) NOT NULL,
  city varchar(50) NOT NULL,
  email varchar(30) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS book(
  book_id VARCHAR(500) PRIMARY key,
  book_name VARCHAR(500) NOT NULL,
  author_name VARCHAR(500) NOT NULL,
  image_url VARCHAR(500) NOT NULL
);
CREATE TABLE IF NOT EXISTS library(
  user_id SERIAL,
  book_id VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS requests(
  id SERIAL PRIMARY KEY,
  requester_id SERIAL REFERENCES users(id),
  requested_id SERIAL REFERENCES users(id),
  book_id1 VARCHAR(500) REFERENCES book(book_id) NOT NULL,
  book_id2 VARCHAR(500) REFERENCES book(book_id)
);
CREATE TABLE IF NOT EXISTS trade_status(
  id SERIAL REFERENCES requests(id),
  stat VARCHAR(20) NOT NULL
);