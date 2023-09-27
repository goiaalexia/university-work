USE GenshinManager
GO

CREATE VIEW View_1_table AS
		select * from Boss
GO


CREATE VIEW View_2_tables AS
SELECT * FROM Boss
INNER JOIN Material
ON Boss.BossID = Material.DroppedBy
GO


CREATE VIEW View_2_tables_group_by AS
SELECT BossID FROM Boss
INNER JOIN Material
ON Boss.BossID = Material.DroppedBy
GROUP BY Boss.BossID
GO