USE GenshinManager
GO

-- get all the weapons
SELECT WeaponID, WName, Refinement, Lvl
FROM Weapon
WHERE WeaponID IS NOT NULL

EXCEPT

-- excepting the catalyst
SELECT WeaponID, WName, Refinement, Lvl
FROM Weapon
WHERE WeaponID = 1