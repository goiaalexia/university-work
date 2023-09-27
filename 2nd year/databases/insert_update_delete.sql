-- insert data – for at least 4 tables; at least one statement must violate referential integrity constraints;
-- update data – for at least 3 tables;
-- delete data – for at least 2 tables.

USE GenshinManager
GO


INSERT INTO Boss VALUES ('Jadeplume Terrorshroom', 'Mint', 'Vajrada Emerald')
INSERT INTO Boss VALUES ('Hydro Hypostasis', 'Vajrada Sapphire', 'Teardrop')

INSERT INTO Material VALUES ('Mint', 100, 'Jadeplume Terrorshroom')
INSERT INTO Material VALUES ('Vajrada Emerald', 100, 'Jadeplume Terrorshroom')
INSERT INTO Material VALUES ('Teardrop', 100, 'Hydro Hypostasis')
INSERT INTO Material VALUES ('Vajrada Sapphire', 100, 'Hydro Hypostasis')

INSERT INTO Food VALUES ('Mint Jelly', 'Food', 1, 'Mint')
INSERT INTO Food VALUES ('Mint Wine', 'Food', 5, 'Mint')
INSERT INTO Food VALUES ('Fruits of the Festival', 'Food', 5, 'Teardrop')

INSERT INTO Domain VALUES ('Domain of Guyun', 'Artifact')   
INSERT INTO Domain VALUES ('Red Desert Threshold', 'Trial')

INSERT INTO Weapon VALUES (1, 'A Thousand Floating Dreams', 5, 80)
INSERT INTO Weapon VALUES (2, 'Sacrificial Sword', 3, NULL) -- we need to add the level
INSERT INTO Weapon VALUES (3, 'The Catch', 1, 90)
INSERT INTO Weapon VALUES (4, 'Rust', 1, 90)
INSERT INTO Weapon VALUES(5, 'Simple Bow', 1, 1)
INSERT INTO Weapon VALUES(6, 'Simple Sword', 1, 1)

INSERT INTO MapLocation VALUES (1, 1)
INSERT INTO MapLocation VALUES (2, 2)
INSERT INTO MapLocation VALUES (3, 3)
INSERT INTO MapLocation VALUES (4, 4)

INSERT INTO Artifact VALUES (1,'Storm Cage', 'Sands', 100, 100, 'Domain of Guyun')
INSERT INTO Artifact VALUES (2,'Gladiator`s Nostalgia', 'Flower', 100, 100, 'Domain of Guyun')
INSERT INTO Artifact VALUES (3,'Sundered Feather', 'Feather', 100, 100, 'Domain of Guyun')
INSERT INTO Artifact VALUES (4,'Scarlet Vessel', 'Goblet', 100, 100, 'Domain of Guyun')
INSERT INTO Artifact VALUES (5,'Ornate Kabuto', 'Circlet', 100, 100, 'Domain of Guyun')

INSERT INTO ArtifactSet VALUES (1, 2, 3, 1, 4, 5, 'atk', 500, 500)



INSERT INTO GameCharacter VALUES ('Nahida', 80, 8, 'Catalyst', 1, 'Vajrada Emerald', 12, 1, 1, 1600, 10000)
INSERT INTO GameCharacter VALUES ('Tighnari', 70, 8, 'Bow', 4, 'Vajrada Emerald', 36, 2, 2, 1300, 14030)
INSERT INTO GameCharacter VALUES ('Raiden Shogun', 80, 8, 'Polearm', 3, 'Teardrop', 12, 3, 3, 1600, 10000)

INSERT INTO BuiltCharacter VALUES ('Nahida', 2, 80, 1600, 10000) -- error, no matching artifact set.
INSERT INTO BuiltCharacter VALUES ('Raiden Shogun', 1, 80, 2100, 10500)
INSERT INTO BuiltCharacter VALUES ('Nahida', 1, 80, 2100, 10500)

-- update 

-- leveling up Nahida and Tighnari
UPDATE GameCharacter
SET Lvl = 90
WHERE Lvl < 80 AND WeaponType IN ('Catalyst', 'Bow') -- used <, =, AND, IN

UPDATE GameCharacter
SET MaterialQuantity = 0
WHERE Lvl = 90 AND WeaponType IN ('Catalyst', 'Bow') 

-- adding a level where it was not added
UPDATE Weapon
SET Lvl = 90
WHERE Lvl IS NULL -- used IS NULL

-- gathered more materials of the crystal type
UPDATE Material
SET Quantity = 200
WHERE MaterialID LIKE 'Vajrada%' AND Quantity BETWEEN 10 AND 20 -- used LIKE, BETWEEN

-- deleting bad weapons
DELETE FROM Weapon
WHERE WeaponID >= 5

-- deleting unreleased map locations
DELETE FROM MapLocation
WHERE CoordinateX = 4