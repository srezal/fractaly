import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class RabbitsPopulationPlot:
    ax = None
    initial_population_slider = None
    r_slider = None
    n_years_slider = None
    rates = []
    stationaries = []

    def __init__(self, fig):
        self.fractal()
        self.ax = fig.add_subplot(121)
        self.bx = fig.add_subplot(122)
        ax_initial_population_slide = plt.axes([.22, .9, .2, .03])
        ax_r_slide = plt.axes([.22, .94, .2, .03])
        n_years_slide = plt.axes([.6, .9, .2, .03])
        self.initial_population_slider = Slider(ax_initial_population_slide, "initial population", valmin=0, valmax=1, valinit=0.4, valstep=0.1)
        self.r_slider = Slider(ax_r_slide, "r", valmin=0, valmax=4, valinit=2.6, valstep=0.1)
        self.n_years_slider = Slider(n_years_slide, "n of years", valmin=5, valmax=100, valinit=30, valstep=5)
        self.draw()
        self.initial_population_slider.on_changed(self.update)
        self.r_slider.on_changed(self.update)
        self.n_years_slider.on_changed(self.update)

    def f(self, initial_population, r, n_years):
        years = [i for i in range(n_years+1)]
        population = [initial_population] + [0] * n_years
        for i in range(1, n_years + 1):
            population[i] = r * population[i - 1] * (1 - population[i - 1])
        return years, population

    @staticmethod
    def get_stationaries(population):
        p = [int(i * 1000) for i in population]
        values = [[i, p.count(i)] for i in set(p)]
        values.sort(key=lambda i: i[1], reverse=True)
        stationaries = [values[0][0]]
        for i in range(1, len(values)):
            ratio = values[i][1] / values[0][1]
            if ratio < 0.9:
                break
            else:
                stationaries.append(values[i][0])
        return [x / 1000 for x in stationaries]

    def fractal(self):
        i = 0
        while i <= 4:
            population = self.f(0.4, i, 100)[1]
            stats = self.get_stationaries(population)
            self.stationaries.extend(stats)
            self.rates.extend([i] * len(stats))
            i += 0.001

    def draw(self):
        initial_population = self.initial_population_slider.val
        r = self.r_slider.val
        n_years = self.n_years_slider.val
        years, population = self.f(initial_population, r, n_years)
        self.ax.plot(years, population)
        self.ax.set_xlabel("Time (years)")
        self.ax.set_ylabel("Population (% of max)")
        self.bx.plot(self.rates, self.stationaries, 'co', markersize=0.3)
        self.bx.set_xlabel("Rate")
        self.bx.set_ylabel("Stationary value")

    def update(self, val):
        self.ax.clear()
        self.bx.clear()
        self.draw()
