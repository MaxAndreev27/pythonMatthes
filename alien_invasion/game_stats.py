import json
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        # Визначаємо шлях один раз при ініціалізації
        self.save_path = Path(__file__).parent / "save.json"
        self.reset_stats()

        # Завантажуємо рекорд
        self.high_score = self._get_high_score_from_file()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score_from_file(self):
        """Безпечне зчитування рекорду."""
        if self.save_path.exists():
            try:
                with open(self.save_path, "r") as f:
                    data = json.load(f)
                    # Якщо ми перейшли на словник:
                    return data.get("high_score", 0)
            except (json.JSONDecodeError, AttributeError):
                return 0  # Якщо файл битий
        return 0

    def save_high_score(self):
        """Запис рекорду лише у форматі словника."""
        # Готуємо дані для збереження
        stats_data = {"high_score": self.high_score, "last_level": self.level}
        with open(self.save_path, "w") as f:
            json.dump(stats_data, f, indent=4)
