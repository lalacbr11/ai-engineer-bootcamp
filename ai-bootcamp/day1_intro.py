from datetime import date
import pandas as pd
from pathlib import Path

print("--- Day 1 Intro ---")
print("Student: Laura")
print("Date:", date.today().isoformat())

csv_path = Path("study_schedule.csv")
if csv_path.exists():
    df = pd.read_csv(csv_path)
    print("\nLoaded study_schedule.csv:")
    print(df)
else:
    print("\nstudy_schedule.csv not found. Run your Jupyter notebook first.")
