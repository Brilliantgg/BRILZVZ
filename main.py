import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("but ill", 0.2),
        ("pray for you", 0.2),
        ("all the time", 0.1),
        ("if i could be", 0.26),
        ("by your side", 0.2),
        ("ill give you all my live,my seasons ", 0.17),

    ]
    delays = [0.1, 7.0, 12.0, 14.0, 19.0, 23.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sing_song()
