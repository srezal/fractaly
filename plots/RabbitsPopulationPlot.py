import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class RabbitsPopulationPlot:
    ax = None
    initial_population_slider = None
    r_slider = None

    def __init__(self, fig):
        self.ax = fig.add_subplot(111)
        ax_initial_population_slide = plt.axes([.22, .9, .2, .03])
        ax_r_slide = plt.axes([.22, .94, .2, .03])
        self.initial_population_slider = Slider(ax_initial_population_slide, "initial population", valmin=0, valmax=1, valinit=0.4, valstep=0.1)
        self.r_slider = Slider(ax_r_slide, "r", valmin=0, valmax=4, valinit=2.6, valstep=0.1)
        self.draw()
        self.initial_population_slider.on_changed(self.update)
        self.r_slider.on_changed(self.update)

    def f(self, initial_population, r):
        years = [i for i in range(31)]
        population = [initial_population] + [0] * 30
        for i in range(1, 31):
            population[i] = r * population[i - 1] * (1 - population[i - 1])
        return years, population

    def draw(self):
        initial_population = self.initial_population_slider.val
        r = self.r_slider.val
        years, population = self.f(initial_population, r)
        self.ax.plot(years, population)
        self.ax.set_xlabel("time (years)")
        self.ax.set_ylabel("population (% of max)")

    def update(self, val):
        self.ax.clear()
        self.draw()
