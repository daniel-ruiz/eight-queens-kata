from typing import Tuple

FILE_POSSIBLE_NAMES = 'abcdefgh'


class Queen:

    def __init__(self, position: str) -> None:
        self.file, self.row = self._calculate_cartesian_position(position)

    def _calculate_cartesian_position(self, position: str) -> Tuple[int, int]:
        file_representation = position[0]
        row_representation = position[1]

        return FILE_POSSIBLE_NAMES.index(file_representation), int(row_representation)

    def can_capture(self, other_queen: "Queen") -> bool:
        return self.row == other_queen.row or self.file == other_queen.file
