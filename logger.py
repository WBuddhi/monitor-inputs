import pandas as pd
from datetime import datetime
from pathlib import Path
from config import config


class Logger:
    def __init__(self, path_override=None):

        self.path = Path(
            path_override
            if path_override
            else config["LOG_FOLDER"] + config["LOG_NAME"]
        )
        self.path.parent.mkdir(
            parents=True, exist_ok=True
        ) if not self.path.parent.exists() else False
        self.logger_start_time = datetime.now()

    def update_log(self, MonitorMouse, MonitorKeyStrokes):

        self.mouse_distance = MonitorMouse.total_distance()
        self.keystroke_total = MonitorKeyStrokes.total_keystrokes()

        latest_entry = {
            "Timestamp": datetime.now(),
            "Logger start time": self.logger_start_time,
            "Mouse distance": self.mouse_distance,
            "Keystroke total": self.keystroke_total,
        }
        self._update_csv(latest_entry)

    def _update_csv(self, latest_entry):

        df_new_entry = pd.DataFrame([latest_entry])

        try:
            df = pd.read_csv(self.path.as_posix())
        except:
            df = pd.DataFrame()

        df = df.append(df_new_entry)
        df.to_csv(self.path.as_posix(), index=False)
