***************************
Getting started with Hambot
***************************

.. image:: https://img.shields.io/pypi/v/hambot.svg
   :target: https://pypi.python.org/pypi/hambot
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/hambot.svg?branch=master
   :target: https://travis-ci.org/readthedocs/hambot
   :alt: Build Status
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: ./hambot.png
  :align:   center


Local setup
============

It is recommended to use the steps below to set up a virtual environment for development:

.. code-block:: console

  python3 -m venv <virtual env name>
  source <virtual env name>/bin/activate
  pip install -r requirements.txt

Save credentials to ``etl.cfg`` file locally in project directory. See ``sample.etl.cfg`` file provided in root directory.

Manifests
============
This is about metadata about your test sets, including the sql and diagnostic queries to be run. Manifests files are stored in
``/hambot/manifests``


Handlers
============
Test results are printed, but handlers are available for other means of notification. See ``/hambot/handlers/``.

.. code-block:: console

  email_handler
  sftp_handler
  slack_handler
  sql_compo_list
  sql_comp
  watch_file_handler


Examples
============

Compare two lists wherein it succeeds when the lists are the same and fails when different.
Try running ``python ham_run.py -m <manifest_file_name>``

.. code-block:: console

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

Services
============
``services.yaml`` This is a global config which stores outbound communication details. Basically it says for a given scenerio, what handlers will be used, and with what targets.


Execution walkthru
===================

* Hambot will be executed from command line for a given manifest (test set): ``python ham_run.py -m <manifest_file_name>``
* It will read the tests from the corresponding manifest file into a Python object
* It will then loop through each test
* For each test it will execute the appropriate plugin
* The results from each test will be collected, then as configured in services.yaml the appropriate handler will be evoked
* Based on the services metadata, the appropriate handler will be evoked with parameters for that service (email list, sns topic, etc)


Go ahead, compose your own and try it out..

Tests
============
To run the testing suite, the following commands are required:

.. code-block:: console

  pip install -r requirements-dev.txt
  tox
