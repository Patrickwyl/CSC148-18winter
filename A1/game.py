"""
Create a class Game for general games.
"""
from typing import Any
from current_state import CurrentState
from current_state import SubtractState
from current_state import ChopstickState


class Game:
    """Represent a class Game for genral games.

    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new game.
        >>> g = Game(True)
        >>> g.current_state.is_p1_turn
        True

        """
        self.current_state = CurrentState(is_p1_turn)

    def __str__(self) -> str:
        """Return the current basic state of the game.

        """
        raise NotImplementedError("Override this!")

    def get_instructions(self) -> str:
        """Return the instructions of the game.

        """
        raise NotImplementedError("Override this!")

    def is_over(self, current_state) -> bool:
        """Return True if the game is over.


        """
        raise NotImplementedError("Override this!")

    def is_winner(self, player: str) -> bool:
        """Return True if the player is the winner.


        """
        raise NotImplementedError("Override this!")

    def str_to_move(self, move_to_make: Any) -> Any:
        """Change the type of move_to_make.


        """
        raise NotImplementedError("Override this!")


class SubtractSqureGame(Game):
    """Reprsent a new subclass for game subtract square.

    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new subtract square game.

        """
        Game.__init__(self, is_p1_turn)
        current_num = int(input("Choose a non-negative number:"))
        self.current_state = SubtractState(is_p1_turn, current_num)

    def __str__(self) -> str:
        """Return the current total number.

        """
        return "The current number is: " + str(self.current_state.current_num)

    def __eq__(self, other) -> bool:
        """Return True if two games are the same.

        """
        return (isinstance(other, SubtractSqureGame)
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """Return the instructions of the game subtact square.

        """
        return "1. A positive whole number is randomly chosen as the\
         starting value by some neutral entity. 2.The player whose turn it is\
          chooses some square of a positive whole number (such as 1, 4, 9) to\
          subtract from the value, provided the chosen square is not larger.\
           After subtracting, we have a new value and the next player chooses\
            a square to subtract from it. 3.Play continues to alternate\
             between the two players until no moves are possible. Whoever is\
              about to play at that point loses! 4.Now Player B touches one\
               hand to one of Player A's hands, and the distribution of \
               fingers proceeds as above, including the possibility of a\
               dead hand. 5.Play repeats steps 2{4 until some player has two\
               deadhands, thus losing."

    def is_over(self, current_state) -> bool:
        """Return True if the game is over.

        """
        return self.current_state.current_num == 0

    def is_winner(self, player: str) -> bool:
        """Return True if the player is the winner.

        """
        if self.is_over(self.current_state):
            if (not self.current_state.is_p1_turn) and player == "p1":
                return True
            if self.current_state.is_p1_turn and player == "p2":
                return True
        return False

    def str_to_move(self, move_to_make: str) -> int:
        """Change type of move_to_make to integer.

        """
        return int(move_to_make)


class ChopsticksGame(Game):
    """Create a new subclass for game chopstciks.

    """

    def __init__(self, is_p1_turn: bool) -> None:
        """Initialize a new chopstick game.
        >>> c = ChopsticksGame(True)
        >>> c.current_state.is_p1_turn
        True
        >>> c.current_state == ChopstickState(True,1 , 1, 1, 1)
        True

        """
        Game.__init__(self, is_p1_turn)
        p1_left = 1
        p1_right = 1
        p2_left = 1
        p2_right = 1
        self.current_state = ChopstickState(is_p1_turn, p1_left,
                                            p1_right, p2_left, p2_right)

    def __str__(self) -> str:
        """Return the turn.
        >>> c = ChopsticksGame(True)
        >>> c.__str__()
        'p1'
        >>> c = ChopsticksGame(False)
        >>> c.__str__()
        'p2'

        """
        if self.current_state.is_p1_turn:
            return "p1"
        return "p2"

    def __eq__(self, other) -> bool:
        """Return True if the two games are the same.
        >>> c = ChopsticksGame(True)
        >>> d = ChopsticksGame(True)
        >>> c.current_state = d.current_state
        >>> c.__eq__(d)
        True

        """
        return (isinstance(other, ChopsticksGame)
                and self.current_state == other.current_state)

    def get_instructions(self) -> str:
        """Return the instructions of the game chopsticks.
        >>> c = ChopsticksGame(True)
        >>> c.get_instructions()
        "1.Each of two players begins with one finger pointed up on\
         each of their hands. 2.Player A touches one hand to one of Player \
         B's hands, increasing the number of fingers pointing up on Player B's\
          hand by the number on Player A's hand. The number pointing up on\
           Player A's hand remains the same. 3.If Player B now has fingers\
            up, that hand becomes or unplayable. If the number of fingers\
             should exceed five, subtract five from the sum."

        """
        return "1.Each of two players begins with one finger pointed up on\
         each of their hands. 2.Player A touches one hand to one of Player \
         B's hands, increasing the number of fingers pointing up on Player B's\
          hand by the number on Player A's hand. The number pointing up on\
           Player A's hand remains the same. 3.If Player B now has fingers\
            up, that hand becomes or unplayable. If the number of fingers\
             should exceed five, subtract five from the sum."

    def is_over(self, current_state) -> bool:
        """Return True if the game is over.
        >>> S = ChopsticksGame(True)
        >>> c = ChopstickState(True, 1, 1, 3, 2)
        >>> S.is_over(c)
        False


        """
        if current_state.get_possible_moves() == []:
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """Return True if the player is the winner.
        >>> c = ChopsticksGame(True)
        >>> player = "p1"
        >>> c.is_winner("p1")
        False

        """
        if self.is_over(self.current_state):
            if (not self.current_state.is_p1_turn) and player == "p1":
                return True
            if self.current_state.is_p1_turn and player == "p2":
                return True
        return False

    def str_to_move(self, move_to_make: str) -> str:
        """Change the type of move_to_make to str.
        >>> c = ChopsticksGame(True)
        >>> c.str_to_move("lr")
        'lr'
        >>> d = ChopsticksGame(True)
        >>> d.str_to_move("rr")
        'rr'

        """
        return str(move_to_make)


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
