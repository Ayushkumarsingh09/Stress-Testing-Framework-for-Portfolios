import unittest
import pandas as pd
from src.stress_testing import StressTesting

class TestStressTesting(unittest.TestCase):
    def setUp(self):
        self.portfolio_data = pd.DataFrame({"Asset1": [100, 200], "Asset2": [300, 400]})
        self.market_data = pd.DataFrame({"Asset1": [0.1, -0.1], "Asset2": [0.05, -0.05]})
        self.stress_scenarios = pd.DataFrame({
            "scenario_name": ["Shock1", "Shock2"],
            "shock_factor": [0.5, -0.5]
        })

    def test_apply_stress_scenario(self):
        tester = StressTesting(self.portfolio_data, self.market_data, self.stress_scenarios)
        result = tester.apply_stress_scenario(self.stress_scenarios.iloc[0])
        self.assertEqual(len(result), 2)

    def test_run_all_scenarios(self):
        tester = StressTesting(self.portfolio_data, self.market_data, self.stress_scenarios)
        results = tester.run_all_scenarios()
        self.assertEqual(results.shape[1], 2)
