from datetime import datetime, timedelta
from functools import wraps
from pathlib import Path
import json

def cache(expiration_delta: timedelta):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_dir = Path("./cache/").mkdir(parents=True, exist_ok=True)
            cache_key = Path(args[1].replace('/', '_').replace(':', ''))
            cache_file_path: Path = cache_dir / cache_key
            
            # Try to load from cache
            if cache_file_path.exists():
                with open(cache_file_path, "r") as file:
                    cache_data = json.load(file)
                    cache_time = datetime.fromisoformat(cache_data["timestamp"])
                    if datetime.now() - cache_time < expiration_delta:
                        return cache_data["data"]
            
            # Make the API call and cache the result
            result = func(*args, **kwargs)
            cache_data = {
                "timestamp": datetime.now().isoformat(),
                "data": result
            }
            
            with open(cache_file_path, "w") as file:
                json.dump(cache_data, file)
            return result
        return wrapper
    return decorator
