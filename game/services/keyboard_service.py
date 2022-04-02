import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        # Player controls, in order they are up, left, down, right, use ability
        # Player 1 controls
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D
        self._keys['q'] = pyray.KEY_Q

        # Player 2 controls
        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L
        self._keys['u'] = pyray.KEY_U

        # Player 3 controls
        self._keys['g'] = pyray.KEY_G
        self._keys['c'] = pyray.KEY_C
        self._keys['v'] = pyray.KEY_V
        self._keys['b'] = pyray.KEY_B
        self._keys['f'] = pyray.KEY_F

        # Player 4 controls
        # self._keys['0'] = pyray.KEY_0
        # self._keys['i'] = pyray.KEY_I
        # self._keys['o'] = pyray.KEY_O
        # self._keys['p'] = pyray.KEY_P
        # self._keys['9'] = pyray.KEY_9

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d, i, j, k, l, etc.)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d, i, j, k, l, etc.)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)