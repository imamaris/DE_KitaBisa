import uuid
import airflow
from datetime import datetime
from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

dag_params = {
    'owner': 'airflow',
    'dag_id': 'create_db',
    'start_date': airflow.utils.dates.days_ago(2)
    
}

dag = DAG(
    'create_db',
    schedule_interval="@once",
    default_args=dag_params
    )

create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres_default',
    sql='''
        CREATE TABLE product (
            id VARCHAR(50) PRIMARY KEY,
            type VARCHAR(500),
            name VARCHAR(500),
            ppu decimal,
            batters JSON,
            topping JSON
        );''',
        dag=dag
)


start = DummyOperator(
    task_id="start",
    dag=dag
)

start >> create_table