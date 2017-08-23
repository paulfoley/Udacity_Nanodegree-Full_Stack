# Project - Bug Management

Finding and fixing bugs in an application is one of the main responsibilities of web developers.

## Project Overview

In this project, we will create a simple database that can track bugs.


## Getting Started

### Prerequisites

You'll need to install:

* [Python 3.6](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/)

### Files

* `bug_management.py` - [Python](https://www.python.org/) script that mimics an API server using [Flask](http://flask.pocoo.org/).
* `database_setup.sql` - [SQL](https://www.w3schools.com/sql/default.asp) commands to create the database and create the necessary tables.
* `Vagrantfile` - A [Vagrant](https://www.vagrantup.com/downloads.html) file to setup the virtual environment.


## Running the Application

To run the application follow the steps below.

### Setup Virtual Environment

We will use [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) to create a virtual environment. Setup and download instructions can be found on their various sites.

The instructions below assume that both [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) are setup.

* First spin up the virtual environment. Navigate to the folder containing the `Vagrantfile` in your terminal, and run the command:

`vagrant up`

* If this is your first time running the command the virtual environment will begin setup, this can take some time. 

* Once the virtual environment is setup, run the command:

`vagrant ssh`

* This will log you into the virtual environment. 

* Navigate to the folder that contains the project files:

`cd /vagrant`

### Setup Database

* Navigate to the directory that holds the `database_setup.sql` file.
* Enter the PostgreSQL database, by typing the following into the terminal:

`psql`

* Create and connect to the `development` database, by entering:

`\i database_setup.sql`

* Check to make sure the `coders`, `programs`, and `bugs` tables have been created by entering:

`\d`

* Exit out of `psql` by entering:

`\q`

### Run the Script

* In the terminal enter:

`python bug_management.py`

* The bugs in the database will be reported.


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
