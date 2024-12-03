Introduction
==================

simple_nexus_dashboard is a simplified REST Client for the Cisco Nexus Dashboard


Features
-----------------

simple_nexus_dashboard has following features:
    * manage login
    * CRUD interface for all possible API URLs via .get, .post, .put 
    * list_all function for getting all paged results

Installation
------------

Install simple_nexus_dashboard by running:

.. code-block:: bash

    pip3 install simple_nexus_dashboard


Examples
---------

Get all Advisories for a specific Site Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import getpass
    from simple_nexus_dashboard import NexusDashboardClient
    from pprint import pprint

    nd=NexusDashboardClient("https://" + input("Nexus Dashboard IP:") , ssl_verify=False)

    nd.login(input("Username:"),getpass.getpass("Password:"))
    nd.nir.params["insightsGroupName"]=input("Site Groupname:")
    nd.nir.params["aggr"]="mnemonicTitle"

    for item in nd.nir.telemetry.advisories.details.list_all().get("entries",[]):
        pprint(item)
  


Contribute
----------

- Issue Tracker: https://github.com/jinjamator/simple_nexus_dashboard/issues
- Source Code: https://github.com/jinjamator/simple_nexus_dashboard

Roadmap
-----------------

Selected Roadmap items:
    * add more documentation
    * add some more examples

For documentation please refer to https://simple_nexus_dashboard.readthedocs.io/en/latest/

License
-----------------

This project is licensed under the Apache License Version 2.0