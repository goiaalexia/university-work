USE GenshinManager
GO

-- getting all characters if they are built and over lvl 80
SELECT DISTINCT *
FROM GameCharacter
WHERE EXISTS (SELECT CharID
              FROM BuiltCharacter
              WHERE Lvl >= 80 AND GameCharacter.CharID = BuiltCharacter.CharID)


-- getting all characters if they are built and have over 2000 HP
SELECT DISTINCT *
FROM GameCharacter
WHERE EXISTS (SELECT CharID
              FROM BuiltCharacter
              WHERE HP > 9000 AND GameCharacter.CharID = BuiltCharacter.CharID)