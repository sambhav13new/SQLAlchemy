import concurrent.futures
import time
import json

def task_function(parameter):
    # Simulate some computation
    time.sleep(2)
    result = parameter * 2
    return result

def run_tasks_in_threads(parameters):
    results = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the thread pool
        futures = {executor.submit(task_function, param): param for param in parameters}

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            param = futures[future]
            try:
                result = future.result()
                results[param] = result
                print(f"Task with parameter {param} completed. Result: {result}")
            except Exception as e:
                print(f"Task with parameter {param} failed: {e}")

    return results

if __name__ == "__main__":
    task_parameters = [1, 2, 3, 4, 5]  # Example task parameters

    results = run_tasks_in_threads(task_parameters)

    # Save results to a JSON file
    with open('thread_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=2)

    print("Results saved to 'thread_results.json'")
