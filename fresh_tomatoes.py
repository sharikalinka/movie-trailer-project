import webbrowser
import os
import re

# HTML head element FYI for movie trailer page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Open+Sans:400,800">
    <link rel="stylesheet" type="text/css" href="css/main.css">

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
   
</head>
'''

# Main page layout and title bar. Inclueds YouTube movie trailer modal
main_page_content = '''
<body>
<!-- modal for video pop -->
<div class="modal" id="trailer">
    <div class="modal-dialog">
        <div class="modal-content">
<!-- modal close x -->
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24">
            </a>
            <div class="scale-media" id="trailer-video-container"></div>
        </div>
    </div>
</div>
<!-- main content -->
<header>
    <div class="content">
        <h1>The Fresh Botanical Berry (Tomato) Movies</h1>
    </div>
</header>
<div class="container">
    {movie_tiles}
</div>
<!-- footer -->
<footer class="my-hidden">
    <div class="content">
        <div class="rights">Copyright &copy; 2018 Shari Kalinka</div>
        <div class="rights">Licensed under <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International</a></div>
        <div class="rights">Background image <a href="https://i.pinimg.com/originals/0c/1b/54/0c1b541757e16d7c32736c0ec00d416f.jpg" target="_blank">Source: Taylor Cabrera | Pinterest | Blue Movie, film strip PPT Backgounds</a>, Image Source: <a href="https://pin.it/2x2yp32hyru3md" target="_blank">, Licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en" target="_blank">Creative Commons BY-NC-SA 2.0</a></div>
        <div>&bull; &bull; &bull;</div>
        <div class="disclaimer">All web pages are only for demonstration purposes. Any resemblance to real websites, living or dead, is purely coincidental.</div>
    </div>  
</footer>
</body>
</html>
'''

# HTML template for unique movie-tile
movie_tile_content = '''
<div class="col-md-4 col-lg-3 movie-tile text-center">
    <div class="movie-img" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
        <img src="{poster_image_url}">
    </div>
    <h2>{movie_title}</h2>
    <div class="year">{year}</div>
</div>
'''

def open_movies_page(movies, sort_option="none"):

    print("open_movies_page called!")

    # Sort movies array by sort_option before processing
    movies = sort_movie_data(movies, sort_option) 

    # Create or overwrite output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Swap tile placeholder with dynamically generated actual content
    rendered_content = main_page_content.format(movie_tiles=
        create_movie_tiles_content(movies))

    # Output file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Open output file in browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # If possible, open in new tab

def create_movie_tiles_content(movies):

    # The HTML content for section and page
    content = ''
    for movie in movies:
        # Get YouTube ID from URL
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = (youtube_id_match or 
            re.search(r'(?<=be/)[^&#]+', movie.trailer_url))
        trailer_youtube_id = (youtube_id_match.group(0) 
            if youtube_id_match else None)

        # Append movie tile and fill in content
        content += movie_tile_content.format(
            movie_title=movie.title,
            year=movie.year,
            poster_image_url=movie.poster_url,
            trailer_youtube_id=trailer_youtube_id)
    return content

def sort_movie_data(movies, sort_option):
    if sort_option == "none": 
        # Do not apply sort order
        return movies
    elif sort_option == "alpha":
        # Sort alphabetical by title
        movies.sort(key=lambda m: m.title, reverse=False)
        return movies
    elif sort_option == "alpha-reverse":
        # Sort reverse alphabetical by title
        movies.sort(key=lambda m: m.title, reverse=True)
        return movies
    elif sort_option == "chronological":
        # Sort chronological by year
        movies.sort(key=lambda m: m.year, reverse=False)
        return movies
    elif sort_option == "chronological-reverse":
        # Sort chronological reversed by year
        movies.sort(key=lambda m: m.year, reverse=True)
        return movies
    else:
        # DO NOT apply sort order
        return movies