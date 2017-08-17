# Project - ASCII Art

[API](https://en.wikipedia.org/wiki/Application_programming_interface)'s are an integral part of web applications.


## Project Overview

In this project, we will build an example API Server to show [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (Create, Read, Update, and Delete) operations.


## Getting Started

### Prerequisites
You'll need to install:

* [Python 3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/)

### Files

* `api_server.py` - [Python](https://www.python.org/) script that mimics an API server using [Flask](http://flask.pocoo.org/).
* `Vagrantfile` - A [Vagrant](https://www.vagrantup.com/downloads.html) file to setup the virtual environment.


## Running the Application

This application uses [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) to create a virtual environment. We will need both of these programs to run the application. Setup and download instructions can be found on there various sites.

The instructions below assume that both [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/) are setup.

### Run the Application

To run the application we'll first need to spin up the virtual environment. Navigate to the folder containing the `Vagrantfile` in your terminal, and run the command:

`vagrant up`

If this is your first time running the command the virtual environment will begin setup, this can take some time. Once the virtual environment is setup, run the command:

`vagrant ssh`

This will log you into the virtual environment. Navigate to the folder that contains the `api_server.py` script:

`cd /vagrant`

Now you can run the python application:

`python api_server.py`

The local development server is now running and listening for requests on port 5000. Visit `http://localhost:5000/` in a web browser to view the app.

The development server can be running while modifying the application. The development server watches for changes in the source files and reloads them if necessary.


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [Flask](http://flask.pocoo.org/)
