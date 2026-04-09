from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from meteostat import daily

# 33345 — код метеостанції Харків (аеропорт)
station_id = "33345"

start = datetime(2025, 1, 1)
end = datetime(2025, 12, 31)

print(f"Завантаження даних для Харкова (станція {station_id})...")

data = daily(station_id, start, end)
data = data.fetch()

if data is not None and not data.empty:
    # Зберігаємо в CSV
    save_path = Path(__file__).parent / "weather_data/kharkiv_weather_2025.csv"
    data.to_csv(save_path)
    print("Дані збережено у файл 'kharkiv_weather_2025.csv'")

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots(figsize=(12, 6))

    # Малюємо графік
    ax.plot(data.index, data["tmax"], color="red", alpha=0.5, label="Макс. °C")
    ax.plot(data.index, data["tmin"], color="blue", alpha=0.5, label="Мін. °C")
    ax.fill_between(data.index, data["tmax"], data["tmin"], facecolor="blue", alpha=0.1)

    # Оформлення
    ax.set_title("Температура в Харкові, 2026", fontsize=20)
    ax.set_xlabel("Дата", fontsize=12)
    ax.set_ylabel("Градуси Цельсія", fontsize=12)
    ax.legend()

    fig.autofmt_xdate()
    plt.show()
else:
    print("Дані не знайдено. Перевірте з'єднання з інтернетом.")
