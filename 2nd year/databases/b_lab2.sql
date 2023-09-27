SELECT FoodID, FoodType, Rarity, MaterialUsed
FROM Food
WHERE MaterialUsed = 'Mint'

INTERSECT

SELECT FoodID, FoodType, Rarity, MaterialUsed
FROM Food
WHERE Rarity = 5