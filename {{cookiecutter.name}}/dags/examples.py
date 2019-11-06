#!/usr/bin/env python3

from datetime import datetime

from airflow import DAG

from airflow.operators.bash_operator import BashOperator

# DEFAULTS

default_args = {
    'owner': '{{cookiecutter.owner}}',
    'depends_on_past': False,
    'end_date': datetime({{cookiecutter.end_date|replace('-', ', ')}}),
    'start_date': datetime({{cookiecutter.start_date|replace('-', ', ')}}),
}

# DIGRAPHS

dag = DAG(
    '{{cookiecutter.name}}',
    catchup=False,
    default_args=default_args,
    schedule_interval='{{cookiecutter.schedule_interval}}',
)

# OPERATORS

t1 = BashOperator(
    dag=dag,
    task_id='date',
    bash_command='date',
)

t2 = BashOperator(
    dag=dag,
    task_id='whoami',
    bash_command='whoami',
)

t3 = BashOperator(
    dag=dag,
    task_id='hostname',
    bash_command='hostname',
)

# DEPENDENCIES

t1 >> t2 >> t3
