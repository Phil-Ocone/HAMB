
# HAMbot

## Health And Monitoring Robot

![hambot](docs/hambot.png)

# Local setup
It is recommended to use the steps below to set up a virtual environment for development:

```
python3 -m venv <virtual env name>
source <virtual env name>/bin/activate
pip install -r requirements.txt
```
Save credentials to `etl.cfg` file locally in project directory. See `sample-etl.cfg` file provided in root directory.

# Components

### hambot/handlers/
This is how you will add new service targets. 

Note that by default hambot will always log to a database. Currently, the default database is postgreSQL, but HAMbot will log to anything that SQLAlchemy can connect to.

Please reference `hambot/hambot_history.ddl` file to create the logging table in your preferred database. 

 - sql_comp_list - compares two lists wherein it succeeds when the lists are the same and fails when different 
(Try running `python ham_run.py -m comp_list_sample`)
```
Examples:

a. when lists are the same
'script_a_result': [a, b, c]
'script_b_result': [a, b, c]
'status': 'success'
'diff': None

b. when only a few elements are similar
'script_a_result': [a, b, c]
'script_b_result': [a, b]
'status': 'failure'
'diff': [c]

c. when one list is empty
'script_a_result': [a, b, c]
'script_b_result': []
'status': 'failure'
'diff': [a, b, c]

d. when lists have completely different elements
'script_a_result': [a, b, c]
'script_b_result': [d, e, f]
'status': 'failure'
'diff': [a, b, c, d, e, f]
```
### manifests/
This is where you will store metadata about your test sets, including the sql and diagnostic queries to be run.

### services.yaml
This is a global config which stores outbound communication details. Basically it says for a given scenerio, what handlers will be used, and with what targets.

# A walkthru of execution:

1. Hambot will be executed from command line for a given manifest (test set): `python ham_run.py -m <manifest_file_name>`
2. It will read the tests from the corresponding manifest file into a Python object
3. It will then loop through each test
4. For each test it will execute the appropriate plugin
5. The results from each test will be collected, then as configured in services.yaml the appropriate handler will be evoked
6. Based on the services metadata, the appropriate handler will be evoked with parameters for that service (email list, sns topic, etc)

# Features
Test results are printed, but handlers are available for other means of notification including:
- Slack
- Email
- FTP/SFTP upload

The sample manifest file: `manifests/sample.yaml` has a few examples tests.

To run the sample: `python ham_run.py -m sample`.

Go ahead, compose your own and try it out..

# Tests
To run the testing suite, the following commands are required:
```
pip install -r requirements-dev.txt
tox
```