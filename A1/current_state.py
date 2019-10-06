"""
Design a class representing the state of the game.
"""

from typing import Any


class CurrentState:
    """Represent a superclass for the current state.

    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Create a superclass, which represents the current state.
        >>> c = CurrentState(True)
        >>> c.is_p1_turn
        True
        >>> d = CurrentState(False)
        >>> d.is_p1_turn
        False

        """
        self.is_p1_turn = is_p1_turn

    def __str__(self) -> str:
        """Return the basic state of the game.
        >>> c = CurrentState(True)
        >>> c.__str__()
        'Game continues, waiting for next player!'

        """
        return "Game continues, waiting for next player!"

    def __eq__(self, other) -> bool:
        """Return True if the two state is the same.
        >>> c = CurrentState(True)
        >>> d = CurrentState(True)
        >>> c.__eq__(d)
        True

        """
        if isinstance(other, CurrentState):
            return self.is_p1_turn == other.is_p1_turn
        return False

    def get_current_player_name(self) -> str:
        """Return the current player's name.
        >>> c = CurrentState(True)
        >>> c.is_p1_turn = True
        >>> c.get_current_player_name()
        'p1'

        """
        if self.is_p1_turn:
            return 'p1'
        return 'p2'

    def get_possible_moves(self) -> list:
        """Return all the possible moves.

        """
        raise NotImplementedError("Override this!")

    def make_move(self, move_to_make: Any) -> None:
        """Run the game for one time.

        """
        raise NotImplementedError("Override this!")

    def is_valid_move(self, move_to_make: Any) -> bool:
        """Return True if the move is valid.

        """
        raise NotImplementedError("Override this!")


class SubtractState(CurrentState):
    """Create a new subclass for game subtract square.

    """
    def __init__(self, is_p1_turn: bool, current_num: int) -> None:
        """Create a new subclass for game subtract square.
        >>> s = SubtractState(True, 9)
        >>> s.current_num
        9
        >>> s.is_p1_turn
        True

        """
        CurrentState.__init__(self, is_p1_turn)
        self.current_num = current_num

    def __str__(self) -> str:
        """Return the current total number.
        >>> s = SubtractState(True, 8)
        >>> s.__str__()
        'The current number is:8'
        >>> s = SubtractState(False, 20)
        >>> s.__str__()
        'The current number is:20'

        """
        return "The current number is:" + str(self.current_num)

    def __eq__(self, other) -> bool:
        """Return True if the two state is the same.
        >>> s = SubtractState(True, 8)
        >>> t = SubtractState(True, 8)
        >>> s.__eq__(t)
        True
        >>> a = SubtractState(False, 8)
        >>> s.__eq__(a)
        False

        """
        if isinstance(other, SubtractState):
            return (self.is_p1_turn == other.is_p1_turn
                    and self.current_num == other.current_num)
        return False

    def get_possible_moves(self) -> list:
        """Return a list of all the possible moves.
        >>> s = SubtractState(True, 8)
        >>> s.get_possible_moves()
        [1, 4]
        >>> t = SubtractState(True, 20)
        >>> t.get_possible_moves()
        [1, 4, 9, 16]


        """
        moves = []
        for num in range(1, self.current_num + 1):
            if self.is_valid_move(num):
                moves.append(num)
        return moves

    def make_move(self, move_to_make: int) -> Any:
        """Run the game for one time.
        >>> s = SubtractState(True, 8)
        >>> move_to_make = 4
        >>> s.make_move(move_to_make) == SubtractState(False, 4)
        True


        """
        s = SubtractState(self.is_p1_turn, self.current_num)
        s.current_num = self.current_num - move_to_make
        if self.is_p1_turn:
            s.is_p1_turn = False
        else:
            s.is_p1_turn = True
        return s

    def is_valid_move(self, move_to_make: int) -> bool:
        """Return True if the move is valid.
        >>> s = SubtractState(True, 8)
        >>> move_to_make = 4
        >>> s.is_valid_move(move_to_make)
        True

        """
        if move_to_make is None:
            return False
        root = move_to_make ** 0.5
        if isinstance(move_to_make, int):
            return (0 < move_to_make <= self.current_num
                    and int(root) ** 2 == move_to_make)
        return False


class ChopstickState(CurrentState):
    """Create a new subclass for game chopsticks.

    """
    def __init__(self, is_p1_turn: bool, p1_left: int, p1_right: int,
                 p2_left: int, p2_right: int) -> None:
        """Create a new subclass for game chopsticks.
        >>> c = ChopstickState(True, 1, 2, 3, 4)
        >>> c.p1_left
        1
        >>> c.p1_right
        2
        >>> c.p2_left
        3
        >>> c.p2_right
        4


        """
        CurrentState.__init__(self, is_p1_turn)
        self.p1_left = p1_left
        self.p1_right = p1_right
        self.p2_left = p2_left
        self.p2_right = p2_right

    def __str__(self) -> str:
        """Return the basic state of both hands of each player.
        >>> c = ChopstickState(True, 1, 2, 3, 4)
        >>> c.__str__()
        'p1: 1 - 2, p2: 3 - 4'
        >>> d = ChopstickState(True, 3, 2, 1, 4)
        >>> d.__str__()
        'p1: 3 - 2, p2: 1 - 4'

        """
        return "p1: {} - {}, p2: {} - {}"\
            .format(self.p1_left, self.p1_right, self.p2_left, self.p2_right)

    def __eq__(self, other) -> bool:
        """Return True if the two state is the same.
        >>> c = ChopstickState(True, 1, 2, 3, 4)
        >>> d = ChopstickState(True, 3, 2, 1, 4)
        >>> c.__eq__(d)
        False

        """
        return (self.p1_left == other.p1_left
                and isinstance(other, ChopstickState)
                and self.p1_right == other.p1_right
                and self.p2_left == other.p2_left
                and self.p2_right == other.p2_right
                and self.is_p1_turn == other.is_p1_turn)

    def get_possible_moves(self) -> list:
        """Return a list of all the possible moves.
        >>> c = ChopstickState(True, 1, 1, 1, 1)
        >>> c.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> d = ChopstickState(True, 3, 2, 1, 4)
        >>> d.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']

        """
        template = []
        if self.is_p1_turn:
            if self.p1_left != 0:
                if self.p2_left != 0:
                    template.append("ll")
                if self.p2_right != 0:
                    template.append("lr")
            if self.p1_right != 0:
                if self.p2_left != 0:
                    template.append("rl")
                if self.p2_right != 0:
                    template.append("rr")
        if self.is_p1_turn is False:
            if self.p2_left != 0:
                if self.p1_left != 0:
                    template.append("ll")
                if self.p1_right != 0:
                    template.append("lr")
            if self.p2_right != 0:
                if self.p1_left != 0:
                    template.append("rl")
                if self.p1_right != 0:
                    template.append("rr")
        return template

    def make_move(self, move_to_make: str) -> Any:
        """Run the game for one time.
        >>> c = ChopstickState(True, 1, 1, 1, 1)
        >>> move_to_make = "lr"
        >>> c.make_move(move_to_make) == ChopstickState(False, 1, 1, 1, 2)
        True


        """
        c = ChopstickState(self.is_p1_turn, self.p1_left, self.p1_right,
                           self.p2_left, self.p2_right)
        if self.is_p1_turn:
            c.is_p1_turn = False
            if move_to_make == "ll":
                c.p2_left = self.p2_left + self.p1_left
                if c.p2_left >= 5:
                    c.p2_left -= 5
            if move_to_make == "lr":
                c.p2_right = self.p2_right + self.p1_left
                if c.p2_right >= 5:
                    c.p2_right -= 5
            if move_to_make == "rl":
                c.p2_left = self.p2_left + self.p1_right
                if c.p2_left >= 5:
                    c.p2_left -= 5
            if move_to_make == "rr":
                c.p2_right = self.p2_right + self.p1_right
                if c.p2_right >= 5:
                    c.p2_right -= 5
        elif self.is_p1_turn is False:
            c.is_p1_turn = True
            if move_to_make == "ll":
                c.p1_left = self.p1_left + self.p2_left
                if c.p1_left >= 5:
                    c.p1_left -= 5
            if move_to_make == "lr":
                c.p1_right = self.p1_right + self.p2_left
                if c.p1_right >= 5:
                    c.p1_right -= 5
            if move_to_make == "rl":
                c.p1_left = self.p1_left + self.p2_right
                if c.p1_left >= 5:
                    c.p1_left -= 5
            if move_to_make == "rr":
                c.p1_right = self.p1_right + self.p2_right
                if c.p1_right >= 5:
                    c.p1_right -= 5
        return c

    def is_valid_move(self, move_to_make: str) -> bool:
        """Return True if the move is valid.
        >>> c = ChopstickState(True, 1, 1, 1, 1)
        >>> move_to_make = "lr"
        >>> c.is_valid_move(move_to_make)
        True

        """
        if self.p1_left == 5:
            self.p1_left = 0
        if self.p2_left == 5:
            self.p2_left = 0
        if self.p1_right == 5:
            self.p1_right = 0
        if self.p2_right == 5:
            self.p2_right = 0

        if move_to_make is None:
            return False
        if self.is_p1_turn:
            if move_to_make == "ll":
                return self.p1_left != 0 and self.p2_left != 0
            elif move_to_make == "lr":
                return self.p1_left != 0 and self.p2_right != 0
            elif move_to_make == "rl":
                return self.p1_right != 0 and self.p2_left != 0
            elif move_to_make == "rr":
                return self.p1_right != 0 and self.p2_right != 0
            return False
        if self.is_p1_turn is False:
            if move_to_make == "ll":
                return self.p2_left != 0 and self.p1_left != 0
            elif move_to_make == "lr":
                return self.p2_left != 0 and self.p1_right != 0
            elif move_to_make == "rl":
                return self.p2_right != 0 and self.p1_left != 0
            elif move_to_make == "rr":
                return self.p2_right != 0 and self.p1_right != 0
            return False


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
