# Project - Logs Analysis

Analyzing log data is common to improve web app performance as well as a security measure to find bugs, hacks, and other issues that can bring down your web application.

## Project Overview

In this project, we will use log data to answer some questions:

1) What the most popular articles visitors are reading?
2) Who are the most popular authors on our site?
3) Which days there were more then 1% load errors?


## Getting Started

### Prerequisites
You'll need to install:

* [Python 3.6](https://www.python.org/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/)

### Files

* `logs_analysis.py` - [Python](https://www.python.org/) script that creates the forum.
* `database_setup.sql` - [SQL](https://www.w3schools.com/sql/default.asp) commands to create the database as well as create the necessary tables.
* `views.sql` - [SQL](https://www.w3schools.com/sql/default.asp) commands to create the views that will be used in the log analysis.
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

To setup the database, follow these instructions:

* We will need to create the `news` database with the `articles`, `authors`, and `log` tables, as well as the neccessary views. We can do this by running the following in the terminal:

`psql -d news -a -f newsdata.sql`

`psql -d news -a -f views.sql` 

### Run the Script

* In the terminal enter:

`python logs_analysis.py`

* The queries should run and output the answer to the questions.


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
