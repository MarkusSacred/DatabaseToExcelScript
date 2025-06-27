@echo off
"C:\Program Files (x86)\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\SQLCMD.EXE" -S ServerName -d databaseName -Q "YourQuery" -o "YourFilePath\report.csv" -s "," -W -h -1
