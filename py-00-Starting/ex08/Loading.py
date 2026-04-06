import os


def format_time(seconds):
    """Format seconds as HH:MM:SS or MM:SS"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def format_speed(it_per_sec):
    """Format speed as it/s or s/it"""
    if it_per_sec >= 1:
        return f"{it_per_sec:.2f}it/s"
    elif it_per_sec > 0:
        sec_per_it = 1 / it_per_sec
        return f"{sec_per_it:.2f}s/it"
    else:
        return "0.00it/s"


def calculate_bar(current, total, bar_length):
    """Calculate the progress bar string"""
    filled = int(bar_length * current / total)
    return '█' * filled + '░' * (bar_length - filled)


def ft_tqdm(lst: range):
    '''
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    '''
    total = len(lst)
    start_time = os.times()[4]

    for i, item in enumerate(lst):
        current = i + 1
        percentage = (current / total) * 100

        # Calculate times and speed
        elapsed_time = os.times()[4] - start_time
        if elapsed_time > 0:
            it_per_sec = current / elapsed_time
        else:
            it_per_sec = 0

        # Calculate remaining time
        if it_per_sec > 0 and current < total:
            remaining_items = total - current
            estimated_remaining = remaining_items / it_per_sec
        else:
            estimated_remaining = 0

        # Format strings
        elapsed_str = format_time(elapsed_time)
        remaining_str = format_time(estimated_remaining)
        speed_str = format_speed(it_per_sec)

        # Build display
        terminal_width = os.get_terminal_size().columns
        prefix = f"{percentage:3.0f}%|"
        suffix = f"| {current}/{total} [{elapsed_str}<{remaining_str}," + \
            f" {speed_str}]"
        bar_length = terminal_width - len(prefix) - len(suffix)

        if bar_length < 1:
            bar_length = 10

        bar = calculate_bar(current, total, bar_length)

        # Print progress
        print(f"\r{prefix}{bar}{suffix}", end='', flush=True)

        yield item
