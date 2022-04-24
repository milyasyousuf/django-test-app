# Simple Finance Test #


### Installation Guide and run the following command

* setup virtualenv by this command virtualenv -p python3.9 venv
* pip3 install -r requirements.txt
* setup redis server


### Run celery worker and celery flower on the other tabs
* celery -A app worker --loglevel=INFO
* celery -A app flower  --address=0.0.0.0 --port=5566


### To run the test

* Load initial data by this command   -```python3 manage.py load_initials```
* Random Revenue by this command   -```python3 manage.py random_revenue```
* Slow Iteration by this command   -```python3 manage.py slow_iteration```
