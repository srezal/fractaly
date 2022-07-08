def get_years_population_values(initial_population, rate, n_years):
    years = [i for i in range(n_years + 1)]
    populations = [initial_population] + [0] * n_years
    for i in range(1, n_years + 1):
        populations[i] = rate * populations[i - 1] * (1 - populations[i - 1])
    return years, populations


def get_stationary_values(populations):
    rounded_populations = [round(i, 3) for i in populations]
    number_of_occur = [[i, rounded_populations.count(i)] for i in set(rounded_populations)]
    number_of_occur.sort(key=lambda i: i[1], reverse=True)
    stationary_values = [number_of_occur[0][0]]
    for i in range(1, len(number_of_occur)):
        ratio = number_of_occur[i][1] / number_of_occur[0][1]
        if ratio < 0.9:
            break
        else:
            stationary_values.append(number_of_occur[i][0])
    return stationary_values


def get_coordinates_of_fractal():
    rate_coordinates = []
    stationary_values_coordinates = []
    rate = 0
    while rate < 4:
        population = get_years_population_values(0.4, rate, 100)[1]
        stationary_values = get_stationary_values(population)
        rate_coordinates.extend([rate] * len(stationary_values))
        stationary_values_coordinates.extend(stationary_values)
        rate += 0.001
    return rate_coordinates, stationary_values_coordinates
