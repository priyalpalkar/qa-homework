# Rescale File Upload Testing

Installation and Execution
--------------------------
.. code-block:: bash

	$ docker-compose up -d

To run UI Tests

- Install VNC viewer: https://www.realvnc.com/en/connect/download/viewer/
- Start VNC viewer at localhost:5900 (password: secret)

.. code-block:: bash

	$ docker exec test_runner pytest test/test_ui


To run API Tests

.. code-block:: bash

	$ docker exec test_runner pytest test/test_api

To run API and UI Tests

.. code-block:: bash

	$ docker exec test_runner pytest test
