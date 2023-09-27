USE GenshinManager
GO

CREATE OR ALTER PROCEDURE [dbo].[insert_rows] 
	-- Add the parameters for the stored procedure here
	@nb_of_rows varchar(30),
	@table_name varchar(30)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	declare @table varchar(100)
	set @table = ('[' + @table_name + ']')

    -- Insert statements for procedure here
	if ISNUMERIC(@nb_of_rows) != 1
	BEGIN
		print('Not a number')
		return 1 
	END
	
	SET @nb_of_rows = cast(@nb_of_rows as INT)

	declare @contor int
	set @contor = 1

	declare @boss_id varchar(50)
	declare @first_drop varchar(50)
	declare @second_drop varchar(50)

	declare @material_id varchar(50)
	declare @quantity int
	declare @dropped_by varchar(50)

	declare @mapx int
	declare @mapy int

	set @mapx = 10
	set @mapy = 10

	while @contor <= @nb_of_rows
	begin
		if @table_name = 'Boss'
		begin
			set @boss_id = 'Boss Name' + convert(varchar(7), @contor)
			set @first_drop = 'First Drop' + convert(varchar(7), @contor)
			set @second_drop = 'Second Drop' + convert(varchar(7), @contor)
			insert into Boss (BossID, FirstDrop, SecondDrop) values (@boss_id, @first_drop, @second_drop)
		end
		
		if @table_name = 'Material'
		begin
			set @material_id = 'Material Name' + convert(varchar(7), @contor)
			set @quantity = 10000
			set @dropped_by = 'Boss Name' + convert(varchar(7), @contor)
			insert into Material(MaterialID,Quantity,DroppedBy) values (@material_id, @quantity, @dropped_by)
		end
		if @table_name = 'MapLocation'
		begin
			insert into MapLocation (CoordinateX, CoordinateY) values (@mapx, @mapy)
			set @mapx = @mapx + 1
			set @mapy = @mapy + 1
		end

		set @contor = @contor + 1
	end
	
END