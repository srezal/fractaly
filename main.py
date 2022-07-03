from plots.RabbitsPopulationPlot import RabbitsPopulationPlot
import matplotlib.pyplot as plt


if __name__ == "__main__":
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 6))
    rb = RabbitsPopulationPlot(fig)
    plt.show()
