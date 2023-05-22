import random
import requests
from bs4 import BeautifulSoup

URL = "http://www.imdb.com/chart/top"


def main():
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    movie_tags = soup.select("td.titleColumn")
    inner_movie_tags = soup.select("td.titleColumn a")
    rating_tags = soup.select("td.posterColumn span[name=ir]")

    def get_year(movie_tag):
        movie_split = movie_tag.text.split()
        year = movie_split[-1]
        return year

    years = [get_year(tag) for tag in movie_tags]
    actors_list = [tag["title"] for tag in inner_movie_tags]
    titles = [tag.text for tag in inner_movie_tags]
    ratings = [float(tag["data-value"]) for tag in rating_tags]
    n_movies = len(titles)

    while True:
        idx = random.randrange(0, n_movies)
        print(f"{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}")
        user_input = input("Do you want another movie (y/[n])? ").lower()
        if user_input != "y":
            break


if __name__ == "__main__":
    main()
