import numpy as np
import random
import cv2


def default_char_factory():
    return chr(random.choice(list(range(33, 126))))


def get_char(size, rate=2.3, char_factory=default_char_factory, func_show=None):
    w, h = size
    h = int(h / rate)
    result = ''
    for r in range(h):
        for c in range(w):
            show = True
            if callable(func_show):
                show = func_show(r, c)
            char = char_factory() if show else ' '
            result += char
        if r != h - 1:
            result += '\n'
    return result


def img2char(data, size, rate=2.3, char_factory=default_char_factory):
    w, h = size
    copy = data.copy()
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
    threshold, copy = cv2.threshold(copy, 127, 255, cv2.THRESH_BINARY)
    copy = cv2.resize(copy, (w, int(h / rate)))
    copy[copy <= 0] = 0
    copy[copy > 0] = 1
    copy = copy.astype(np.float)
    return get_char(size, rate, char_factory, func_show=lambda r, c: copy[r, c])


if __name__ == '__main__':
    print get_char((100, 100))
    import os

    os.system('clear')
