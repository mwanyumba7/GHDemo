USE employees_data;
-- Create the original unnormalized table
CREATE TABLE Unnormalized_Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Projects VARCHAR(255), -- Comma-separated list of projects
    ToolsUsed VARCHAR(255), -- Comma-separated list of tools
    Hobbies VARCHAR(255) -- Comma-separated list of hobbies
);

-- Insert sample data into the unnormalized table
INSERT INTO Unnormalized_Employees (EmployeeID, EmployeeName, Projects, ToolsUsed, Hobbies)
VALUES
    (1, 'Alice', 'ProjectA,ProjectB', 'ToolX,ToolY', 'Reading,Painting'),
    (2, 'Bob', 'ProjectC', 'ToolZ', 'Hiking,Photography'),
    (3, 'Charlie', 'ProjectA,ProjectD', 'ToolX,ToolW', 'Gaming,Coding');
    

-- Create a normalized table for 1NF
CREATE TABLE Employees_1NF (
    EmployeeID INT,
    EmployeeName VARCHAR(50),
    Project VARCHAR(50),
    ToolUsed VARCHAR(50),
    Hobby VARCHAR(50)
);

-- Insert data into the 1NF table by splitting the comma-separated values
INSERT INTO Employees_1NF (EmployeeID, EmployeeName, Project, ToolUsed, Hobby)
SELECT 
    e.EmployeeID,
    e.EmployeeName,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(e.Projects, ',', n.n), ',', -1)) AS Project,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(e.ToolsUsed, ',', n.n), ',', -1)) AS ToolUsed,
    TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(e.Hobbies, ',', m.m), ',', -1)) AS Hobby
FROM 
    Unnormalized_Employees e
JOIN 
    (SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3) AS n
ON 
    LENGTH(e.Projects) - LENGTH(REPLACE(e.Projects, ',', '')) >= n.n - 1
JOIN 
    (SELECT 1 AS m UNION ALL SELECT 2 UNION ALL SELECT 3) AS m
ON 
    LENGTH(e.Hobbies) - LENGTH(REPLACE(e.Hobbies, ',', '')) >= m.m - 1;
-- The SUBSTRING_INDEX function splits the comma-separated values into individual rows.
-- The n and m subqueries generate row numbers to handle up to three projects/tools/hobbies per employee.


-- Convert to 2NF : eliminate partial dependencies by separating EmployeeName into its own table.
-- Create the Employees table for 2NF
CREATE TABLE Employees_2NF (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50)
);

-- Populate the Employees table
INSERT INTO Employees_2NF (EmployeeID, EmployeeName)
SELECT DISTINCT EmployeeID, EmployeeName
FROM Employees_1NF;

-- Create the Employee_Projects_Tools_Hobbies table for 2NF
CREATE TABLE Employee_Projects_Tools_Hobbies (
    EmployeeID INT,
    Project VARCHAR(50),
    ToolUsed VARCHAR(50),
    Hobby VARCHAR(50),
    PRIMARY KEY (EmployeeID, Project, ToolUsed, Hobby),
    FOREIGN KEY (EmployeeID) REFERENCES Employees_2NF(EmployeeID)
);

-- Populate the Employee_Projects_Tools_Hobbies table
INSERT INTO Employee_Projects_Tools_Hobbies (EmployeeID, Project, ToolUsed, Hobby)
SELECT EmployeeID, Project, ToolUsed, Hobby
FROM Employees_1NF;


-- Convert to 3NF :  eliminate transitive dependencies by separating ToolUsed and Hobby into their own tables.
-- Create the Employee_Projects table for 3NF
CREATE TABLE Employee_Projects (
    EmployeeID INT,
    Project VARCHAR(50),
    PRIMARY KEY (EmployeeID, Project),
    FOREIGN KEY (EmployeeID) REFERENCES Employees_2NF(EmployeeID)
);

-- Populate the Employee_Projects table
INSERT INTO Employee_Projects (EmployeeID, Project)
SELECT DISTINCT EmployeeID, Project
FROM Employee_Projects_Tools_Hobbies;

-- Create the Employee_Tools table for 3NF
CREATE TABLE Employee_Tools (
    EmployeeID INT,
    ToolUsed VARCHAR(50),
    PRIMARY KEY (EmployeeID, ToolUsed),
    FOREIGN KEY (EmployeeID) REFERENCES Employees_2NF(EmployeeID)
);

-- Populate the Employee_Tools table
INSERT INTO Employee_Tools (EmployeeID, ToolUsed)
SELECT DISTINCT EmployeeID, ToolUsed
FROM Employee_Projects_Tools_Hobbies;

-- Create the Employee_Hobbies table for 3NF
CREATE TABLE Employee_Hobbies (
    EmployeeID INT,
    Hobby VARCHAR(50),
    PRIMARY KEY (EmployeeID, Hobby),
    FOREIGN KEY (EmployeeID) REFERENCES Employees_2NF(EmployeeID)
);

-- Populate the Employee_Hobbies table
INSERT INTO Employee_Hobbies (EmployeeID, Hobby)
SELECT DISTINCT EmployeeID, Hobby
FROM Employee_Projects_Tools_Hobbies;

-- Drop the intermediate table as it's no longer needed
DROP TABLE Employee_Projects_Tools_Hobbies;

-- To achieve 4NF , ensure there are no multi-valued dependencies by keeping ToolsUsed and Hobbies in separate tables 
-- (already done in 3NF).