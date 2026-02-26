def estimate_duration_from_text(script: str) -> int:
    words = script.split()
    words_count = len(words)
    duration_seconds = words_count / 2.7
    return int(duration_seconds)
