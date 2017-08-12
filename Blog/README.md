# Project - Blog

[Blogging](https://en.wikipedia.org/wiki/Blog) is one of the most common activities on the web!


## Project Overview

In this project, we will use [Google App Engine](https://cloud.google.com/appengine/) to create a simple blog that allows a user to enter a title and blog post, store the post, and display the blog.


## Getting Started

### Prerequisites
You'll need to install:

* [Python 2.7](https://www.python.org/)
* [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
* [Jinja2](http://jinja.pocoo.org/)

### Files

* `blog.py` - [Python](https://www.python.org/) script that creates functionality to input and display [ASCII](http://www.asciitable.com/) art.
* `app.yaml` - [Google App Engine](https://cloud.google.com/appengine/) environment file.
* `templates` - [HTML5](https://www.w3schools.com/html/) files that display the blog.
* `css` - [CSS](https://www.w3schools.com/html/html_css.asp) files for styling.


## Running the Application

This application uses [Google App Engine](https://cloud.google.com/appengine/) to run. Setup instructions can be found at [Quickstart with Google App Engine](https://cloud.google.com/appengine/docs/standard/python/quickstart).

The instructions below assume [Google App Engine](https://cloud.google.com/appengine/docs/standard/python/quickstart) is setup.

### Run the Application Locally

To run the application using the local development server, we'll use `dev_appserver.py` which is included with the [Google Cloud SDK](https://cloud.google.com/sdk/docs/). From within the directory where `app.yaml` configuration file is located, start the local development server with the following command:

`dev_appserver.py .`

The local development server is now running and listening for requests on port 8080. Visit `http://localhost:8080/` in your web browser to view the app.

The development server can be running while modifying application. The development server watches for changes in your source files and reloads them if necessary.

### Deploy the Application

To deploy the application to [Google App Engine](https://cloud.google.com/appengine/), run the following command from within the root directory where the `app.yaml` file is located:

`gcloud app deploy`

### View the Application

Launch the browser and view the app at `http://[YOUR_PROJECT_ID].appspot.com`, by runing the following command:

`gcloud app browse`

The app should now be displayed in the browser!


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [Google App Engine](https://cloud.google.com/appengine/)
