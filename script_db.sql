USE Kaggle
GO 

IF NOT EXISTS (SELECT * FROM SYS.TABLES WHERE object_id = OBJECT_ID(N'dbo.TSLA') AND TYPE = 'U')
	CREATE TABLE dbo.TSLA (
		FECHA DATE,
		Open_DB FLOAT,
		High_DB FLOAT,
		Low_DB FLOAT,
		Close_DB FLOAT,
		Adj_Close FLOAT,
		Volume FLOAT
	)
GO

TRUNCATE TABLE dbo.TSLA;
GO

BULK INSERT dbo.TSLA
FROM 'C:\Users\FABIAN\Documents\DevOps\proyecto_parcial\python\dataset\TSLA.csv'
WITH 
(
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '0x0a'
)
GO