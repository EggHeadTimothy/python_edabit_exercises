"""
The Snake - Area Filling by Timothy Eden
Date Last Modified: September 13, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
"""


def snakefill(n):
    """
    The logic behind this is to start the length of the snake at 1, and continue to double that number until it exceeds
    the screen size (which is calculated through n * n). The variable reps is an accumulator which increments by 1 each
    time the snake is able to double in size.
    """
    screen_size = n * n
    snake = 1
    snake_alive = True
    reps = 0
    while snake_alive:
        snake = snake * 2
        if snake <= screen_size:
            reps += 1
        else:
            snake_alive = False
    return reps


def main():
    assert snakefill(3) == 3
    assert snakefill(6) == 5
    assert snakefill(24) == 9
    assert snakefill(8) == 6
    assert snakefill(18) == 8
    assert snakefill(555) == 18
    assert snakefill(2) == 2
    assert snakefill(1) == 0
    assert snakefill(900) == 19


if __name__ == '__main__':
    main()
