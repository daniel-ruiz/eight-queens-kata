class TestQueen:

    def test_queen_can_capture_queens_of_the_same_row(self):
        assert Queen("a3").can_capture(Queen("d3")) is True
        assert Queen("d3").can_capture(Queen("a3")) is True
