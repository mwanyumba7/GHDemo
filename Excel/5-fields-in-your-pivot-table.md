---
title: Fields in your pivot table
video: https://youtu.be/mNWik8HBkXU
code-along: False
---

## Field in your pivot table

### Example Dataset

| Date   | Salesperson | Product | Region | Sales |
| ------ | ----------- | ------- | ------ | ----- |
| 01-Jan | John        | Laptop  | East   | 800   |
| 02-Jan | Mary        | Phone   | West   | 500   |
| 03-Jan | John        | Tablet  | East   | 400   |
| 04-Jan | David       | Laptop  | South  | 800   |
| 05-Jan | Mary        | Phone   | West   | 500   |

After creation of your pivot table, you will see 4 areas:

### Rows

Fields placed here appear vertically.

**Example:** 
- Salesperson
- Region

### Columns

Fields placed here appear horizontally.

**Example:**
- Product
- Month

### Values

Fields placed here are summarized.

**Example:**
- Sales
- Quantity

By default:
- Numbers - Sum
- Text - Count

### Filters

Used to filter the entire report.

**Example:**
- Region
- Year

### Example: Total Sales by Salesperson
Drag:

- Salesperson - Rows
- Sales - Values

Result:

| Salesperson | Sum of Sales |
| ----------- | ------------ |
| John        | 1200         |
| Mary        | 1000         |
| David       | 800          |

No formulas required.

### Changing Calculation Type

Click dropdown in Values - Value Field Settings

You can change to:
- Sum
- Count
- Average
- Max
- Min
- % of Total
- Running Total

**Example:**

Change Sum to Average to get average sales per person.

### Two-Dimensional Pivot Table
Sales by Salesperson and Product

Drag:

- Salesperson - Rows
- Product - Columns
- Sales - Values

Result:

|       | Laptop | Phone | Tablet |
| ----- | ------ | ----- | ------ |
| John  | 800    | 0     | 400    |
| Mary  | 0      | 1000  | 0      |
| David | 800    | 0     | 0      |

This shows data comparison clearly.


