Installation
============

Overview
--------
Before the **ifrs16** package can be used, it must be installed on your computer.
The **ifrs16** is not currently hosted on `PyPi`_ and instead involves installing
it from a pre-built wheel. The wheel is a pre-made file of the **ifrs16** source code to be
installed.

.. _`PyPi`: https://pypi.org/

So there are three options available to get the wheel:

#. via an URL to GitHub where it is hosted (*recommended*)
#. download wheel from GitHub manually
#. build the wheel yourself from the source code

GitHub URL (Option 1)
---------------------
The quickest way to get started is to install the wheel directly from a release on GitHub.

#. Find the latest release from GitHub
#. Install it using pip:
	
	.. container:: highlight

		.. parsed-literal::
		
			pip install \ |wheel|\ 

You can verify that the package has been installed by listing your dependencies

	.. code-block:: console

		pip freeze
		ifrs16 @ https://github.com/bradley-smith-gpa/sphinx-test/releases/<latest-wheel-file>.whl

GitHub Download (Option 2)
--------------------------

#. :wheel_url:`Download the wheel  <>` from GitHub and save it to a location on your computer
#. Install the wheel using pip:

.. code-block:: console

	pip install path/to/your/directory/<latest-wheel-file>.whl

You can verify that the package has been installed by listing your dependencies

.. code-block:: console

	pip freeze
	...
	ifrs16 @ file:///path/to/your/directory/<latest-wheel-file>.whl
	...

Notice that the URI starts with the ``file:///`` since we are referencing
the wheel file locally.

Build from Source Code (Option 3)
---------------------------------
#. Clone the ifrs16 repo
#. Navigate to the repo directory in your command line (i.e. where the ``pyproject.toml`` file is),
#. Run the following command

	.. code-block:: console

		python -m build

#. Navigate to the ``dist`` folder which should contain a wheel file
#. Install the wheel using pip:

	.. code-block:: console

		pip install path/to/your/directory/<latest-wheel-file>.whl

You can verify that the package has been installed by listing your dependencies

.. code-block:: console

	pip freeze
	...
	ifrs16 @ file:///path/to/your/directory/<latest-wheel-file>.whl
	...

Notice that the URI starts with the ``file:///`` since we are referencing
the wheel file locally.
