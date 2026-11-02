# Python Advanced Mastering - Combined Study Repository

This repository tracks my personal code implementations, technical notes, complex exercises, and advanced engineering projects based on the comprehensive study of three modern Python volumes:

1. **"Learning Python" (Изучаем Python, 2025)** by Eric Mattheis
2. **"Python All-in-One" (Весь Python, 2026)** by Fabrizio Romano and Heinrich Kruger
3. **"Powerful Python" (Мощный Python, 2025)** by Aaron Maxwell

The objective of this collection is to advance from standard programming paradigms to master idiomatic Python (Pythonic code), robust architectural patterns, internal mechanisms, runtime performance optimizations, and full-scale software development.

## 🚀 Repository Structure

Each chapter is a separate folder. Folders with third-party dependencies are standalone uv projects (`pyproject.toml` + `uv.lock` + `.python-version`).

```text
.
├── README.md
├── alien_invasion/                  # Pygame project (uv project)
├── chapter01_Hello/                 # Hello world
├── chapter02_Variables/             # Variables
├── chapter03_Lists/                 # Lists
├── chapter04_WorkLists/             # Working with lists
├── chapter05_IfOperator/            # Conditional operator
├── chapter06_Dictionary/            # Dictionaries
├── chapter07_While/                 # While loops
├── chapter08_Functions/             # Functions and modules
├── chapter09_Classes/               # Classes
├── chapter10_Files/                 # Files, exceptions, JSON, CSV
├── chapter11_Tests/                 # Testing with pytest (uv project)
├── chapter15_DataAnalysisPlotly/    # Matplotlib/Plotly basics (uv project)
├── chapter16_LoadData/              # CSV/JSON data loading (uv project)
├── chapter17_API/                   # Web APIs (uv project)
├── chapter18_JupiterNotebook/       # Jupyter notebooks (uv project)
├── chapter19_NumPy/                 # NumPy (uv project)
├── chapter20_Pandas/                # Pandas (uv project)
├── chapter21_Matplotlib/            # Matplotlib/Seaborn (uv project)
├── chapter22_Scikitlearn/           # Scikit-learn (uv project)
├── chapter23_async/                 # asyncio
├── chapter24_SOLID/                 # SOLID principles
├── learning_log/                    # Django web app (uv project)
└── power_python/                    # Powerful Python: decorators, generators, iterators, etc.
```

## ⚙️ Environment (uv)

Python 3.12 is managed with [uv](https://docs.astral.sh/uv/). Install it once:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Work inside a chapter folder that has a `pyproject.toml`:

```bash
cd chapter15_DataAnalysisPlotly
uv sync                          # creates .venv and installs locked dependencies
uv run python mpl_squares.py     # run a script in the project environment
uv add <package>                 # add a dependency (updates pyproject.toml and uv.lock)
uv lock --upgrade                # refresh uv.lock to the latest allowed versions
```

Examples: `cd chapter11_Tests && uv run pytest`, `cd learning_log && uv run python manage.py runserver`.
For Jupyter chapters, select the `.venv` interpreter as the notebook kernel. Chapters without a `pyproject.toml` use only the standard library: `uv run python file.py`.

## 📜 Community Standards

This repository adheres to GitHub's 100% Community Standards to ensure open, high-quality, and maintainable software practices:

- **License**: [LICENSE](LICENSE) (MIT License)
- **Code of Conduct**: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Contributing Guidelines**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Security Policy**: [SECURITY.md](SECURITY.md)
- **Issue Templates**:
  - [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)
  - [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md)
- **Pull Request Template**: [PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)
