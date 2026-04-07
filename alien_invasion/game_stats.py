import json
from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self._get_high_score_from_file()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score_from_file(self):
        """Loading high_score from file"""
        base_dir = Path(__file__).parent
        path = base_dir / "save.json"

        if path.exists():
            contents = path.read_text()
            record = json.loads(contents)
        else:
            record = 0

        return record

    def write_high_score_to_file(self):
        """Write high_score to the file"""
        base_dir = Path(__file__).parent
        path = base_dir / "save.json"
        contents = json.dumps(self.score)
        path.write_text(contents)
