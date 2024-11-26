from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.preprocess_data import preprocess_data

with DAG("data_preprocessing", start_date=datetime(2024, 11, 25), schedule_interval="@daily", catchup=False) as dag:
    preprocess = PythonOperator(
        task_id="preprocess_weather_data",
        python_callable=preprocess_data
    )
