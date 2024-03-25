import requests
from concurrent.futures import ThreadPoolExecutor
import time
import json

def make_request(url):
    response = requests.get(url)
    return response.status_code

def test_parallel_requests(app_url, max_parallel_requests=100, threshold_time=5.0):
    results = {}

    for num_parallel_requests in range(1, max_parallel_requests + 1):
        with ThreadPoolExecutor(max_workers=num_parallel_requests) as executor:
            start_time = time.time()
            _ = list(executor.map(make_request, [app_url] * num_parallel_requests))
            end_time = time.time()

        total_time = end_time - start_time
        results[num_parallel_requests] = {
            "total_time": total_time,
            "requests_per_second": num_parallel_requests / total_time
        }

        print(f"Parallel Requests: {num_parallel_requests}")
        print(f"Total Time: {total_time:.2f} seconds")
        print(f"Requests per Second: {num_parallel_requests / total_time:.2f}")
        print("---")

        # Check if performance starts to degrade
        if total_time > threshold_time:
            bre
