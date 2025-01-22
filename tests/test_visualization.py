import unittest
from src.visualization import Visualization

class TestVisualization(unittest.TestCase):
    def test_plot_loss_distribution(self):
        try:
            Visualization.plot_loss_distribution([1, 2, 3, 4])
        except Exception as e:
            self.fail(f"plot_loss_distribution failed: {e}")

    def test_plot_scenario_impacts(self):
        try:
            Visualization.plot_scenario_impacts({"Scenario1": 1, "Scenario2": 2})
        except Exception as e:
            self.fail(f"plot_scenario_impacts failed: {e}")
