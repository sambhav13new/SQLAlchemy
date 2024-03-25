docker-compose up -d
python employee.py

python test_app.py
python test_worker.py

pytest test_integration.py

pytest test_benchmark.py --benchmark-autosave

python plot_benchmark_results.py

python performance_test.py
# SQLAlchemy
