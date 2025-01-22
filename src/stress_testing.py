import pandas as pd
import numpy as np

class StressTesting:
    def __init__(self, portfolio_data, market_data, stress_scenarios):
        self.portfolio_data = portfolio_data
        self.market_data = market_data
        self.stress_scenarios = stress_scenarios

    def apply_stress_scenario(self, scenario):
        """
        Apply a single stress scenario to the portfolio.
        """
        scenario_impact = self.market_data * scenario["shock_factor"]
        stressed_portfolio = self.portfolio_data + scenario_impact
        portfolio_loss = stressed_portfolio.sum(axis=1) - self.portfolio_data.sum(axis=1)
        return portfolio_loss

    def run_all_scenarios(self):
        """
        Run all stress scenarios on the portfolio.
        """
        results = {}
        for _, scenario in self.stress_scenarios.iterrows():
            results[scenario["scenario_name"]] = self.apply_stress_scenario(scenario)
        return pd.DataFrame(results)
