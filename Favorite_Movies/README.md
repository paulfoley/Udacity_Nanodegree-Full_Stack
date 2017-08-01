# Project - Favorite Movies

[Python](https://www.python.org/) scripts that generate a web page of my favorite movies.


## Project Overview

In this project, [Python](https://www.python.org/) code is used to create a list of movies titles, as well as their respective box art imagery and movie trailers. The [Python](https://www.python.org/) code then generates a static [HTML5](https://www.w3schools.com/html/html5_intro.asp) web page allowing a visitor to browse the movies and watch their trailers.


### Project Steps

* Create a data structure (i.e. a [Python](https://www.python.org/) Class) to store favorite movies, including movie title, box art URL (or poster URL) and a [YouTube](https://www.youtube.com/) link to the movie trailer.
* Create multiple instances of that [Python](https://www.python.org/) Class to represent my favorite movies.
* Group all the instances of movies together in a list.
* Generate a website that displays the movies.
* Ensure the website renders correctly when loaded into the browser.


## Getting Started

### Prerequisites

You'll need to install:

* [Python](https://www.python.org/)


## Python Scripts

`favorite_movies.py` - Main python script, contains the list of favorite movies and calls the open_movies_page function in the `fresh_tomatoes.py`.

`fresh_tomatoes.py` - Module has a function called `open_movies_page(movies)` that takes in one argument, which is a list of movies, and creates an [HTML5](https://www.w3schools.com/html/html5_intro.asp) file which will display all of my favorite movies.

### Running the script

`python favorite_movies.py`

### Outptut

`fresh_tomatoes.html` - Web page containing my favorite movies and their trailers!

## Authors

* **[Paul Foley](https://github.com/paulfoley)**
* [Udacity](https://www.udacity.com/)


## License

* <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/">
	<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" />
</a>


## Acknowledgments

* [YouTube](https://www.youtube.com/)
* [Rotten Tomatoes](https://www.rottentomatoes.com/)
