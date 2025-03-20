# Getting Started and Loading Data

1. Open an Excel workbook and launch the Power Query editor.

2. Load the dailycensus_7665.xlsx Excel file (sheet dailycensus) into Power Query.

3. The column headers need to be corrected. Use the Remove Rows feature in the Home ribbon to remove the first row.

Note if you are using Mac OS, you may need to remove the first two rows if the first row shows "col1", "col2", "col3", etc._

4. Next, you need to make the column headers correctly display their name by selecting Use First Row as Headers from the Transform section of the Home ribbon tab.

5. Now, update the effective_date field to type Date.

Note: If a "Change Column Type" pop-up appears, select "Replace Current".

6. You can sort rows by clicking the arrow next to the column header. Sort effective_date in descending order.

# Managing Columns

We will be loading a file on drug administrations and set it up for a quick ad-hoc analysis of prescription dates by doctor

1. With Power Query editor opened, load the drug_administrations.txt file.

2. Keep only columns `prescription_date` and `prescribing_doctor_id`.

3. Rename this new query: `prescription_dates_by_doctor`.

4. Close and load the data from the Power Query editor and view the table of your newly created query in Excel.

5. Use the `COUNTIF()` function in an empty cell in your Excel Workbook to calculate the total number of rows attributed to `prescribing_doctor_id` "D098"

6. There are reports that Doctor 0987 prescribes much more medications than their peers. We expect each doctor to comprise 5% of total prescriptions. What is the proportion of total prescriptions for Doctor 0987? (Provide your answer in X.XX% format).
<details>
  <summary>Click to reveal answer</summary>
  9.90%
</details>

# Extracting PDF Data
You have been sent another data file to be prepped. This PDF file is a list of 11 survey questions that are distributed to patients who had a recent hospital encounter.

Your task will be to load this content into Power Query.

1. With the Power Query editor open, load the Patient Experience Survey Template PDF file.
In the "Navigator" pop-up window, assess the preview options and select the one that includes all 11 survey questions.

2. There’s a lot of unnecessary content in here! Keep only the first and last columns.

3. Many of these rows are not showing any information that we need. Remove the top 7 rows.

4. Label the two columns "question" and "questionid".

5. Filter out any rows with null or "[]"for the question and question id columns.
Next, re-order columns so that questionid is first.

6. Rename the query: "PatientExperienceSurveyQuestions".

7. Your boss wanted to double-check what the last transformation done on this file to prepare it for loading. What is the formula displayed in the last applied step?


