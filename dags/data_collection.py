from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.collect_data import fetch_weather_data

with DAG("data_collection", start_date=datetime(2024, 11, 25), schedule_interval="@daily", catchup=False) as dag:
    collect_data = PythonOperator(
        task_id="collect_weather_data",
        python_callable=fetch_weather_data
    )
