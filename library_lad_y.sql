SHOW DATABASES;

USE librarylady;

SHOW TABLES;
SELECT * FROM genre;
SHOW PROCEDURE STATUS WHERE Db = 'librarylady';

CALL book_has_genre('Mystery');

CALL book_has_genre('Technology');

CALL book_has_genre('Technology');

CALL book_has_genre('Accounting');

SELECT * FROM book_genre WHERE genre = 'Accounting';


DELIMITER $$

DROP PROCEDURE IF EXISTS book_has_genre;
CREATE PROCEDURE book_has_genre(IN genre_p VARCHAR(30))
BEGIN
    DECLARE genre_exists INT;

    SELECT COUNT(*) INTO genre_exists
    FROM genre
    WHERE LOWER(name) = LOWER(genre_p);

    IF genre_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid genre provided. This genre does not exist';
    ELSE
        SELECT DISTINCT
            b.isbn AS book_id,
            b.title AS title,
            COALESCE(a.name, 'Unknown Author') AS author,
            b.page_count,
            b.publisher_name
        FROM book b
        JOIN book_genre bg ON b.isbn = bg.isbn
        LEFT JOIN book_author ba ON b.isbn = ba.isbn
        LEFT JOIN author a ON ba.author = a.name
        WHERE LOWER(bg.genre) = LOWER(genre_p);
    END IF;
END $$

DELIMITER ;

CALL book_has_genre('Accounting');

SELECT * FROM book WHERE isbn IN ('9780749460211', '9780814416259', '9781601638618');