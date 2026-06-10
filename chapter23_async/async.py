import asyncio
import time


# Ключове слово 'async' перетворює звичайну функцію на корутину (coroutine)
async def fetch_data(service_name: str, delay: int) -> dict:
    print(f"📡 [Запуск] Запит до {service_name}...")

    # Ключове слово 'await' призупиняє виконання ЦІЄЇ функції,
    # віддаючи контроль Event Loop'у, щоб інші завдання могли виконуватися в цей час.
    # asyncio.sleep імітує неблокуюче мережеве очікування (I/O)
    await asyncio.sleep(delay)

    print(f"✅ [Успіх] Дані від {service_name} отримано!")
    return {service_name: "data_payload"}


async def main():
    start_time = time.time()
    print("🚀 Початок роботи асинхронного Event Loop...")

    # Запускаємо обидві корутини паралельно за допомогою asyncio.gather.
    # Програма не чекатиме завершення першої, щоб почати другу.
    results = await asyncio.gather(
        fetch_data("API_1 (Користувачі)", 2), fetch_data("API_2 (Товари)", 3)
    )

    end_time = time.time()

    print("-" * 40)
    print(f"📊 Результати збору даних: {results}")
    # Загальний час буде ~3 секунди (максимальний delay), а не 5 (2 + 3)
    print(f"⏱️ Загальний час виконання: {end_time - start_time:.2f} секунд.")


if __name__ == "__main__":
    # Точка входу: створює цикл подій (Event Loop) і запускає головну корутину
    asyncio.run(main())
