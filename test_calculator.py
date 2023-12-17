import calculator

class TestCalc:
    def test_sum(self):
        assert 5 == calculator.sum(2, 3)
