from typing import Tuple

LETTERS_THAT_INDICATE_A_BOARD_FILE = 'abcdefgh'


class Queen:

    def __init__(self, position: str) -> None:
        self.position = position
        self.file, self.row = self._calculate_cartesian_position(position)

    def __repr__(self) -> str:
        return f"Queen({self.position})"

    def _calculate_cartesian_position(self, position: str) -> Tuple[int, int]:
        file_representation = position[0]
        row_representation = position[1]

        return LETTERS_THAT_INDICATE_A_BOARD_FILE.index(file_representation), int(row_representation)

    def can_capture(self, other_queen: "Queen") -> bool:
        return (
            self._is_other_queen_in_same_row(other_queen)
            or self._is_other_queen_in_same_file(other_queen)
            or self._is_other_queen_in_a_diagonal(other_queen)
        )

    def _is_other_queen_in_same_file(self, other_queen: "Queen") -> bool:
        return self.file == other_queen.file

    def _is_other_queen_in_same_row(self, other_queen: "Queen") -> bool:
        return self.row == other_queen.row

    def _is_other_queen_in_a_diagonal(self, other_queen: "Queen") -> bool:
        return abs(self.file - other_queen.file) == abs(self.row - other_queen.row)
