import os
import pandas as pd
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(ROOT, "data", "city_stats_small.csv")
OUT_DIR = os.path.join(ROOT, "outputs")
PLOTS_DIR = os.path.join(OUT_DIR, "plots")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

df = pd.read_csv(DATA)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
df["year"] = df["year"].astype(int)
df["population"] = df["population"].astype(int)
df["median_income"] = df["median_income"].astype(int)

by_city = df.groupby("city", as_index=False).agg(
    avg_population=("population", "mean"),
    avg_median_income=("median_income", "mean"),
    count=("year", "count"),
).sort_values("avg_population", ascending=False)

over_time = df.groupby("year", as_index=False).agg(
    total_population=("population", "sum"),
    avg_median_income=("median_income", "mean"),
).sort_values("year")

by_city.to_csv(os.path.join(OUT_DIR, "summary_by_city.csv"), index=False)
over_time.to_csv(os.path.join(OUT_DIR, "summary_over_time.csv"), index=False)

plt.figure()
plt.bar(by_city["city"], by_city["avg_population"])
plt.title("Average Population by City")
plt.xlabel("City")
plt.ylabel("Avg Population")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "population_by_city.png"))
plt.close()

plt.figure()
plt.bar(by_city["city"], by_city["avg_median_income"])
plt.title("Average Median Income by City")
plt.xlabel("City")
plt.ylabel("Avg Median Income (USD)")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "income_by_city.png"))
plt.close()

print("✅ Done. Outputs saved in:", OUT_DIR)
