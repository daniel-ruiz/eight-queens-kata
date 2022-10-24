from eight_queens_kata.solver import EightQueensSolver


class TestSolver:

    def test_returns_eight_queens_that_cannot_be_captured_between_themselves(self):
        solver = EightQueensSolver()

        solution = solver.solve()

        assert len(solution) == 8
        
        for i in range(8):
            for j in range(i + 1, 8):
                queen_i = solution[i]
                queen_j = solution[j]
    
                assert not queen_i.can_capture(queen_j)
