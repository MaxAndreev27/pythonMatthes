import pandas as pd
import plotly.express as px
import requests

# 1. Виконуємо виклик API та перевіряємо відповідь.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Перевірка на успішність запиту
if r.status_code != 200:
    print(f"Error: Unable to fetch data from GitHub. Reason: {r.reason}")
    exit()

# 2. Обробка загальних результатів.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# 3. Обробка інформації про репозиторії.
repo_dicts = response_dict["items"]
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Перетворюємо імена репозиторіїв на клікабельні посилання.
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    # Формуємо текст для підказок (hover).
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"] or "No description provided."
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 4. Візуалізація.
# Використання DataFrame вирішує проблему порожніх стовпців у нових версіях Plotly.
df = pd.DataFrame(
    {"Repository": repo_links, "Stars": stars, "Description": hover_texts}
)

title = "Most-Starred Python Projects on GitHub"
labels = {"Repository": "Repository", "Stars": "Stars"}

# Створюємо графік, передаючи DataFrame як джерело даних.
fig = px.bar(
    df, x="Repository", y="Stars", title=title, labels=labels, hover_name="Description"
)

# Налаштування вигляду графіка.
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,  # Нахиляємо підписи, щоб вони не перекривали один одного.
)

# Налаштування кольору та прозорості стовпців.
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

# Відображення графіка.
fig.show()
