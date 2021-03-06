# Project - Tournament

Running sport simulations is a common web application.

## Project Overview

In this project, we will create a simple tournament database that will simulate the results of a sporting tournament.


## Getting Started

### Prerequisites

You'll need to install:

* [Python 3.6](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/)

### Files

* `tournament.py` - [Python](https://www.python.org/) script that simulates a tournament.
* `test.py` - [Python](https://www.python.org/) script that tests to see if the tournament simulation is working correctly.
* `database_setup.sql` - [SQL](https://www.w3schools.com/sql/default.asp) commands to create the database and create the necessary tables.
* `Vagrantfile` - A [Vagrant](https://www.vagrantup.com/downloads.html) file to setup the virtual environment.


## Running the Application

To run the application follow the steps below.

### Setup Virtual Environment

We will use [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) to create a virtual environment. Setup and download instructions can be found on their various sites.

The instructions below assume that both [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) are setup.

* First, spin up the virtual environment. Navigate to the folder containing the `Vagrantfile` in your terminal, and run the command:

`vagrant up`

* If this is your first time running the command the virtual environment will begin setup, this can take some time. 

* Once the virtual environment is setup, run the command:

`vagrant ssh`

* This will log you into the virtual environment. 

* Navigate to the folder that contains the project files:

`cd /vagrant`

### Setup Database

* Make sure you're in the directory that holds the `database_setup.sql` file.
* Type `psql` into the terminal
* Type '\i database_setup.sql' to create and connect to the `tournament` database.
* Check to make sure the `players` and `matches` tables have been created by running '\d' at the prompt.
* Exit out of `psql` by typing ‘\q’

### Run the Code

* Run the python application by entering:

`python test.py`

* A tournament simulation will run.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/)
