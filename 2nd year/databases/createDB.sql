CREATE DATABASE GenshinManager
GO
USE GenshinManager
GO

ALTER AUTHORIZATION ON DATABASE::GenshinManager TO sa;
GO

CREATE TABLE Boss(
BossID varchar(50) PRIMARY KEY,
FirstDrop varchar(50),
SecondDrop varchar(50)
)

CREATE TABLE Weapon(
WeaponID int PRIMARY KEY,
WName varchar(50),
Refinement smallint,
Lvl smallint
)

CREATE TABLE Material(
MaterialID varchar(50) PRIMARY KEY,
Quantity int,
DroppedBy varchar(50) FOREIGN KEY REFERENCES Boss(BossID)
)

CREATE TABLE MapLocation(
CoordinateX int,
CoordinateY int,
CONSTRAINT LocationID PRIMARY KEY (CoordinateX, CoordinateY)
)

CREATE TABLE GameCharacter(
CharID varchar(50) PRIMARY KEY, -- name
Lvl smallint,
TalentLvl smallint,
WeaponType varchar(50),
HeldWeapon int FOREIGN KEY REFERENCES Weapon(WeaponID),
NeededMaterial varchar(50) FOREIGN KEY REFERENCES Material(MaterialID),
MaterialQuantity int,
FirstMetX int,
FirstMetY int,
FOREIGN KEY (FirstMetX, FirstMetY) REFERENCES MapLocation(CoordinateX, CoordinateY),
Attack int,
HP int
)

CREATE TABLE Domain(
DomainID varchar(50) PRIMARY KEY,
DomainType varchar(50)
)


CREATE TABLE Artifact(
ArtifactID int PRIMARY KEY,
ArtifactName varchar(50),
ArtifactType varchar(50),
AttackBonus int,
HPBonus int,
ObtainedFrom varchar(50) FOREIGN KEY REFERENCES Domain(DomainID)
)

CREATE TABLE ArtifactSet(
ArtifactSetID int PRIMARY KEY,
Flower int FOREIGN KEY REFERENCES Artifact(ArtifactID),
Feather int FOREIGN KEY REFERENCES Artifact(ArtifactID),
Sands int FOREIGN KEY REFERENCES Artifact(ArtifactID),
Goblet int FOREIGN KEY REFERENCES Artifact(ArtifactID),
Circlet int FOREIGN KEY REFERENCES Artifact(ArtifactID),
SetBonus varchar(5), -- atk/hp
AttackTotal int,
HPTotal int
)

CREATE TABLE BuiltCharacter(
CharID varchar(50) FOREIGN KEY REFERENCES GameCharacter(CharID),
ArtifactSetID int FOREIGN KEY REFERENCES ArtifactSet(ArtifactSetID),
CONSTRAINT BuiltCharID PRIMARY KEY (CharID, ArtifactSetID),
Lvl smallint,
Attack int,
HP int
)

CREATE TABLE Food(
FoodID varchar(50) PRIMARY KEY,
FoodType varchar(5),
Rarity smallint,
UsedMaterial VARCHAR(50) FOREIGN KEY REFERENCES Material(MaterialID)
)

