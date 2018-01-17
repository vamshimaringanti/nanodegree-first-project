import media
import fresh_tomatoes

# Create a Movie instance toy_story
toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=NTdKQzVFeis")

# Create a Movie instance avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Create a Movie instance baahubali
baahubali = media.Movie("Baahubali",
                        "A revenge story of cousins in a war of lust for women and power",
                        "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                        "https://www.youtube.com/watch?v=VdafjyFK3ko")

# Create a Movie instance baahubali2
baahubali2 = media.Movie("Baahubali 2",
                        "Part 2 - A revenge story of cousins in a war of lust for women and power",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=G62HrubdD6o")

# Create a Movie instance hunger_games
hunger_games = media.Movie("Hunger Games",
                        "Really realistic reality movie",
                        "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                        "https://www.youtube.com/watch?v=mfmrPu43DF8")

# Create a Movie instance dangal
dangal = media.Movie("Dangal",
                     "A story of how a women conquered boxing ring",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

# Create a list of all Movie instances
movies_list = [toy_story, avatar, baahubali, baahubali2, hunger_games, dangal]

# call open_movies_page function
fresh_tomatoes.open_movies_page(movies_list)
