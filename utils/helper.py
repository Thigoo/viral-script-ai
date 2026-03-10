def estimate_duration_from_text(script: str) -> int:
    words = script.split()
    words_count = len(words)
    duration_seconds = words_count / 2.7
    return int(duration_seconds)

def generate_srt(script: str, total_duration: int, speaker: str = None):

    blocks = [b.strip() for b in script.split("\n\n") if b.strip()]

    total_chars = sum(len(b) for b in blocks)

    def format_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    srt_content = ""
    current_time = 0

    for i, block in enumerate(blocks, start=1):

        proportion = len(block) / total_chars
        block_duration = total_duration * proportion

        start_time = format_time(current_time)
        end_time = format_time(current_time + block_duration)

        if speaker:
            block_text = f"{speaker}:\n{block}"
        else:
            block_text = block

        srt_content += f"{i}\n"
        srt_content += f"{start_time} --> {end_time}\n"
        srt_content += f"{block_text}\n\n"

        current_time += block_duration

    return srt_content
