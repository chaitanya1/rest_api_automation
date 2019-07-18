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
class Test_creating_task_events(unittest.TestCase):
    @describe('Testcases are related to deleting Tasks in to-do-list app')
    def _():
        @it('First we create a task and pass the created task id to delete request.')
        def delete_new_task():
            url = settings.baseurl + end_point_url
            try:
                #request body for creating a new task
                payload = {"task": "add task_1","completed": "false"}
                response = requests.post(url,data=json.dumps(payload),headers={'Content-Type': 'application/json'})
                response_json = response.json() 
                # print(response_json) 
                assert response.status_code == 200
                task_id = response_json['task_id']
                # As there was no taskname from the sample response,so getting taskname from pay load.
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


        # deleting recently created task by making delete request
            url = settings.baseurl + "/tasks/" + str(task_id)
            try:

            #making delete request for created event. 
                response = requests.delete(url, headers={'Content-Type': 'application/json'})
                response_json = response.json() 
                # getting task_name from the previous function and asserting the tasking making get request.

                assert response.status_code == 200
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

        #hitting getrequest method with deleted eventid to make sure that event is deleted.
            url = settings.baseurl + "/tasks/" + str(task_id)
            try:

            #making delete request for created event. 
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                response_json = response.json() 
                # getting task_name from the previous function and asserting the tasking making get request.

                assert response.status_code == 404
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
            
        @it('Verify that if there is invalid task_id in parameters the server should throw 404 status')
        def sending_empty_data_to_api():
            empty = "alksdalsdj"
            url = settings.baseurl + end_point_url + empty
            #request body for creating a new task
            response = requests.delete(url,headers={'Content-Type': 'application/json'}) 
            assert response.status_code == 404

if __name__ == '__main__':
    unittest.main()