USE GenshinManager
GO

-- get all characters with a level higher than any characters using Vajrada Emeralds (for upgrade purposes)
SELECT *
FROM GameCharacter
WHERE Lvl > ANY (SELECT Lvl
                 FROM BuiltCharacter
                 WHERE NeededMaterial = 'Vajrada Emerald')

-- get all foods that have a smaller rarity than all other foods
SELECT *
FROM Food
WHERE Rarity <= ALL (SELECT Rarity
                 FROM Food)

-- get all characters that are also built
SELECT *
FROM GameCharacter
WHERE CharID IN (SELECT CharID
              FROM BuiltCharacter)

-- get all unbuilt characters
SELECT *
FROM GameCharacter
WHERE CharID NOT IN (SELECT CharID
              FROM BuiltCharacter)
