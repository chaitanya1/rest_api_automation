import time
import requests
import pandas as pd 
import unittest
from pocha import it,describe
import settings
#  ------------------------------------------- URlS--------------------------------------------------------------
end_point_url = "/tasks"
All_tasks_id = []
class Test_get_methods(unittest.TestCase):
    @describe('To-do list app get request test cases')
    def _():
        @it('Making get request to fetch all tasks.')
        def get_all_tasks():
            url = settings.baseurl + end_point_url
            try:
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                response_json = response.json()
                # saving all the created tasks id's into seperate list for further use like getting task info using get method.
                for hello in response_json:
                    All_tasks_id.append(hello['id'])
                #  Asserting response status code to 200->if status code changes this test case will fail.
                assert response.status_code == 200

                # Using Pandas to beautify the json data into a tabular structure.

                data_beautify = pd.DataFrame(response_json)  

                # renaming the exisiting json payload(key_values) to readable format.
                data_beautify.rename(columns = {'completed':'Task Completed','id':'Task id','task':'Task Name',}, inplace = True)

                # Adding not null constraint,By default task id should not be null.
                task_id_not_null = pd.notnull(data_beautify["Task id"]) 

                # print(data_beautify)
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

        @it('Hitting invalid url should throw 404 error from the server')
        def invalid_url_path():
            url = "http://127.0.0.1:5000" + "/random_path"
            try:
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                assert response.status_code == 404 
                # enable below two statement to see the beautifed response.
                # data_beautify = pd.DataFrame(response) 
                # print(data_beautify)
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

        @it('counting number of finished and pending tasks')
        def pending_and_finished_task_count():
            url = settings.baseurl + end_point_url
            try:
                response = requests.get(url, headers={'Content-Type': 'application/json'})
                assert response.status_code == 200
                response_json = response.json()        
                data_beautify = pd.DataFrame(response_json) 
                data_beautify.rename(columns = {'completed':'Finished and pending task count',}, inplace = True)
                # use print statement to check total finshed and pending tasks
                count_of_tasks = data_beautify.groupby('Finished and pending task count').size()
                # print(count_of_tasks)
            #handling different types of errors.
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
            except requests.exceptions.ConnectionError as error_connecting:
                print ("Error Connecting:",error_connecting)
            except requests.exceptions.Timeout as timeout_error:
                print ("Timeout Error:",timeout_error)
            except requests.exceptions.RequestException as err:
                print ("oops: Something Else",err)
if __name__ == '__main__':
    unittest.main()