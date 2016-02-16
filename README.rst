=============================
dj-node-utils
=============================

.. image:: https://badge.fury.io/py/dj-node-utils.png
    :target: https://badge.fury.io/py/dj-node-utils

.. image:: https://travis-ci.org/schacki/dj-node-utils.png?branch=master
    :target: https://travis-ci.org/schacki/dj-node-utils

It requires quite some repetitive, boilerplate code to fully integrate your Django project with any gulp or grunt tasks,
if you want to use any or your project's Django settings or have access your project's static directories. dj-node-utils
will provide some easy to use management commands to address this issue.

Documentation
-------------

The full documentation is at https://dj-node-utils.readthedocs.org.

Quickstart
----------

Install dj-node-utils::

    pip install dj-node-utils

Then use it in a project::

    import dj_node_utils

Features
--------

* Python API and management command to get a JSON list of absolute static file directories.
* Python API and Django management command to get a JSON dictionary of all available Django settings.

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
