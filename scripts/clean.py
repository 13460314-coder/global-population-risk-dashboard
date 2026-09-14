import json
import csv

# 讀取原始人口資料
with open("data/raw.txt", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 轉換資料型態
population = []

for row in data:
    population.append({
        "year": int(row["year"]),
        "population_billion": float(row["population_billion"])
    })

# 計算平均人口
average = sum(item["population_billion"] for item in population) / len(population)

# 計算各期間成長率
growth_rates = []

for i in range(1, len(population)):
    previous = population[i - 1]
    current = population[i]

    growth_rate = (
        (current["population_billion"] - previous["population_billion"])
        / previous["population_billion"]
        * 100
    )

    growth_rates.append({
        "period": f'{previous["year"]}-{current["year"]}',
        "growth_rate_percent": round(growth_rate, 2)
    })

# 計算 2024 到 2100 CAGR
start_population = population[0]["population_billion"]
end_population = population[-1]["population_billion"]
years = population[-1]["year"] - population[0]["year"]

cagr = ((end_population / start_population) ** (1 / years) - 1) * 100

# 整理輸出結果
result = {
    "source": "UN World Population Prospects 2024",
    "population": population,
    "average_population_billion": round(average, 2),
    "growth_rates": growth_rates,
    "cagr_2024_2100_percent": round(cagr, 3)
}

# 輸出 JSON
with open("data/cleaned.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

print("Population data cleaned successfully.")
print(json.dumps(result, ensure_ascii=False, indent=2))
