import logging
import os

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)


def get_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Exported loggers
generator_logger = get_logger("generator", "logs/generators.log")
