from eight_queens_kata.models import Queen


class TestQueen:

    def test_queen_can_capture_queens_of_the_same_row(self):
        assert Queen("a3").can_capture(Queen("d3"))
        assert Queen("d3").can_capture(Queen("a3"))

    def test_queen_can_capture_queens_of_the_same_file(self):
        assert Queen("f5").can_capture(Queen("f1"))
        assert Queen("f1").can_capture(Queen("f5"))

    def test_queen_can_capture_queens_in_one_diagonal(self):
        assert Queen("c4").can_capture(Queen("f7"))
        assert Queen("f7").can_capture(Queen("c4"))

    def test_queen_can_capture_queens_in_the_other_diagonal(self):
        assert Queen("c4").can_capture(Queen("e2"))
        assert Queen("e2").can_capture(Queen("c4"))

    def test_queen_cannot_capture_queens_not_in_same_row_or_file_or_diagonal(self):
        assert not Queen("g6").can_capture(Queen("h4"))
        assert not Queen("h4").can_capture(Queen("g6"))
