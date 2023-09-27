USE DummyTables
drop table Tc
drop table Tb
drop table Ta
SET NOCOUNT ON;

CREATE TABLE Ta(
	aid integer not null primary key,
	a2 integer unique,
	a3 integer
)



CREATE TABLE Tb(
	bid integer not null primary key,
	b2 integer
)

CREATE Table Tc(
	cid integer not null primary key,
	aid integer,
	bid integer,
	foreign key (aid) references Ta(aid) on delete cascade on update cascade,
	foreign key (bid) references Tb(bid) on delete cascade on update cascade
)

IF EXISTS (SELECT [name] FROM sys.objects 
            WHERE object_id = OBJECT_ID('RandIntBetween'))
BEGIN
   DROP FUNCTION RandIntBetween;
END
GO


-- With this function I generate a random number taken from a given interval
CREATE FUNCTION RandIntBetween(@lower INT, @upper INT, @rand FLOAT)
RETURNS INT
AS
BEGIN
  DECLARE @result INT;
  DECLARE @range INT = @upper - @lower + 1;
  SET @result = FLOOR(@rand * @range + @lower);
  RETURN @result;
END
GO

-- With this procedure I insert some random data into the table Ta
CREATE OR ALTER PROC insertDataIntoTa
@nrOfRows INT
AS
BEGIN
	DECLARE @aid INT
	DECLARE @a2 INT
	DECLARE @a3 INT
	SET @aid  = (SELECT MAX(aid) + 1 FROM Ta)
	if @aid is NULL
		SET @aid = 1
	SET @a2 = (SELECT MAX(a2) + 1 FROM Ta)
	if @a2 is NULL
		SET @a2 = 1
	WHILE @nrOfRows > 0
	BEGIN
		SET @a3 = [dbo].[RandIntBetween](1, 100, RAND())
		INSERT INTO Ta(aid, a2, a3) VALUES (@aid, @a2, @a3)
		SET @nrOfRows = @nrOfRows - 1
		SET @aid = @aid + 1
		SET @a2 = @a2 + 1
	END
END
GO

EXEC insertDataIntoTa 300
SELECT * FROM Ta

EXEC sp_helpindex Ta
-- primary key constraint on aid column => clustered index automatically created on aid column
-- unique constraint on a2 column       => non-clustered index automaticall created on a2 column

-- 1. Clustered Index Scan
-- have to scan the entire table for the matching rows -> scan
-- ESC: 

SELECT a3
FROM Ta
WHERE a3 = 10

-- 2. Clustered Index Seek
-- particular range of rows from a clustered index -> seek
-- ESC:

SELECT a3
FROM Ta
WHERE aid between 1 and 100

-- 3. Non-Clustered Index Scan
-- retrives all the rows from the table -> scan
-- ESC:

SELECT a2
FROM Ta

-- 4. Non-Clustered Index Seek
-- for example when we search for particulars values of the a2 column on which we have a unique constraint => seek
-- ESC:

SELECT a2
FROM Ta
WHERE a2 >30

-- 5. Key Look-Up
-- non-clustered index seek and key look up
-- ESC: 

SELECT a2, a3
FROM Ta
WHERE a2 = 30
GO

create or alter view view1 as
    select top 1000 T1.x, T2.b2
    from Tc T3 join Ta T1 on T3.aid = T1.aid join Tb T2 on T3.bid = T2.bid
    where T2.b2 > 500 and T1.x < 15

-- This selects all rows from the "viewClustered" view
select * from view1
go

/*
create nonclustered index idx1
	on Ta(a3)

drop index Ta.idx1

sp_helpindex Ta

select *
from Ta
where a2 = 30 and a3 = 10
*/