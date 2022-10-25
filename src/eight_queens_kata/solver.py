from typing import List

from eight_queens_kata.models import Queen

CHESS_BOARD_POSITIONS = [
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
]
TARGET_NUMBER_OF_QUEENS_IN_SOLUTION = 8

class EightQueensSolver:

    def solve(self) -> List[Queen]:
        result = []

        if not self._can_solve_using_backtracking(result, CHESS_BOARD_POSITIONS):
            raise Exception('Could not find a solution to the problem')

        return result

    def _can_solve_using_backtracking(self, result: List[Queen], available_positions: List[str]) -> bool:

        if self._no_queen_can_capture_each_other(result) and len(result) == TARGET_NUMBER_OF_QUEENS_IN_SOLUTION:
            return True
        
        for next_position in available_positions:
            result.append(Queen(next_position))
            remaining_positions = self._calculate_possible_queen_positions(result, available_positions)

            if self._can_solve_using_backtracking(result, remaining_positions):
                return True

            result.pop()

        return False

    def _no_queen_can_capture_each_other(self, result: List[Queen]) -> bool:
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                queen_i = result[i]
                queen_j = result[j]

                if queen_i.can_capture(queen_j):
                    return False

        return True

    def _calculate_possible_queen_positions(self, result: List[Queen], available_positions: List[str]) -> List[str]:
        possible_positions = []

        for position in available_positions:
            if any(queen.can_capture(Queen(position)) for queen in result):
                continue

            possible_positions.append(position)

        return possible_positions