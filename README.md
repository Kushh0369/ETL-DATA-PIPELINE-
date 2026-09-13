# ETL Data Pipeline

A simple ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and SQLite.

## What this project does

This project takes a raw CSV file, cleans it, and loads it into a SQLite database — a basic example of how data engineers move and prepare data for use.

- **Extract**: Reads student data from a CSV file
- **Transform**: Removes missing values and duplicate rows, standardizes column names
- **Load**: Saves the cleaned data into a SQLite database table

## Dataset

[Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset) from Kaggle — 2,392 rows, 15 columns of academic performance data.

## Tools Used

- Python
- Pandas
- SQLite3
- Logging module (for tracking pipeline execution)

## How to Run

```bash
pip install pandas
python etl_pipeline.py
```

## Output

The script creates `output.db`, a SQLite database containing the cleaned data in a table called `cleaned_data`.

```
Data Extracted. Shape: (2392, 15)
Data Transformed. Shape: (2392, 15)
Data Loaded into output.db -> table: cleaned_data
Pipeline completed successfully.
```
