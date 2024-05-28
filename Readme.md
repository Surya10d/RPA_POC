# ROBOT STUDY

# Robot Framework is implemented with Python, so you need to have Python installed.
# On Windows machines, make sure to add Python to PATH during installation.

## Installing Robot Framework with pip is simple:

# ```pip install robotframework ```

## To check that the installation was successful, run

# ``` robot --version ```

## To Execute the cases on terminal, use below code
 
``` 
robot --pythonpath . <folder_path>

for eg :) folder_name = robot_test 

robot --pythonpath . robot_test
```

## To Execute a single case on terminal, use below code

```
robot --pythonpath . <test_folder_name>/<file_name>.robot

for eg:) test_folder_name = robot_test, file_name = Testsuite.robot

robot --pythonpath . robot_test/TestSuite.robot
```