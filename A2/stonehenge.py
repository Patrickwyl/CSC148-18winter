"""
An implementation of a state for Stonehenge.
"""
from typing import Any
from copy import deepcopy
from game_state import GameState
from game import Game


class StonehengeState(GameState):
    """
    The state of a game at a certain point in time.
    """

    def __init__(self, is_p1_turn: bool, size: int,
                 left_leyline, ley_line,
                 right_leyline, is_finished: bool) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> print(a.p1_turn)
        True
        >>> print(a.size)
        1
        >>> print(a.left_leyline)
        [['@', 'A'], ['@', 'B', 'C']]
        >>> print(a.ley_line)
        [['@', 'A', 'B'], ['@', 'C']]
        >>> print(a.right_leyline)
        [['A', 'C', '@'], ['B', '@']]
        >>> print(a.is_finished)
        False
        """
        super().__init__(is_p1_turn)
        self.size = size
        self.is_finished = is_finished
        self.left_leyline = deepcopy(left_leyline)
        self.ley_line = deepcopy(ley_line)
        self.right_leyline = deepcopy(right_leyline)
        self.graph = "Haven't drawn yet"
        self.draw_graph()

    def draw_graph(self) -> None:
        """
        Draw a graph for the class Stonehenge state.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.draw_graph()
        >>> a.graph == a.__str__()
        True
        """
        if self.size == 1:
            self.graph = (
                """
      {}   {}
     /   / 
{} - {} - {}  
     \\ / \\ 
  {} - {}   {}
       \\   
        {}   """).format(self.left_leyline[0][0],
                         self.left_leyline[1][0],
                         self.ley_line[0][0],
                         self.ley_line[0][1],
                         self.ley_line[0][2],
                         self.ley_line[1][0],
                         self.ley_line[1][1],
                         self.right_leyline[-1][-1],
                         self.right_leyline[-2][-1])
        if self.size == 2:
            self.graph = (
                """
        {}   {}  
       /   /   
  {} - {} - {}   {}
     / \\ / \\ / 
{} - {} - {} - {}  
     \\ / \\ / \\  
  {} - {} - {}   {}
       \\   \\   
        {}   {}   """).format(self.left_leyline[0][0],
                              self.left_leyline[1][0],
                              self.ley_line[0][0],
                              self.ley_line[0][1],
                              self.ley_line[0][2],
                              self.left_leyline[2][0],
                              self.ley_line[1][0],
                              self.ley_line[1][1],
                              self.ley_line[1][2],
                              self.ley_line[1][3],
                              self.ley_line[2][0],
                              self.ley_line[2][1],
                              self.ley_line[2][2],
                              self.right_leyline[-1][-1],
                              self.right_leyline[-3][-1],
                              self.right_leyline[-2][-1])
        if self.size == 3:
            self.graph = (
                """
          {}   {}    
         /   /     
    {} - {} - {}   {}  
       / \\ / \\ /   
  {} - {} - {} - {}   {}
     / \\ / \\ / \\ / 
{} - {} - {} - {} - {}  
     \\ / \\ / \\ / \\ 
  {} - {} - {} - {}   {}
       \\   \\   \\   
        {}   {}   {} 
                   """).format(self.left_leyline[0][0],
                               self.left_leyline[1][0],
                               self.ley_line[0][0],
                               self.ley_line[0][1],
                               self.ley_line[0][2],
                               self.left_leyline[2][0],
                               self.ley_line[1][0],
                               self.ley_line[1][1],
                               self.ley_line[1][2],
                               self.ley_line[1][3],
                               self.left_leyline[3][0],
                               self.ley_line[2][0],
                               self.ley_line[2][1],
                               self.ley_line[2][2],
                               self.ley_line[2][3],
                               self.ley_line[2][4],
                               self.ley_line[3][0],
                               self.ley_line[3][1],
                               self.ley_line[3][2],
                               self.ley_line[3][3],
                               self.right_leyline[-1][-1],
                               self.right_leyline[-4][-1],
                               self.right_leyline[-3][-1],
                               self.right_leyline[-2][-1])
        if self.size == 4:
            self.graph = (
                """
            {}   {}      
           /   /       
      {} - {} - {}   {}    
         / \\ / \\ /     
    {} - {} - {} - {}   {}  
       / \\ / \\ / \\ /   
  {} - {} - {} - {} - {}   {}
     / \\ / \\ / \\ / \\ / 
{} - {} - {} - {} - {} - {}  
     \\ / \\ / \\ / \\ / \\ 
  {} - {} - {} - {} - {}   {}
       \\   \\   \\   \\   
        {}   {}   {}   {}   """).format(self.left_leyline[0][0],
                                        self.left_leyline[1][0],
                                        self.ley_line[0][0],
                                        self.ley_line[0][1],
                                        self.ley_line[0][2],
                                        self.left_leyline[2][0],
                                        self.ley_line[1][0],
                                        self.ley_line[1][1],
                                        self.ley_line[1][2],
                                        self.ley_line[1][3],
                                        self.left_leyline[3][0],
                                        self.ley_line[2][0],
                                        self.ley_line[2][1],
                                        self.ley_line[2][2],
                                        self.ley_line[2][3],
                                        self.ley_line[2][4],
                                        self.left_leyline[4][0],
                                        self.ley_line[3][0],
                                        self.ley_line[3][1],
                                        self.ley_line[3][2],
                                        self.ley_line[3][3],
                                        self.ley_line[3][4],
                                        self.ley_line[3][5],
                                        self.ley_line[4][0],
                                        self.ley_line[4][1],
                                        self.ley_line[4][2],
                                        self.ley_line[4][3],
                                        self.ley_line[4][4],
                                        self.right_leyline[-1][-1],
                                        self.right_leyline[-5][-1],
                                        self.right_leyline[-4][-1],
                                        self.right_leyline[-3][-1],
                                        self.right_leyline[-2][-1])
        if self.size == 5:
            self.graph = (
                """
              {}   {}        
             /   /         
        {} - {} - {}   {}      
           / \\ / \\ /       
      {} - {} - {} - {}   {}    
         / \\ / \\ / \\ /     
    {} - {} - {} - {} - {}   {}  
       / \\ / \\ / \\ / \\ /   
  {} - {} - {} - {} - {} - {}   {}
     / \\ / \\ / \\ / \\ / \\ / 
{} - {} - {} - {} - {} - {} - {}  
     \\ / \\ / \\ / \\ / \\ / \\ 
  {} - {} - {} - {} - {} - {}   {}
       \\   \\   \\   \\   \\   
        {}   {}   {}   {}   {}   """).format(self.left_leyline[0][0],
                                             self.left_leyline[1][0],
                                             self.ley_line[0][0],
                                             self.ley_line[0][1],
                                             self.ley_line[0][2],
                                             self.left_leyline[2][0],
                                             self.ley_line[1][0],
                                             self.ley_line[1][1],
                                             self.ley_line[1][2],
                                             self.ley_line[1][3],
                                             self.left_leyline[3][0],
                                             self.ley_line[2][0],
                                             self.ley_line[2][1],
                                             self.ley_line[2][2],
                                             self.ley_line[2][3],
                                             self.ley_line[2][4],
                                             self.left_leyline[4][0],
                                             self.ley_line[3][0],
                                             self.ley_line[3][1],
                                             self.ley_line[3][2],
                                             self.ley_line[3][3],
                                             self.ley_line[3][4],
                                             self.ley_line[3][5],
                                             self.left_leyline[5][0],
                                             self.ley_line[4][0],
                                             self.ley_line[4][1],
                                             self.ley_line[4][2],
                                             self.ley_line[4][3],
                                             self.ley_line[4][4],
                                             self.ley_line[4][5],
                                             self.ley_line[4][6],
                                             self.ley_line[5][0],
                                             self.ley_line[5][1],
                                             self.ley_line[5][2],
                                             self.ley_line[5][3],
                                             self.ley_line[5][4],
                                             self.ley_line[5][5],
                                             self.right_leyline[-1][-1],
                                             self.right_leyline[-6][-1],
                                             self.right_leyline[-5][-1],
                                             self.right_leyline[-4][-1],
                                             self.right_leyline[-3][-1],
                                             self.right_leyline[-2][-1])

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> b = a.__str__()
        >>> c = a.graph
        >>> b == c
        True
        """
        return self.graph

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.get_possible_moves()
        ['A', 'B', 'C']
        """
        acc = []
        for sublist in self.ley_line:
            for item in sublist:
                if item in ['A', 'B', 'C', 'D', 'E', 'F',
                            'G', 'H', 'I', 'J', 'K', 'L',
                            'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X',
                            'Y', 'Z'] and not self.is_finished:
                    acc.append(item)
        return acc

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.get_current_player_name()
        'p1'
        >>> b = StonehengeState(False, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> b.get_current_player_name()
        'p2'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.make_move('A')
        False, 1, [[1, 1], ['@', 'B', 'C']], [[1, 1, 'B'], ['@', 'C']], [[1, 'C', 1], ['B', '@']], True
        """
        new_state = StonehengeState(not self.p1_turn, self.size,
                                    self.left_leyline,
                                    self.ley_line, self.right_leyline,
                                    self.is_finished)
        helper_change_value(new_state.ley_line, move, self.p1_turn)
        helper_change_value(new_state.left_leyline, move, self.p1_turn)
        helper_change_value(new_state.right_leyline, move, self.p1_turn)
        helper_change_marker(new_state.ley_line, 0, self.p1_turn)
        helper_change_marker(new_state.left_leyline, 0, self.p1_turn)
        helper_change_marker(new_state.right_leyline, -1, self.p1_turn)
        acc = helper_count_marker(new_state.ley_line,
                                  new_state.left_leyline,
                                  new_state.right_leyline)
        acc1 = acc[0]
        acc2 = acc[1]
        ley_lines = 3 * (self.size + 1)
        if acc1 >= (1 / 2 * ley_lines) or (acc2 >= 1 / 2 * ley_lines):
            new_state.is_finished = True
        new_state.draw_graph()
        return new_state

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.is_valid_move('A')
        True
        >>> a.is_valid_move('C')
        True
        >>> a.is_valid_move('D')
        False
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.__repr__()
        "True, 1, [['@', 'A'], ['@', 'B', 'C']], [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False"
        """
        return ("{}, {}, {}, {}, {}, {}"
                .format(self.p1_turn, self.size,
                        self.left_leyline,
                        self.ley_line, self.right_leyline, self.is_finished))

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        >>> a = StonehengeState(True, 1, [['@', 'A'], ['@', 'B', 'C']],\
        [['@', 'A', 'B'], ['@', 'C']], [['A', 'C', '@'], ['B', '@']], False)
        >>> a.rough_outcome()
        0
        """
        acc = helper_count_marker(self.ley_line,
                                  self.left_leyline, self.right_leyline)
        acc1 = acc[0]
        acc2 = acc[1]
        ley_lines = 3 * (self.size + 1)
        if self.p1_turn:
            if (acc2 + 1) >= (1 / 2 * ley_lines):
                return self.LOSE
            elif acc1 == acc2:
                return self.DRAW
            return self.WIN
        else:
            if (acc1 + 1) >= (1 / 2 * ley_lines):
                return self.LOSE
            elif acc1 == acc2:
                return self.DRAW
            return self.WIN


def helper_change_value(lst: Any, move: Any, p1: bool) -> None:
    """
    A helper function that changes the value for nake_move.
    >>> lst = [['@', 'A'], ['@', 'B', 'C']]
    >>> move = 'A'
    >>> p1 = True
    >>> helper_change_value(lst, move, p1)
    >>> lst
    [['@', 1], ['@', 'B', 'C']]
    """
    for sublist in lst:
        for i in range(len(sublist)):
            if move == sublist[i] and p1:
                sublist[i] = 1
            if move == sublist[i] and not p1:
                sublist[i] = 2


def helper_change_marker(lst: Any, index: int, p1: bool) -> None:
    """
    A helper function that changes the marker for make_move.
    >>> lst = [['@', 1], ['@', 'B', 'C']]
    >>> index = 0
    >>> p1 = True
    >>> helper_change_marker(lst, index, p1)
    >>> lst
    [[1, 1], ['@', 'B', 'C']]
    """
    for sublist in lst:
        acc1 = 0
        acc2 = 0
        for i in range(len(sublist)):
            if p1 and sublist[i] == 1:
                acc1 += 1
            if (not p1) and sublist[i] == 2:
                acc2 += 1
        if sublist[index] == '@':
            if acc1 >= ((len(sublist) - 1) * 1 / 2):
                sublist[index] = 1
            if acc2 >= ((len(sublist) - 1) * 1 / 2):
                sublist[index] = 2


def helper_count_marker(lst1: list, lst2: list, lst3: list) -> list:
    """
    A helper function that count the marker after changing '@'.
    >>> lst1 = [[1, 1], ['@', 'B', 'C']]
    >>> lst2 = [[1, 1, 'B'], ['@', 'C']]
    >>> lst3 = [[1, 'C', 1], ['B', '@']]
    >>> helper_count_marker(lst1, lst2, lst3)
    [3, 0]
    """
    acc1 = 0
    acc2 = 0
    for sublist in lst1:
        if sublist[0] == 1:
            acc1 += 1
        if sublist[0] == 2:
            acc2 += 1
    for sublist in lst2:
        if sublist[0] == 1:
            acc1 += 1
        if sublist[0] == 2:
            acc2 += 1
    for sublist in lst3:
        if sublist[-1] == 1:
            acc1 += 1
        if sublist[-1] == 2:
            acc2 += 1
    return [acc1, acc2]


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """
    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        size = int(input("Enter a side length of the borad: "))
        left_leyline = []
        ley_line = []
        right_leyline = []
        finished = False
        if size == 1:
            ley_line = [['@', 'A', 'B'], ['@', 'C']]
            left_leyline = [['@', 'A'], ['@', 'B', 'C']]
            right_leyline = [['A', 'C', '@'], ['B', '@']]
        if size == 2:
            ley_line = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G']]
            left_leyline = [['@', 'A', 'C'],
                            ['@', 'B', 'D', 'F'],
                            ['@', 'E', 'G']]
            right_leyline = [['C', 'F', '@'],
                             ['A', 'D', 'G', '@'],
                             ['B', 'E', '@']]
        if size == 3:
            ley_line = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L']]
            left_leyline = [['@', 'A', 'C', 'F'],
                            ['@', 'B', 'D', 'G', 'J'],
                            ['@', 'E', 'H', 'K'],
                            ['@', 'I', 'L']]
            right_leyline = [['F', 'J', '@'],
                             ['C', 'G', 'K', '@'],
                             ['A', 'D', 'H', 'L', '@'],
                             ['B', 'E', 'I', '@']]
        if size == 4:
            ley_line = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L', 'M', 'N'],
                        ['@', 'O', 'P', 'Q', 'R']]
            left_leyline = [['@', 'A', 'C', 'F', 'J'],
                            ['@', 'B', 'D', 'G', 'K', 'O'],
                            ['@', 'E', 'H', 'L', 'P'],
                            ['@', 'I', 'M', 'Q'],
                            ['@', 'N', 'R']]
            right_leyline = [['J', 'O', '@'],
                             ['F', 'K', 'P', '@'],
                             ['C', 'G', 'L', 'Q', '@'],
                             ['A', 'D', 'H', 'M', 'R', '@'],
                             ['B', 'E', 'I', 'N', '@']]
        if size == 5:
            ley_line = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L', 'M', 'N'],
                        ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                        ['@', 'U', 'V', 'W', 'X', 'Y']]
            left_leyline = [['@', 'A', 'C', 'F', 'J', 'O'],
                            ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                            ['@', 'E', 'H', 'L', 'Q', 'V'],
                            ['@', 'I', 'M', 'R', 'W'],
                            ['@', 'N', 'S', 'X'],
                            ['@', 'T', 'Y']]
            right_leyline = [['O', 'U', '@'],
                             ['J', 'P', 'V', '@'],
                             ['F', 'K', 'Q', 'W', '@'],
                             ['C', 'G', 'L', 'R', 'X', '@'],
                             ['A', 'D', 'H', 'M', 'S', 'Y', '@'],
                             ['B', 'E', 'I', 'N', 'T', '@']]
        self.current_state = StonehengeState(p1_starts, size,
                                             left_leyline,
                                             ley_line, right_leyline, finished)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        return ("Players take turns claiming cells. "
                "When a player captures at least half of the"
                "cells in a ley-line, "
                "then the player captures that ley-line. "
                "The first player to capture at least half of "
                "the ley-lines is the winner. "
                "A ley-line, once claimed, cannot be taken "
                "by the other player.")

    def is_over(self, state: StonehengeState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        return state.is_finished

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.
        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return str(string)


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
