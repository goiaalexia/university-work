USE GenshinManager
GO

-- getting all characters that are built and above level 80
SELECT *
FROM GameCharacter
WHERE CharID IN (SELECT CharID
                 FROM BuiltCharacter
                 WHERE Lvl >= 80)

-- getting all characters that are built and use a catalyst                
SELECT *
FROM GameCharacter
WHERE CharID IN (SELECT CharID
                 FROM BuiltCharacter
                 WHERE WeaponType = 'Catalyst')