-- write 2 queries with the union operation; use UNION [ALL] and OR;
USE GenshinManager
GO

-- getting the weapons of Dendro characters
SELECT WeaponID, WName, Refinement, Lvl
FROM Weapon
WHERE WeaponID = 1 OR WeaponID = 4

UNION ALL

-- getting the other weapons
SELECT WeaponID, WName, Refinement, Lvl
FROM Weapon
WHERE WeaponID = 3 OR WeaponID = 2