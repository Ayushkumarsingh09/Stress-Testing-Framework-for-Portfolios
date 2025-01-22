import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_loss_distribution(losses, title="Portfolio Loss Distribution"):
        """
        Plot the portfolio loss distribution.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(losses, bins=50, alpha=0.7, color="blue")
        plt.title(title)
        plt.xlabel("Loss")
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()

    @staticmethod
    def plot_scenario_impacts(results, title="Scenario Impact Analysis"):
        """
        Plot the impact of different scenarios on the portfolio.
        """
        results.plot(kind="bar", figsize=(12, 8))
        plt.title(title)
        plt.xlabel("Scenarios")
        plt.ylabel("Impact")
        plt.grid()
        plt.show()
