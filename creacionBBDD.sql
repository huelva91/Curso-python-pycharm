CREATE TABLE `curso_python`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `precio` INT NULL,
  `fecha_registro` DATETIME NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `curso_python`.`persona` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


persona

id ai
nombre 
apellido 
email

insertar 3 personas

consultas
1. obtener solo los nombre de las personas de todas
2. Sacar informacion de las personas que tengan un email terminado en @gmail.com
3. Actualizar a las personas que no tengan un @gmail.com a @gmail.com


INSERT INTO persona(id, nombre, apellido, email) VALUES(1, "Ana", "Gomez", "email1@gmail.com")

DELETE FROM `curso_python`.`persona` WHERE (`id` = '1');

UPDATE `persona` SET `email` = 'email2@gmail.com' WHERE (`id` = '2');

