DROP DATABASE IF EXISTS mutation;
CREATE DATABASE mutation CHARACTER SET utf8mb4;
USE mutation;

CREATE TABLE dna(
    id_dna INT AUTO_INCREMENT PRIMARY KEY,
    name_dna VARCHAR(120) NOT NULL,
    chain_dna VARCHAR(250) UNIQUE NOT NULL,
    mutation_dna ENUM("True","False") NOT NULL default "True"
);