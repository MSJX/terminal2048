# -*- coding: UTF-8 -*-
"""
Keyboard events processing
"""

# Space Bar key to pause the game
SPACE = 32

# Vim keys
K, J, L, H = 107, 106, 108, 104

try:
    import termios
except ImportError:
    # Windows
    import msvcrt

    UP, DOWN, RIGHT, LEFT = 72, 80, 77, 75

    __key_aliases = {
        H: LEFT,
        J: RIGHT,
        K: UP,
        L: DOWN
    }


    def getKey():
        """return a key pressed by the user"""
        while True:
            if msvcrt.kbhit():
                a = ord(msvcrt.getch())
                return __key_aliases.get(a, a)

else:
    # Linux/OS

    import sys
    import tty

    __fd = sys.stdin.fileno()
    __old = termios.tcgetattr(__fd)

    # Arrow keys
    # they are preceded by 27 and 91, hence the double
    UP, DOWN, RIGHT, LEFT = 65, 66, 67, 68

    __key_aliases = {
        K: UP,
        J: DOWN,
        L: RIGHT,
        H: LEFT,
    }


    def __getKey():
        """return a key pressed by the user"""
        try:
            tty.setcbreak(sys.stdin.fileno())
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            ch = sys.stdin.read(1)
            return ord(ch) if ch else None
        finally:
            termios.tcsetattr(__fd, termios.TCSADRAIN, __old)


    def getKey():
        """
        same as __getKey, but handle arrow keys
        """
        k = __getKey()
        if k == 27:
            k = __getKey()
            if k == 91:
                k = __getKey()

        return __key_aliases.get(k, k)

# legacy support
getArrowKey = getKey
