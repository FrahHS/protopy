import logging

log_format = '[%(levelname)s] %(message)s'

LOG_COLORS = {
    'DEBUG': '\033[94m',  # Blu
    'INFO': '\033[92m',   # Verde
    'WARNING': '\033[93m',  # Giallo
    'ERROR': '\033[91m',   # Rosso
    'CRITICAL': '\033[91m',  # Rosso
    'RESET': '\033[0m'    # Reset
}

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_level = record.levelname
        log_color = LOG_COLORS.get(log_level, LOG_COLORS['RESET'])
        log_format = f"{log_color}{super().format(record)}{LOG_COLORS['RESET']}"
        return log_format

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

console_formatter = ColoredFormatter(log_format)
console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)
