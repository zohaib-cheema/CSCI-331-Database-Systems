/*Use meta database*/
USE meta;

/*Drop backup table if it exists*/
DROP TABLE IF EXISTS meta.backup;

/*[1] Create backup table in meta database*/
CREATE TABLE backup (
    backup_id INT AUTO_INCREMENT PRIMARY KEY,
    db VARCHAR(20) NOT NULL,
    relation VARCHAR(30) NOT NULL,
    `rows` INT NOT NULL,
    cols INT NOT NULL,
    csv_length INT NOT NULL,
    xml_length INT NOT NULL,
    json_length INT NOT NULL,
    csv_data MEDIUMTEXT NOT NULL,
    xml_data MEDIUMTEXT NOT NULL,
    json_data JSON NOT NULL,
    saved_dtm TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

/*Retrieve everything from the backup table*/
SELECT * FROM meta.backup;

/*[7a] Create a view v_table_backups that has a list of backups without the actual csv_data, xml_data, and json_data*/
CREATE OR REPLACE VIEW v_table_backups AS (
    SELECT backup_id, db, relation, `rows`, cols, csv_length, xml_length, json_length, saved_dtm
    FROM meta.backup
);

/*[7b] Retrieve summary of backups from the view*/
SELECT * FROM meta.v_table_backups;
