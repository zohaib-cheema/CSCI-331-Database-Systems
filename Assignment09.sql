/* Drop schema books */
DROP SCHEMA IF EXISTS books;

/* Create schema books */
CREATE SCHEMA books;

/* Make it the default */
USE books;

/* Drop any tables */
DROP TABLE IF EXISTS ONF_book;

/* Creating a 0NF Table */
CREATE TABLE ONF_book(
  book_title VARCHAR(255),
  author VARCHAR(255),
  author_nationality VARCHAR(100),
  book_format VARCHAR(50),
  price DECIMAL(10,2),
  book_subject VARCHAR(255),          /* multi-valued list */
  pages INT,
  thickness VARCHAR(50),
  publisher VARCHAR(255),
  publisher_country VARCHAR(100),
  genre_id INT,
  genre_name VARCHAR(255),
  PRIMARY KEY (book_title, book_format)
);

/* Insert into 0NF table */
INSERT INTO ONF_book
(book_title, author, author_nationality, book_format, price, book_subject, pages, thickness, publisher, publisher_country, genre_id, genre_name)
VALUES
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 'American', 'Hardcover', 49.99, 'MySQL, Database, Design', 520, 'Thick', 'Apress', 'USA', 1, 'Tutorial'),
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 'American', 'E-book', 22.34, 'MySQL, Database, Design', 520, 'Thick', 'Apress', 'USA', 1, 'Tutorial'),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 'British', 'E-book', 13.88, NULL, 538, 'Thick', 'Addison-Wesley', 'USA', 2, 'Popular science'),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 'British', 'Paperback', 39.99, NULL, 538, 'Thick', 'Addison-Wesley', 'USA', 2, 'Popular science');

/* Select from the tables */
SELECT * FROM ONF_book;


/* Drop any tables */
DROP TABLE IF EXISTS NF1_book_subject;
DROP TABLE IF EXISTS NF1_book;

/* Creating a 1NF Book table */
CREATE TABLE NF1_book(
  book_title VARCHAR(255),
  author VARCHAR(255),
  author_nationality VARCHAR(100),
  book_format VARCHAR(50),
  price DECIMAL(10,2),
  pages INT,
  thickness VARCHAR(50),
  publisher VARCHAR(255),
  publisher_country VARCHAR(100),
  genre_id INT,
  genre_name VARCHAR(255),
  PRIMARY KEY (book_title, book_format)
);

/* Creating a 1NF Book-Subject table */
CREATE TABLE NF1_book_subject(
  book_title VARCHAR(255),
  subject_name VARCHAR(255),
  PRIMARY KEY (book_title, subject_name)
);

/* Insert into 1NF book table */
INSERT INTO NF1_book
(book_title, author, author_nationality, book_format, price, pages, thickness, publisher, publisher_country, genre_id, genre_name)
VALUES
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 'American', 'Hardcover', 49.99, 520, 'Thick', 'Apress', 'USA', 1, 'Tutorial'),
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 'American', 'E-book', 22.34, 520, 'Thick', 'Apress', 'USA', 1, 'Tutorial'),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 'British', 'E-book', 13.88, 538, 'Thick', 'Addison-Wesley', 'USA', 2, 'Popular science'),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 'British', 'Paperback', 39.99, 538, 'Thick', 'Addison-Wesley', 'USA', 2, 'Popular science');

/* Insert subjects as atomic rows */
INSERT INTO NF1_book_subject (book_title, subject_name)
VALUES
('Beginning MySQL Database Design and Optimization', 'MySQL'),
('Beginning MySQL Database Design and Optimization', 'Database'),
('Beginning MySQL Database Design and Optimization', 'Design');

/* Select from the tables */
SELECT * FROM NF1_book;
SELECT * FROM NF1_book_subject;


/* Drop any tables */
DROP TABLE IF EXISTS NF2_price;
DROP TABLE IF EXISTS NF2_book;

/* Creating a 2NF Book table */
CREATE TABLE NF2_book(
  book_title VARCHAR(255) PRIMARY KEY,
  author VARCHAR(255),
  author_nationality VARCHAR(100),
  pages INT,
  thickness VARCHAR(50),
  publisher VARCHAR(255),
  publisher_country VARCHAR(100),
  genre_id INT,
  genre_name VARCHAR(255)
);

/* Creating a 2NF Price table */
CREATE TABLE NF2_price(
  book_title VARCHAR(255),
  book_format VARCHAR(50),
  price DECIMAL(10,2),
  PRIMARY KEY (book_title, book_format)
);

/* Insert into 2NF book table */
INSERT INTO NF2_book
(book_title, author, author_nationality, pages, thickness, publisher, publisher_country, genre_id, genre_name)
VALUES
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 'American', 520, 'Thick', 'Apress', 'USA', 1, 'Tutorial'),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 'British', 538, 'Thick', 'Addison-Wesley', 'USA', 2, 'Popular science');

/* Insert into 2NF price table */
INSERT INTO NF2_price
(book_title, book_format, price)
VALUES
('Beginning MySQL Database Design and Optimization', 'Hardcover', 49.99),
('Beginning MySQL Database Design and Optimization', 'E-book', 22.34),
('The Relational Model for Database Management: Version 2', 'E-book', 13.88),
('The Relational Model for Database Management: Version 2', 'Paperback', 39.99);

/* Select from the tables */
SELECT * FROM NF2_book;
SELECT * FROM NF2_price;


/* Drop any tables (children first) */
DROP TABLE IF EXISTS NF3_price;
DROP TABLE IF EXISTS NF3_book;
DROP TABLE IF EXISTS NF3_genre;
DROP TABLE IF EXISTS NF3_publisher;
DROP TABLE IF EXISTS NF3_author;

/* Creating 3NF Author table */
CREATE TABLE NF3_author(
  author VARCHAR(255) PRIMARY KEY,
  nationality VARCHAR(100)
);

/* Creating 3NF Publisher table */
CREATE TABLE NF3_publisher(
  publisher VARCHAR(255) PRIMARY KEY,
  country VARCHAR(100)
);

/* Creating 3NF Genre table */
CREATE TABLE NF3_genre(
  genre_id INT PRIMARY KEY,
  name VARCHAR(255)
);

/* Creating 3NF Book table */
CREATE TABLE NF3_book(
  book_title VARCHAR(255) PRIMARY KEY,
  author VARCHAR(255),
  pages INT,
  thickness VARCHAR(50),
  publisher VARCHAR(255),
  genre_id INT,
  FOREIGN KEY (author) REFERENCES NF3_author(author),
  FOREIGN KEY (publisher) REFERENCES NF3_publisher(publisher),
  FOREIGN KEY (genre_id) REFERENCES NF3_genre(genre_id)
);

/* Creating 3NF Price table */
CREATE TABLE NF3_price(
  book_title VARCHAR(255),
  book_format VARCHAR(50),
  price DECIMAL(10,2),
  PRIMARY KEY (book_title, book_format),
  FOREIGN KEY (book_title) REFERENCES NF3_book(book_title)
);

/* Insert into 3NF tables */
INSERT INTO NF3_author (author, nationality) VALUES
('Chad Russell', 'American'),
('E.F.Codd', 'British');

INSERT INTO NF3_publisher (publisher, country) VALUES
('Apress', 'USA'),
('Addison-Wesley', 'USA');

INSERT INTO NF3_genre (genre_id, name) VALUES
(1, 'Tutorial'),
(2, 'Popular science');

INSERT INTO NF3_book (book_title, author, pages, thickness, publisher, genre_id) VALUES
('Beginning MySQL Database Design and Optimization', 'Chad Russell', 520, 'Thick', 'Apress', 1),
('The Relational Model for Database Management: Version 2', 'E.F.Codd', 538, 'Thick', 'Addison-Wesley', 2);

INSERT INTO NF3_price (book_title, book_format, price) VALUES
('Beginning MySQL Database Design and Optimization', 'Hardcover', 49.99),
('Beginning MySQL Database Design and Optimization', 'E-book', 22.34),
('The Relational Model for Database Management: Version 2', 'E-book', 13.88),
('The Relational Model for Database Management: Version 2', 'Paperback', 39.99);

/* Select from the tables */
SELECT * FROM NF3_author;
SELECT * FROM NF3_publisher;
SELECT * FROM NF3_genre;
SELECT * FROM NF3_book;
SELECT * FROM NF3_price;

/* Create a view of everything*/
CREATE OR REPLACE VIEW v_everything AS
SELECT
  b.book_title,
  b.author,
  a.nationality AS author_nationality,
  b.pages,
  b.thickness,
  b.publisher,
  p.country AS publisher_country,
  b.genre_id,
  g.name AS genre_name,
  pr.book_format,
  pr.price
FROM NF3_book b
JOIN NF3_author a
  ON b.author = a.author
JOIN NF3_publisher p
  ON b.publisher = p.publisher
JOIN NF3_genre g
  ON b.genre_id = g.genre_id
JOIN NF3_price pr
  ON b.book_title = pr.book_title;

SELECT * FROM v_everything;