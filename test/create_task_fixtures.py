import json
import pytest
import requests
#-----Do Not Execute this file-

@pytest.fixture()
def create_task_data():
    primary_view_data = {"task": "add task","completed": "false"}
    return primary_view_data

@pytest.fixture()
def create_task_without_name():
    data = {"completed": false}
    return data
