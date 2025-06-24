# DatabaseToExcelScript
This aims to create an automated report with the use of DB to Excel

# This script is aim to create an automated query through Database and convert the file into Excel.
# If not don’t have a data exist you can try to use this sample code:

CREATE DATABASE db_testDatabase;

CREATE TABLE people (
    id INT PRIMARY KEY identity(1,1),
    name VARCHAR(50),
    age INT,
    sex VARCHAR(10),
    country VARCHAR(50),
    birthday DATE,
    birthdofplace VARCHAR(100)
);

-- Insert 20 rows of data
INSERT INTO people (name, age, sex, country, birthday, birthdofplace) VALUES
('Alice Johnson', 28, 'Female', 'USA', '1996-04-15', 'New York'),
('Bob Smith', 34, 'Male', 'Canada', '1990-11-22', 'Toronto'),
('Carmen Lee', 22, 'Female', 'South Korea', '2002-07-09', 'Seoul'),
('David Miller', 45, 'Male', 'UK', '1979-02-18', 'London'),
('Eva Lopez', 30, 'Female', 'Spain', '1993-12-01', 'Madrid'),
('Frank White', 27, 'Male', 'Australia', '1996-06-25', 'Sydney'),
('Grace Kim', 29, 'Female', 'South Korea', '1994-08-14', 'Busan'),
('Henry Brown', 40, 'Male', 'USA', '1983-03-30', 'Chicago'),
('Isabel Garcia', 33, 'Female', 'Mexico', '1990-10-10', 'Mexico City'),
('Jack Wilson', 26, 'Male', 'Canada', '1997-05-05', 'Vancouver'),
('Kathy Nguyen', 24, 'Female', 'Vietnam', '1999-01-19', 'Hanoi'),
('Liam O’Connor', 38, 'Male', 'Ireland', '1985-09-29', 'Dublin'),
('Mona Patel', 31, 'Female', 'India', '1992-11-13', 'Mumbai'),
('Nate Thomas', 35, 'Male', 'USA', '1988-07-21', 'Los Angeles'),
('Olivia Sanchez', 28, 'Female', 'Argentina', '1995-04-04', 'Buenos Aires'),
('Peter Müller', 42, 'Male', 'Germany', '1981-12-15', 'Berlin'),
('Quinn Taylor', 23, 'Non-binary', 'UK', '2000-03-07', 'Manchester'),
('Rita Fernandez', 36, 'Female', 'Colombia', '1987-08-11', 'Bogotá'),
('Steve Rogers', 39, 'Male', 'USA', '1984-06-13', 'Boston'),
('Tina Wang', 25, 'Female', 'China', '1998-02-28', 'Beijing');

/* Now create your query statement. Eg. "SELECT * FROM people" Table 
Install the SQL Command Line Utility
https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver16&tabs=odbc%2Cwindows%2Cwindows-support&pivots=cs1-cmd#download-and-install
*/

Now we have this kind of command 

