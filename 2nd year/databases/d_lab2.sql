USE GenshinManager
GO

-- get foods using a certain material
SELECT *
FROM Food
INNER JOIN Material
ON Food.MaterialUsed = Material.MaterialID


-- get all characters that use the same set
SELECT *
FROM BuiltCharacter
LEFT JOIN ArtifactSet
ON BuiltCharacter.ArtifactSetID = ArtifactSet.ArtifactSetID

SELECT *
FROM GameCharacter
RIGHT JOIN Weapon
ON GameCharacter.HeldWeapon = Weapon.WeaponID

-- getting all drops that are used for food and for upgrades
SELECT DISTINCT *
FROM Boss
FULL JOIN Food ON Boss.SecondDrop = Food.MaterialUsed
FULL JOIN GameCharacter ON Boss.SecondDrop = GameCharacter.NeededMaterial