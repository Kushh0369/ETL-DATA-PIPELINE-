import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# ---------- EXTRACT ----------
def extract(file_path):
    df = pd.read_csv(file_path)
    logging.info(f"Data Extracted. Shape: {df.shape}")
    return df


# ---------- TRANSFORM ----------
def transform(df):
    df = df.dropna()                       # missing values hatao
    df = df.drop_duplicates()              # duplicate rows hatao
    df.columns = df.columns.str.lower()    # column names lowercase
    logging.info(f"Data Transformed. Shape: {df.shape}")
    return df


# ---------- LOAD ----------
def load(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    logging.info(f"Data Loaded into {db_name} -> table: {table_name}")


# ---------- RUN PIPELINE ----------
if __name__ == "__main__":
    try:
        df = extract("data.csv")
        df = transform(df)
        load(df, "output.db", "cleaned_data")
        logging.info("Pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")