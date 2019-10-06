"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
import random
from game import Game
from game_state import GameState

# TODO: Adjust the type annotation as needed.


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value: GameState, children=None, score=0) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.children = children[:] if children is not None else []
        self.score = score


class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contents = []

    def add(self, obj: object) -> None:
        """
        Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(7)
        """
        self._contents.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(7)
        >>> s.is_empty()
        False
        """
        return len(self._contents) == 0


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move

# TODO: Implement a recursive version of the minimax strategy.


def recursive_minimax(game: Game) -> Any:
    """
    Return a move for game with a recursive version of the minimax strategy.
    """
    moves = game.current_state.get_possible_moves()
    states = []
    scores = []
    for move in moves:
        states.append(game.current_state.make_move(move))
    for state in states:
        scores.append(helper_get_score(game, state))
    if -1 in scores:
        return moves[scores.index(-1)]
    return random.choice(scores)


def helper_get_score(game: Game, current_state: Any) -> int:
    """
    Return the score of the state.
    """
    # Basecase: When the game is over.
    if game.is_over(current_state):
        if game.is_winner(game.current_state.get_current_player_name()):
            return 1
        if not game.is_winner(game.current_state.get_current_player_name()):
            return -1
        return 0
    # Recursive Step
    states = []
    scores = []
    moves = current_state.get_possible_moves()
    for move in moves:
        states.append(current_state.make_move(move))
    for new_state in states:
        scores.append(helper_get_score(game, new_state) * (-1))
    return max(scores)

# TODO: Implement an iterative version of the minimax strategy.


def iterative_minimax(game: Game) -> Any:
    """
    Return a move for game with a iterative version of the minimax strategy.
    """
    s = Stack()
    node = Tree(game.current_state)
    s.add(node)
    acc = []
    while not s.is_empty():
        temp = s.remove()
        if game.is_over(temp.value):
            original_state = game.current_state
            game.current_state = temp.value
            if game.is_winner(temp.value.get_current_player_name()):
                temp.score = -1
            else:
                temp.score = 1
            game.current_state = original_state
        else:
            if not temp.children:
                helper_add_tree(temp)
                s.add(temp)
                helper_add_child(temp.children, s)
            else:
                scores = []
                helper_append_score(scores, temp.children)
                temp.score = min(scores)
                acc.append(temp)
    score = []
    for child in node.children:
        score.append(child.score)
    return node.value.get_possible_moves()[score.index(max(score))]


def helper_add_tree(temp) -> None:
    """
    Helper function for adding tree to a list of children.
    """
    for move in temp.value.get_possible_moves():
        temp.children.append(Tree(temp.value.make_move(move)))


def helper_add_child(children: list, s: Stack) -> None:
    """
    Helper function for adding each child to stack s.
    """
    for child in children:
        s.add(child)


def helper_append_score(lst: list, children: list) -> None:
    """
    Helper function for appending score of each child to a list.
    """
    for child in children:
        lst.append((-1) * child.score)


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
