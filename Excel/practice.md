# Working with structured cell references

1. Open 1_4_working_with_structured_references.xlsx on your local computer.

2. Create a new column OrderToDelivery between DeliveryDueDate and CustomerName columns

3. Write a formula that calculates the difference between OrderDate and DeliveryDueDate for each row.
    - Use a structured cell reference (column name instead of cell reference). You can refer to a column name using the @ symbol.

4. That doesn't look quite right! It's defaulted to a date… let's change it by changing the data type to "Number".

5. How many days on average does it take for Adventure Works to deliver once a customer has placed an order? Round to the nearest whole number.

# Filtering data

1. Filter the table in the `Sales` worksheet to display orders from September 2017 only.

2. Now it's time to sort your orders by two columns in the following priority:
    - CustomerCountry (A-Z)
    - OrderDate (Oldest to Newest)

     <details>
        Navigating to Home > Sort & Filter (in Editing) > Custom Sort.

        The first sort by should be CustomerCountry which will be sorted on Cell Values with the order A to Z.

        Add the next column to sort by clicking + Add Level.
        
        The second sort should be OrderDate on Cell Values with the order Oldest to Newest and click OK.
     </details>

3. What is the order number for the first visible row in the table after the data has been filtered and sorted? 

     <details>
        SO44323
    </details>

# Formatting tables

1. Remove any previous filters applied from the last exercise, we want to see all orders.
Change the sort to only sort by `OrderNo` ascending.

    <details>
        To update a custom sort:
        Navigate to Home > Sort & Filter (in Editing) > Custom Sort.
        Select the level to delete, and click Delete Level.
        Change the first sort by column to OrderNo.
    </details>

2. Format the following columns as Currency: `ItemCost` and `ItemPrice`.

3. Format the following columns as Number with 0 decimal places: `SalesOrderLineKey`, `OrderQuantity`, and `OrderToDelivery`.

4. Format all other columns as Text.

5. How many columns are formatted as text in our Sales table?

# Pivot Tables 

Look into Pivot Tables and create a Pivot Table In Excel 

