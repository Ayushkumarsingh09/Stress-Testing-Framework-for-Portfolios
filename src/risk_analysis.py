import numpy as np

class RiskAnalysis:
    @staticmethod
    def calculate_var(returns, confidence_level=0.95):
        """
        Calculate Value at Risk (VaR) for the portfolio.
        """
        return np.percentile(returns, (1 - confidence_level) * 100)

    @staticmethod
    def calculate_es(returns, confidence_level=0.95):
        """
        Calculate Expected Shortfall (ES) for the portfolio.
        """
        var = RiskAnalysis.calculate_var(returns, confidence_level)
        return returns[returns <= var].mean()
