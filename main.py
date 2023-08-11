import pandas
import numpy as np

movies = pandas.read_csv("movies.csv")
credits = pandas.read_csv("credits.csv")
ratings = pandas.read_csv("ratings.csv")

m = movies["vote_count"].quantile(0.9)
C = movies["vote_average"].mean()
movies_filtered = movies.copy().loc[movies["vote_count"] >= m]


def weighted_rating(df, m=m, C=C):
    R = df["vote_average"]
    v = df["vote_count"]
    wr = (v / (v+m) * R) +(m / (v+m) * C)
    return wr


movies_filtered["weighted_rating"] = movies_filtered.apply(weighted_rating, axis=1)
n = movies_filtered.sort_values("weighted_rating", ascending=False).head(10).to_dict()
print(n)
