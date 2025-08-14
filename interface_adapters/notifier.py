from dataclasses import dataclass
from pathlib import Path
from entities.observer import Observer

class ConsoleNotifier(Observer):
    def update(self, message: str):
        print(f"[NOTIFICATION]: {message}")

@dataclass
class LoggerNotifier(Observer):
    filepath: str = "events.log"
    def update(self, message: str):
        with open(self.filepath, 'a') as f:
            f.write(f"{message}\n")
