import json
import matplotlib.pyplot as plt

def plot_benchmark_results(results_file):
    with open(results_file, 'r') as f:
        data = json.load(f)

    benchmarks = data['benchmarks']
    names = [benchmark['name'] for benchmark in benchmarks]
    mean_times = [benchmark['stats']['mean'] for benchmark in benchmarks]

    plt.figure(figsize=(10, 6))
    plt.barh(names, mean_times, color='skyblue')
    plt.xlabel('Mean Time (ms)')
    plt.title('Benchmark Results')
    plt.show()

if __name__ == "__main__":
   # plot_benchmark_results('benchmark_results.json')
    plot_benchmark_results('/Users/sambhavgupta/PycharmProjects/SQLAlchemy/.benchmarks/Darwin-CPython-3.9-64bit/0004_benchmark_results.json.json')
