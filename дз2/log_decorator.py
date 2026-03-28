from datetime import datetime
from functools import wraps
from pathlib import Path


def function_logger(log_path):
    log_file = Path(log_path)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            with log_file.open("a", encoding="utf-8") as target:
                target.write(f"{func.__name__}\n")
                target.write(f"{start_time:%Y-%m-%d %H:%M:%S}\n")
                target.write(f"{args if args else '-'}\n")
                target.write(f"{kwargs if kwargs else '-'}\n")
                target.write(f"{result if result is not None else '-'}\n")
                target.write(f"{end_time:%Y-%m-%d %H:%M:%S}\n")
                target.write(f"{duration:.6f}\n")

            return result

        return wrapper

    return decorator
