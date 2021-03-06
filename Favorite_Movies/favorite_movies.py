# Creates a web page with Paul's favorite movies

# Import from fresh_tomatoes
from fresh_tomatoes import open_movies_page, Movie

# Favorite Movies
moana = Movie(
  "Moana",
  "A story of a girl that is out to save her village",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
  "https://www.youtube.com/watch?v=LKFuXETZUsI"
)

avengers = Movie(
  "Avengers",
  "A story of Super Heros uniting to save the world",
  "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # noqa
  "https://www.youtube.com/watch?v=eOrNdBpGMv8"
)

gladiator = Movie(
  "Gladiator",
  "A story of a gladiator out of revenge",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
  "https://www.youtube.com/watch?v=owK1qxDselE"
 )

dragon = Movie(
  "How to Train Your Dragon",
  "Vikings and dragons learn to co-exist!",
  "https://images-na.ssl-images-amazon.com/images/I/91DnBoRk-WL._SL1500_.jpg",  # noqa
  "https://www.youtube.com/watch?v=oKiYuIsPxYk"
)

panda = Movie(
  "Kung Fu Panda",
  "A panda discovers the power within an saves the world",
  "http://chevaliertheatre.com/wp-content/uploads/kung.jpg",
  "https://www.youtube.com/watch?v=PXi3Mv6KMzY"
)

star_wars = Movie(
  "Star Wars",
  "A story of Jedi taking down the empire",
  "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",  # noqa
  "https://www.youtube.com/watch?v=5UfA_aKBGMc"
)

movies = [moana, avengers, gladiator, dragon, panda, star_wars]

# Display Movies
open_movies_page(movies)
