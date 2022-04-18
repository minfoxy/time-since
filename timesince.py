import time
import math


def time_since(val: str) -> str:
    '''Returning since time'''
    sec = math.floor(time.time() - float(val))
    interval = sec // 31536000
    if interval > 1:
        return f'{math.floor(interval)} years ago'

    interval = sec / 2592000
    if interval > 1:
        return f'{math.floor(interval)} months ago'

    interval = sec / 86400
    if interval > 1:
        return f'{math.floor(interval)} days ago'

    interval = sec / 3600
    if interval > 1:
        return f'{math.floor(interval)} hours ago'

    interval = sec / 60
    if interval > 1:
        return f'{math.floor(interval)} minutes ago'

    return f'{math.floor(sec)} seconds ago'

