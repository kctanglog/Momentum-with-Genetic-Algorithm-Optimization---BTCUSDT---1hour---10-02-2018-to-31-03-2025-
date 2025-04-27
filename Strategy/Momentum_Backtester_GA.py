# Momentum_Backtester - GA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

class Momentum_Backtester(object):
    ''' A class designed for backtesting trading strategy based on 
        Momentum in a vectorized manner
    '''
    
    def __init__(self, asset, start_time, end_time, capital, t_cost):
        self.asset = asset
        self.start_time = start_time
        self.end_time = end_time
        self.capital = capital
        self.t_cost = t_cost
        self.results = None
        self.import_data()

    def import_data(self):
        ''' Loads and prepares the historical price data for backtesting '''
        # ⭐
        data_imported = "BTCUSDT - 1hour - (10-02-2018 to 31-03-2025)"
        fn = f'/Users/kctang/Desktop/Algo Trading Project (S2)/Data/Data - Processed/Data/{data_imported}.csv'
        raw_data = pd.read_csv(fn, index_col=0, parse_dates=True).dropna()
        raw_data = pd.DataFrame(raw_data['close'])
        raw_data = raw_data.loc[self.start_time:self.end_time]
        raw_data.rename(columns={'close': 'price'}, inplace=True)
        raw_data['return'] = np.log(raw_data / raw_data.shift(1))
        self.data = raw_data

    def execute_strategy(self, momentum=1):
        ''' Executes trading strategy and evaluates its performance '''
        self.momentum = momentum
        data = self.data.copy().dropna()
        data['position'] = np.sign(data['return'].rolling(momentum).mean())
        data['strategy'] = data['position'].shift(1) * data['return']
        data.dropna(inplace=True)
        trades = data['position'].diff().fillna(0) != 0
        data.loc[trades, 'strategy'] -= self.t_cost
        data['cum_returns'] = self.capital * data['return'].cumsum().apply(np.exp)
        data['cum_strategy'] = self.capital * data['strategy'].cumsum().apply(np.exp)
        self.results = data
        total_perf = self.results['cum_strategy'].iloc[-1]
        out_perf = total_perf - self.results['cum_returns'].iloc[-1]
        return round(total_perf, 2), round(out_perf, 2)

    def display_results(self):
        ''' Creates a plot comparing the strategy's performance to that of the asset '''
        if self.results is None:
            print('No results to plot yet. Run a strategy.')
        title = '%s | t_cost = %.4f' % (self.asset, self.t_cost)
        self.results[['cum_returns', 'cum_strategy']].plot(title=title, figsize=(20, 12))

    def parameters_optimization(self, momentum_range):
        ''' Brute force optimization (original method) '''
        performances = []
        for momentum in momentum_range:
            total_perf, _ = self.execute_strategy(momentum)
            performances.append((momentum, total_perf))
        results = pd.DataFrame(performances, columns=['momentum', 'performance'])
        best_momentum = results.loc[results['performance'].idxmax(), 'momentum']
        best_performance = results['performance'].max()
        print(f'Best Momentum: {best_momentum}, Best Performance: {best_performance}\n')
        return results

    def genetic_algorithm_optimization(self, generations=10, population_size=10, mutation_rate=0.1, momentum_bounds=(1, 100)):
        ''' Uses Genetic Algorithm (GA) to optimize the momentum parameter '''
        
        def generate_individual():
            return random.randint(momentum_bounds[0], momentum_bounds[1])

        def generate_population():
            return [generate_individual() for _ in range(population_size)]

        def fitness(individual):
            performance, _ = self.execute_strategy(momentum=individual)
            return performance

        def selection(population, fitnesses):
            selected = random.choices(list(zip(population, fitnesses)), k=2)
            return max(selected, key=lambda x: x[1])[0]

        def crossover(parent1, parent2):
            return int((parent1 + parent2) / 2)

        def mutate(individual):
            if random.random() < mutation_rate:
                return generate_individual()
            return individual

        population = generate_population()
        best_individual = None
        best_fitness = -float('inf')
        history = []

        for gen in range(generations):
            fitnesses = [fitness(ind) for ind in population]
            gen_best_fitness = max(fitnesses)
            gen_best_individual = population[fitnesses.index(gen_best_fitness)]

            if gen_best_fitness > best_fitness:
                best_fitness = gen_best_fitness
                best_individual = gen_best_individual

            print(f"Generation {gen+1} | Best Momentum: {gen_best_individual} | Performance: {gen_best_fitness}")
            history.append((gen_best_individual, gen_best_fitness))

            new_population = []
            for _ in range(population_size):
                parent1 = selection(population, fitnesses)
                parent2 = selection(population, fitnesses)
                child = crossover(parent1, parent2)
                child = mutate(child)
                new_population.append(child)

            population = new_population

        print(f"\nOptimal Momentum Found: {best_individual} | Performance: {best_fitness}")
        return pd.DataFrame(history, columns=['momentum', 'performance'])

    def heatmap_visualisation(self, results):
        ''' Visualizes the optimization results using a heatmap '''
        heatmap_data = results.pivot(index="momentum", columns="performance", values="performance")
        max_index = results['performance'].idxmax()
        max_momentum = results.loc[max_index, 'momentum']
        max_performance = results.loc[max_index, 'performance']
        # Plot the heatmap
        # can change figsize for longer height, eg. 6 -> 100
        #   standard : plt.figure(figsize=(25, 6))
        #   longer   : plt.figure(figsize=(25, 100))
        #   longest  : plt.figure(figsize=(25, 500))
        # ⭐
        plt.figure(figsize=(25, 6))
        ax = sns.heatmap(
            heatmap_data,
            cmap="RdYlGn",
            annot=True,
            fmt=".2f",
            center=self.capital,
            cbar=True,
        )
        rect_x = heatmap_data.columns.get_loc(max_performance) - 0.6
        rect_y = heatmap_data.index.get_loc(max_momentum) - 0.4
        rect_width = 2.2
        rect_height = 1.8
        rect = plt.Rectangle(
            (rect_x, rect_y),
            rect_width,
            rect_height,
            fill=False, color='magenta', linewidth=3
        )
        ax.add_patch(rect)
        max_x = heatmap_data.columns.get_loc(max_performance) + 0.5
        max_y = heatmap_data.index.get_loc(max_momentum) + 0.5
        x_gap_start = max_x - (rect_width / 2)
        x_gap_end = max_x + (rect_width / 2)
        plt.hlines(
            y=max_y, xmin=0, xmax=x_gap_start, color='magenta', linestyle='-', linewidth=1.5, alpha=0.8
        )
        plt.vlines(
            x=max_x, ymin=max_y + (rect_height / 2), ymax=len(heatmap_data.index),
            color='magenta', linestyle='-', linewidth=1.5, alpha=0.8
        )
        plt.xlim(-0.5, len(heatmap_data.columns) + 1)
        plt.title("Momentum Optimization Heatmap")
        plt.xlabel("Performance")
        plt.ylabel("Momentum")
        plt.show()

    def ga_visualisation(self, results):
        ''' Visualizes GA optimization results (generation vs performance) '''
        plt.figure(figsize=(20, 8))
        plt.plot(range(1, len(results) + 1), results['performance'], marker='o', color='blue')
        plt.title('Genetic Algorithm Optimization Progress')
        plt.xlabel('Generation')
        plt.ylabel('Performance')
        plt.grid(True)
        plt.show()