# -*- coding: cp1252 -*-
# above cp code auto inserted from IDE to allow ASCII character recognition
import media
import fresh_tomatoes

"""
declare Shari's favorite movies, with 4 arguments each:
1 title (movie title)
2 year (release year)
3 poster_url (poster image url)
4 trailer_url (youtube trailer url)
"""
harry_potter_philosopher_stone = media.Movie(
    "Harry Potter and the Philosopher&#39;s Stone",
    2001,
    "http://bit.ly/2FOMZ6f",
    "https://www.youtube.com/watch?v=PbdM1db3JbY")
harry_potter_chamber_of_secrets = media.Movie(
    "Harry Potter and the Chamber of Secrets",
    2002,
    "http://bit.ly/2FIKwy3",
    "https://www.youtube.com/watch?v=r8_iuixRa_Y")
harry_potter_prisoner_of_azkaban = media.Movie(
    "Harry Potter and the Prisoner of Azkaban",
    2004,
    "http://bit.ly/2j6X3hv",
    "https://www.youtube.com/watch?v=R69laoH02xg")
harry_potter_goblet_of_fire = media.Movie(
    "Harry Potter and the Goblet of Fire",
    2005,
    "http://bit.ly/2pfPYhI",
    "https://www.youtube.com/watch?v=WVNENtEJyMM")
harry_potter_order_of_the_phoenix = media.Movie(
    "Harry Potter and the Order of the Phoenix",
    2007,
    "http://bit.ly/2FWzGUu",
    "https://www.youtube.com/watch?v=WS8Jbm8Gob4")
harry_potter_half_blood_prince = media.Movie(
    "Harry Potter and the Half-Blood Prince",
    2009,
    "http://bit.ly/2G1sNRW",
    "https://www.youtube.com/watch?v=JYLdTuL9Wjw&t=2s")
harry_potter_deathly_hallows_1 = media.Movie(
    "Harry Potter and the Deathly Hallows – Part 1",
    2010,
    "http://bit.ly/2IqZmqF",
    "https://www.youtube.com/watch?v=4fG2Q1VCm7U")
harry_potter_deathly_hallows_2 = media.Movie(
    "Harry Potter and the Deathly Hallows – Part 2",
    2011,
    "http://bit.ly/2GyKXbu",
    "https://www.youtube.com/watch?v=5NYt1qirBWg")

# Assign each movie to a movie array
movies = [harry_potter_philosopher_stone,harry_potter_chamber_of_secrets,harry_potter_prisoner_of_azkaban,harry_potter_goblet_of_fire,
    harry_potter_order_of_the_phoenix,harry_potter_half_blood_prince,harry_potter_deathly_hallows_1,harry_potter_deathly_hallows_2]

# Call movie trailer page method, pass movie array, sort option
fresh_tomatoes.open_movies_page(movies,"chronological")
