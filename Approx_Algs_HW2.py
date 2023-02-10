import time
import random

def first_fit(items, bin_capacity):
    n = len(items)
    bins = []
    for i in range(n):
        item_placed = False
        for j in range(len(bins)):
            if bins[j] + items[i] <= bin_capacity:
                bins[j] += items[i]
                item_placed = True
                break
        if not item_placed:
            bins.append(items[i])
    return len(bins)

def run_experiment(num_items, max_item_size, bin_capacity, num_trials, algorithm):
    results = []
    for trial in range(num_trials):
        items = generate_data(num_items, max_item_size)
        start_time = time.time()
        num_bins = algorithm(items, bin_capacity)
        end_time = time.time()
        runtime = end_time - start_time
        if(runtime > 0.025):
            runtime = 0.025
        results.append((runtime, num_bins))
    return results

def generate_data(num_items, max_item_size):
    items = []
    for i in range(num_items):
        items.append(random.randint(1, max_item_size))
    return items


def best_fit(items, bin_capacity):
    n = len(items)
    bins = []
    for i in range(n):
        min_bin = -1
        min_bin_space = bin_capacity + 1
        for j in range(len(bins)):
            if bins[j] + items[i] <= bin_capacity and bin_capacity - (bins[j] + items[i]) < min_bin_space:
                min_bin = j
                min_bin_space = bin_capacity - (bins[j] + items[i])
        if min_bin == -1:
            bins.append(items[i])
        else:
            bins[min_bin] += items[i]
    return len(bins)

def first_fit_decreasing(items, bin_capacity):
    n = len(items)
    items.sort(reverse=True)
    bins = []
    for i in range(n):
        item_placed = False
        for j in range(len(bins)):
            if bins[j] + items[i] <= bin_capacity:
                bins[j] += items[i]
                item_placed = True
                break
        if not item_placed:
            bins.append(items[i])
    return len(bins)

def best_fit_decreasing(items, bin_capacity):
    n = len(items)
    items.sort(reverse=True)
    bins = []
    for i in range(n):
        min_bin = -1
        min_bin_space = bin_capacity + 1
        for j in range(len(bins)):
            if bins[j] + items[i] <= bin_capacity and bin_capacity - (bins[j] + items[i]) < min_bin_space:
                min_bin = j
                min_bin_space = bin_capacity - (bins[j] + items[i])
        if min_bin == -1:
            bins.append(items[i])
        else:
            bins[min_bin] += items[i]
    return len(bins)


import matplotlib.pyplot as plt
import numpy as np
def compare_algorithms(num_items_list, max_item_size, bin_capacity, num_trials):
    algorithms = [first_fit, best_fit, first_fit_decreasing, best_fit_decreasing]
    algorithm_names = ['First Fit', 'Best Fit', 'First Fit Decreasing', 'Best Fit Decreasing']
    runtime_data = []
    bins_data = []
    for algorithm, name in zip(algorithms, algorithm_names):
        runtimes = []
        bins = []
        for num_items in num_items_list:
            results = run_experiment(num_items, max_item_size, bin_capacity, num_trials, algorithm)
            runtimes_for_trial = [result[0] for result in results]
            num_bins_for_trial = [result[1] for result in results]
            runtimes.append(np.mean(runtimes_for_trial))
            bins.append(np.mean(num_bins_for_trial))
        runtime_data.append(runtimes)
        bins_data.append(bins)

    fig, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    #color = 'tab:red'
    ax1.set_xlabel('Number of items')
    ax1.set_ylabel('Runtime')
    #ax1.set_ylabel('Runtime (s)', color=color)
    color_palette = ['red', 'blue', 'green', 'purple']
    for i, (runtimes, name) in enumerate(zip(runtime_data, algorithm_names)):
        color = color_palette[i]
        ax1.plot(num_items_list, runtimes, label=name, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    #ax2 = ax1.twinx()
    #color = 'tab:blue'
    #ax2.set_ylabel('Number of bins', color=color)
    ax2.set_xlabel('Number of items')
    ax2.set_ylabel('Bins Used')
    for i, (bins, name) in enumerate(zip(bins_data, algorithm_names)):
        color = color_palette[i]
        ax2.plot(num_items_list, bins, label=name, color=color, linestyle='--')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.legend()
    fig.tight_layout()
    fig2.legend()
    fig2.tight_layout
    plt.show()






def main():
    num_items_list = range(10, 1001, 10)
    max_item_size = 50
    bin_capacity = 100
    num_trials = 75
    compare_algorithms(num_items_list, max_item_size, bin_capacity, num_trials)

if __name__ == '__main__':
    main()
