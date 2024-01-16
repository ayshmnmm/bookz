CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username varchar(20) NOT NULL UNIQUE,
  pwd varchar(255) NOT NULL,
  city varchar(50) NOT NULL,
  email varchar(30) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);