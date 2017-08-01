# Project - Favorite Movies

In this project we'll 

## Project Overview

In this project, we are going to help real estate agents find the best selling price for their clients homes in Boston. To do this we'll use the [Boston Housing Dataset provided by UCI](https://archive.ics.uci.edu/ml/datasets/Housing), which contains aggregated data on various features for houses in the greater Boston communities and includes the median value of homes for each of those areas. 

Our goal is to build an optimal model, based on machine learning, and then use the model to estimate the best selling price for the clients homes.

### Project Steps

* Explore the data to obtain important features and descriptive statistics about the dataset. 
* Properly split the data into testing and training subsets, and determine a suitable performance metric for this problem. 
* Analyze performance graphs for a learning algorithm with varying parameters and training set sizes. Specifically looking for variance and bias.
* Pick the optimal model that best generalizes for unseen data. 
* Test the optimal model on a new sample and compare the predicted selling price to our statistics.


## Getting Started

### Prerequisites

You'll need to install:

* [Anaconda](https://www.continuum.io/downloads)
* [Python (Minimum 3)](https://www.continuum.io/blog/developer-blog/python-3-support-anaconda)
* [Jupyter Notebook](http://ipython.org/notebook.html)
* [Pandas](https://anaconda.org/anaconda/pandas)
* [Numpy](https://anaconda.org/anaconda/numpy)
* [scikit-learn](https://anaconda.org/anaconda/scikit-learn)
* [Matplotlib](https://anaconda.org/anaconda/matplotlib)

### Data Files

* `housing.csv` - The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing).

#### Features

* `RM` - Average number of rooms per home
* `LSTAT` - Percentage of population considered lower status
* `PTRATIO` - Pupil to teacher ratio by community

#### Target Variable

* `MEDV` - Median value of owner-occupied homes


## Python Notebook and Scripts

* `Boston_Housing_Prices.ipynb` - Main project file, an IPython Notbook that contains the analysis for the project.
* `visuals.py` - A Python script containing visualization code that is run behind the scenes.

### Opening the Jupyter Notebook

The project `Boston_Housing_Prices.ipynb` can be read using a Jupyter Notebook. There's also an HTML version `Boston_Housing_Prices.html` included for easier viewability.

* Open your Command Prompt (PC) or terminal (Mac or Linux).
* On a PC click the Start button and search for "Command Prompt".
* On a Mac type command + spacebar. Then, type "terminal" in the Spotlight Search. You can also search for "terminal" in finder.
* Navigate to the directory where you downloaded the Jupyter notebook file.
* On a PC you might type: cd C:\Users\username\Downloads\, replacing your username. 
* On Mac or Linux you might type: cd ~/Downloads.
* Run the command `jupyter notebook Boston_Housing_Prices.ipynb` in your terminal.

This will open the iPython Notebook in your browser.

#### Special Note

If you try running a code block and get an error message like `no module named matplotlib`, then your distribution of [Anaconda](https://www.continuum.io/downloads) may be missing a package used in the project. That's okay – there's an easy way that you can install these packages. It's as simple as [Googling](https://www.google.com/) the library for easy to use guides on installation!


## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [UCI Datasets](https://archive.ics.uci.edu/ml/datasets/Housing)
