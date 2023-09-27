USE GenshinManager
GO

CREATE OR ALTER PROCEDURE [dbo].[select_view] 
	-- Add the parameters for the stored procedure here
	@view_name varchar(30)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	if @view_name = 'View_1_table'
	begin
		select * from View_1_table
	end

	if @view_name = 'View_2_tables'
	begin
		select * from View_2_tables
	end

	if @view_name = 'View_2_tables_group_by'
	begin
		select * from View_2_tables_group_by
	end
END