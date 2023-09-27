USE GenshinManager
GO

SELECT CharID
FROM (SELECT *
      FROM GameCharacter
      WHERE Lvl > 80) AS GC

SELECT CharID
FROM (SELECT *
      FROM GameCharacter
      WHERE Lvl > 70 AND Lvl <= 80) AS GC