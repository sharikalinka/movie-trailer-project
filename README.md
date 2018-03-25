# movie-trailer-project 

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Python Movie object class to generate a static web page, displaying a list of favorite movies and links each movie to their YouTube trailer video. The project includes CSS and jQuery involved to display the project web page.  

## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Copyright and License](#copyright-and-license)

## DemoFor demo display <https://sharikalinka.github.io/movie-trailer-project/fresh_tomatoes.html>!

## DownloadProject files may be [downloaded here](https://github.com/sharikalinka/movie-trailer-project-master.zip).

## Quick StartAfter project file download, a movie trailer page may be created by importing [media.py](https://github.com/sharikalinka/movie-trailer-project/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/sharikalinka/movie-trailer-project/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create individual movie objects by calling media.Movie() and supplying it with four arguments -- title, year, poster_url, and trailer_url. Finally, to generate movie trailers, please call fresh_tomatoes.open_movies_page() and supply it with the movie objects array you created. 

```
import media
import fresh_tomatoes

# Information for object arguments
title = "Harry Potter and the Chamber of Secrets"
year = 2002
poster_url = "http://bit.ly/2FIKwy3"
trailer = "https://www.youtube.com/watch?v=r8_iuixRa_Y"

# Create Movie object
chamber = media.Movie(title, year, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([chamber])

```

A more detailed example with multiple movie objects, which is used for the [demo](https://sharikalinka.github.io/movie-trailer-project/fresh_tomatoes.html), can be found in [entertainment_center.py](https://github.com/sharikalinka/movie-trailer-project/blob/master/entertainment_center.py) 


### Included 

in the download are directories and files:

```
movie-trailer-project-master.zip/
├── css/
│   └── main.css
├── img/
│   └── Film_Strip.jpg.jpg
├── js/
│   └── main.js
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

 The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/sharikalinka/movie-trailer-project/blob/master/media.py). 

##### Constructor Method

The constructor method is called when a new Movie object is created. It must include four arguments -- [title](#movietitle), [year](#movieyear), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each argument is discussed further below.

```
import media

#Information for object arguments
title = "Harry Potter and the Chamber of Secrets"
year = 2002
poster_url = "http://bit.ly/2FIKwy3"
trailer = "https://www.youtube.com/watch?v=r8_iuixRa_Y"

# Create Movie Object
chamber = media.Movie(title, year, poster_url, trailer_url)
```

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.year is an integer representing release year of the movie.  

###### movie.poster_url

movie.poster_url is a string containing a URL linking an image which is used to represent the Movie object, such as a movie poster or DVD cover. The movie trailer project page portion displays these images with a width of 188px and a height of 292px. Images with a ratio of 1:1.5 will work best. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL that links to a YouTube movie trailer. The movie trailer page portion of this project extracts the YouTube id from the URL. Links to other video services are valid in the Movie class object but they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's web page movie trailer. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/sharikalinka/movie-trailer-project/blob/master/fresh_tomatoes.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects) and one optional argument (a string to specify the sort order). If no sort order is specified or an unrecognized sort option is provided, the movies order will appear in the array that was used. Valid strings for specifying a sort order are:

- "none" (no sort, default)
- "alpha" (alphabetical by title)
- "alpha-reverse" (reverse alphabetical by title)
- "chronological" (chronological by year)
- "chronological-reverse" (chronological by year)

```
# Create movie trailer page with array of Movie class objects
fresh_tomatoes.open_movies_page([movie1, movie2, movie3])

# Create page with movies sorted in reverse chronological order by year 
fresh_tomatoes.open_movies_page([movie1, movie2, movie3], "chronological-reverse")

``` 

The newly generated page is placed in the same directory and named fresh_tomatoes.html. This new page has three file dependencies for the background image (img/Film_Strip.jpg), CSS style settings (css/main.css), and jQuery effects (js/main.js).

#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of the Movie class objects as an argument and iterates through each Movie object then applies the object's data to the portion of the HTML template for each movie. While iterating through each object class variable, it extracts the YouTube id from movie.trailer_url.

#### sort_movie_data

The sort_movie_data function is called by the open_movies_page function. It takes two arguments array of Movie class objects and sort_option to specify when open_movies_page was called (or "none" if no sort_option was provided). The function sorts the array, if needed and returns the array. 

## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Shari Kalinka]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

- Background image source [Pinterest](https://pin.it/2x2yp32hyru3md) used under [Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic License (BY-NC-SA)](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).