banner = r"""
       __                _ ____          
      / /   ____  ____ _(_) __/_  _______
     / /   / __ \/ __ `/ / /_/ / / / ___/
    / /___/ /_/ / /_/ / / __/ /_/ / /    
   /_____/\____/\__, /_/_/  \__, /_/     
               /____/      /____/        
+------------------------------------------+
|                 Logifyr                  |
|                =========                 |
|        Author : Prashant Bhandari        |
+------------------------------------------+
| Logifyr is a Python class designed       |
| to facilitate logging with customizable  |
| timestamp formats and colored output.    |
+------------------------------------------+
"""

import os
import time
import inspect
from module.textartisan.text_artisan import TextArtisan
from datetime import datetime


class Logifyr(TextArtisan):

    # Default color mapping
    status_colors = {
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "DEBUG": "blue",
        # Add more statuses and corresponding colors as needed
    }

    def __init__(self, timestamp_format="%Y-%m-%d %H:%M:%S", color_enabled=True):
        """
        ===========================================================================================
        Initializes a Logifyr object with the specified timestamp format and colorization settings.
        ===========================================================================================

        Args:
        -----
        -> timestamp_format (str, optional): The format for the timestamp in log messages. Defaults to "%Y-%m-%d %H:%M:%S".
        -> color_enabled (bool, optional): Whether colorized output is enabled for log messages. Defaults to True.
        """
        super().__init__()
        self.timestamp_format = timestamp_format
        self.color_enabled = color_enabled

    def print_log(self, status, message):
        """
        ============================================================================================
        Prints a log message with the specified status, timestamp, message content, and line number.
        ============================================================================================

        Args:
        -----
        -> status (str): The status of the log message (e.g., "INFO", "WARNING", "ERROR").
        -> message (str): The content of the log message.
        """
        timestamp = datetime.now().strftime(self.timestamp_format)
        status_color = (
            self.status_colors.get(status.upper(), "white")
            if self.color_enabled
            else "white"
        )
        status_style = [self.COLORS[status_color.lower()]] if self.color_enabled else []
        frame_info = inspect.stack()[1]
        file_name = os.path.basename(
            frame_info.filename
        )  # Get just the filename without the path
        line_number = frame_info.lineno
        log_message = (
            f"[{timestamp}] "
            + self.decorate(status_style, f"[{status.upper()}]")
            + f" {message}"
            + f"({self.decorate([self.COLORS['green'], self.UNDERLINE], file_name)}: {self.decorate([self.COLORS['red']], str(line_number))})"
        )
        print(log_message)

    def set_status_color(self, status, color):
        """
        =========================================
        Sets the color for a specific log status.
        =========================================

        Args:
        -----
        -> status (str): The status for which to set the color.
        -> color (str): The color to set for the specified status.
        """
        self.status_colors[status.upper()] = color.lower()  # Convert color to lowercase for consistency

    def set_timestamp_format(self, timestamp_format):
        """
        ==================================================
        Sets the format for the timestamp in log messages.
        ==================================================

        Args:
        -----
        -> timestamp_format (str): The format string specifying how the timestamp should be formatted.
        """
        self.timestamp_format = timestamp_format

    def enable_color(self):
        """
        ========================
        Enable colorized output.
        ========================
        """
        self.color_enabled = True

    def disable_color(self):
        """
        =========================
        Disable colorized output.
        =========================
        """
        self.color_enabled = False


if __name__ == "__main__":
    print(TextArtisan.decorate([TextArtisan.BOLD, TextArtisan.COLORS["green"]], banner))
    logger = Logifyr()
    logger.print_log("INFO", "Initializing Logifyr 🚀.")
    time.sleep(1)
    logger.print_log("WARNING", "Just Joking 🎉.")
    time.sleep(2)
    logger.print_log("ERROR", "Logifyr Terminated ❌.")
