import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math_operations import rabbits_population as rp


class RabbitsPopulationPlot:

    def __init__(self, fig):
        self.rabbits_population_subplot = fig.add_subplot(121)
        self.fractal_subplot = fig.add_subplot(122)
        initial_population_slide = plt.axes([.22, .9, .2, .03])
        rate_slide = plt.axes([.22, .94, .2, .03])
        n_years_slide = plt.axes([.6, .9, .2, .03])
        self.initial_population_slider = Slider(initial_population_slide, "initial population", valmin=0, valmax=1, valinit=0.4, valstep=0.1)
        self.rate_slider = Slider(rate_slide, "r", valmin=0, valmax=4, valinit=2.6, valstep=0.1)
        self.n_years_slider = Slider(n_years_slide, "n of years", valmin=5, valmax=100, valinit=30, valstep=5)
        self.initial_population_slider.on_changed(self.update_rabbits_population_subplot)
        self.rate_slider.on_changed(self.update_rabbits_population_subplot)
        self.n_years_slider.on_changed(self.update_rabbits_population_subplot)
        self.draw_rabbits_population_subplot()
        self.draw_fractal_subplot()

    def draw_fractal_subplot(self):
        self.fractal_subplot.set_xlabel("Rate")
        self.fractal_subplot.set_ylabel("Stationary value")
        rate_coordinates, stationary_values_coordinates = rp.get_coordinates_of_fractal()
        self.fractal_subplot.plot(rate_coordinates, stationary_values_coordinates, 'co', markersize=0.3)

    def draw_rabbits_population_subplot(self):
        self.rabbits_population_subplot.set_xlabel("Time (years)")
        self.rabbits_population_subplot.set_ylabel("Population (% of max)")
        initial_population = self.initial_population_slider.val
        rate = self.rate_slider.val
        n_years = self.n_years_slider.val
        years, populations = rp.get_years_population_values(initial_population, rate, n_years)
        self.rabbits_population_subplot.plot(years, populations)

    def update_rabbits_population_subplot(self, val):
        self.rabbits_population_subplot.clear()
        self.draw_rabbits_population_subplot()
