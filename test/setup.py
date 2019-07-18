# # import unittest
# # import Test_get_methods
# # import Test_create_tasks
# # import os
# # import HtmlTestRunner
# # import time
# # import requests
# # import pandas as pd 
# # from pocha import it,describe
 
# # direct = os.getcwd()
 
# # class MyTestSuite(unittest.TestCase):
# #     def test_Issue(self):
# #         sanity_test = unittest.TestSuite()
# #         sanity_test.addTests([
# #             unittest.defaultTestLoader.loadTestsFromTestCase(Test_get_methods.Test_get_methods),
# #             unittest.defaultTestLoader.loadTestsFromTestCase(Test_create_tasks.Creating_task_events),
# #         ])
 
# #         outfile = open("\Sanity.html", "w")
 
# #         runner1 = HtmlTestRunner.HTMLTestRunner(
# #             stream=outfile
# #         )
 
# #         runner1.run(sanity_test)
 
# import unittest

# # import your test modules
# import Test_create_tasks
# import Test_get_methods

# # initialize the test suite
# loader = unittest.TestLoader()
# suite  = unittest.TestSuite()

# # add tests to the test suite
# suite.addTests(loader.loadTestsFromModule(Test_create_tasks))
# suite.addTests(loader.loadTestsFromModule(Test_get_methods))

# # initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
# result = runner.run(suite)
