USE GenshinManager
GO

-- selecting the weapons that are in use and have a level greater than the average of all used weapons' levels
SELECT WeaponType, Lvl
FROM GameCharacter
GROUP BY WeaponType, Lvl
HAVING Lvl >= AVG(Lvl)
ORDER BY WeaponType

-- selecting the rarest foods
SELECT Rarity, FoodID
FROM Food
GROUP BY Rarity, FoodID
HAVING Rarity = (SELECT MAX(Rarity) from Food)


-- selecting the most common foods
SELECT Rarity, FoodID
FROM Food
GROUP BY Rarity, FoodID
HAVING Rarity = (SELECT MIN(Rarity) from Food)
ORDER BY FoodID

-- count all weapons of a type that are in use
SELECT WeaponType, COUNT(Lvl)
FROM GameCharacter
GROUP BY WeaponType
ORDER BY WeaponType
