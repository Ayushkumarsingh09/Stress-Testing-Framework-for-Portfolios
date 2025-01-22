import unittest
import numpy as np
from src.risk_analysis import RiskAnalysis

class TestRiskAnalysis(unittest.TestCase):
    def setUp(self):
        self.returns = np.array([-0.1, -0.2, -0.3, 0.1, 0.2, 0.3])

    def test_calculate_var(self):
        var = RiskAnalysis.calculate_var(self.returns, confidence_level=0.95)
        self.assertLessEqual(var, 0)

    def test_calculate_es(self):
        es = RiskAnalysis.calculate_es(self.returns, confidence_level=0.95)
        self.assertLessEqual(es, 0)
