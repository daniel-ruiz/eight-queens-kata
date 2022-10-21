from eigth_queens_kata.models import Queen


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