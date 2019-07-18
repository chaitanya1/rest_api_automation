import time
import json
import requests
import unittest
import pytest
import pandas as pd
from pocha import it,describe
import settings
#  ------------------------------------------- URlS--------------------------------------------------------------

end_point_url = "/tasks"

# -------------------------------------------------------------------------------------------------------------------


class Test_creating_task_events(unittest.TestCase):
    @describe('Testcases related to creating tasks in todo-list app')
    def _():
        @it('creating a new task')
        def create_new_task():
            url = settings.baseurl + end_point_url
            try:
                #request body for creating a new task
                payload = {"task": "add task","completed": "false"}
                response = requests.post(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'})
                response_json = response.json() 

                # print(response_json) 

                assert response.status_code == 200
                task_id = response_json['task_id']
                # As there was no taskname from the sample response,so getting taskname from pay load.

                task_name =payload['task']


            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.ConnectionError as error_connecting:
                print ("Error Connecting:",error_connecting)
            except requests.exceptions.Timeout as timeout_error:
                print ("Timeout Error:",timeout_error)
            except requests.exceptions.RequestException as err:
                print ("OOps: Something Else",err)


        # fetching recently create task and verifying that task is created or not.
            url = settings.baseurl + "/tasks/" + str(task_id)
            try:

            #making get request for created events and verifying that created data is valid or not. 
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                response_json = response.json() 
                # getting task_name from the previous function and asserting the tasking making get request.

                assert response.status_code == 200

                # Asserting the taskname to make sure created and fetched name are same.
                assert task_name == response_json['task']
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.ConnectionError as error_connecting:
                print ("Error Connecting:",error_connecting)
            except requests.exceptions.Timeout as timeout_error:
                print ("Timeout Error:",timeout_error)
            except requests.exceptions.RequestException as err:
                print ("OOps: Something Else",err)

        @it('Verify that if there is no request body the server should throw 400 status')
        def sending_empty_data_to_api():
            url = settings.baseurl + end_point_url  
            #request body for creating a new task
            payload = {}
            response = requests.post(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'}) 
            assert response.status_code == 400  

        @it('Verify that if user hits invalid url,server should throw 404.')
        def hitting_invalid_url():
            url = settings.baseurl + "/invalid_url/"
            #request body for creating a new task
            payload = {}
            response = requests.post(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'}) 
            assert response.status_code == 404

        @it('Verify that if user hits endpoint other than get,put,post,delete should throw method not allowed')
        def hitting_with_invalid_method():
            url = settings.baseurl + end_point_url
            #request body for creating a new task
            payload = {}
            response = requests.patch(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'}) 
            assert response.status_code == 405

        @it('Verify that if user sends request without taskname value should throw 400 validation error')
        def hitting_without_task_name():
            url = settings.baseurl + end_point_url
            #request body for creating a new task
            payload = {"completed": "false"}
            response = requests.post(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'}) 
            assert response.status_code == 400

if __name__ == '__main__':
    unittest.main()