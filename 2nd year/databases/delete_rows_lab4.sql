USE GenshinManager
GO

CREATE OR ALTER PROCEDURE dbo.delete_rows
	-- add the parameters for the stored procedure here
	@nb_of_rows varchar(30),
	@table_name varchar(30)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	declare @contor int
	set @contor = 1
    -- Insert statements for procedure here
	if ISNUMERIC(@nb_of_rows) != 1
	BEGIN
		print('Not a number')
		return 1 
	END
	SET @nb_of_rows = cast(@nb_of_rows as INT)
	declare @last_row int

	declare @MyCursor cursor
	SET @MyCursor = CURSOR FOR
    select top 1000 MaterialID from Material   

	declare @MyCursor2 cursor
	SET @MyCursor2 = CURSOR FOR
    select top 1000 CharID from GameCharacter 

	declare @MyCursor3 cursor
	SET @MyCursor3 = CURSOR FOR
    select top 1000 CoordinateX, CoordinateY from MapLocation

	declare @char_id varchar(50)
	declare @material_id varchar(50)
	declare @mapx int
	declare @mapy int

    OPEN @MyCursor 
    FETCH NEXT FROM @MyCursor 
    INTO @char_id

	OPEN @MyCursor2 
    FETCH NEXT FROM @MyCursor2 
    INTO @material_id

	OPEN @MyCursor3
    FETCH NEXT FROM @MyCursor3 
    INTO @mapx, @mapy


	if @table_name = 'Boss'
		begin
			delete from BuiltCharacter
			delete from GameCharacter
			delete from Material
			delete from Boss
		end
		
		if @table_name = 'Material'
		begin
		-- delete built character first, then game character, then material
			  delete from BuiltCharacter
			  delete from GameCharacter
			  delete from Food
			  delete from Material
		end

		if @table_name = 'MapLocation'
			  delete from BuiltCharacter
			  delete from GameCharacter
			delete from MapLocation
		
		CLOSE @MyCursor ;
		DEALLOCATE @MyCursor;
		CLOSE @MyCursor2 ;
		DEALLOCATE @MyCursor2;
		CLOSE @MyCursor3;
		DEALLOCATE @MyCursor3
END