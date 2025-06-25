-- Transform a DB and table to UTF-8 format
-- Select the correct DataBase
USE hbtn_0c_0;

-- DataBase transformation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Table transformation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;