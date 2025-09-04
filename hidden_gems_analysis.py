# Import Libraries
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create folder for figures if it doesn't exist
os.makedirs("figures", exist_ok=True)

# Set seaborn style for clean visuals
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# Load Data
# Required files: books.csv, ratings.csv, book_tags.csv, tags.csv
books = pd.read_csv("books.csv")
ratings = pd.read_csv("ratings.csv")
book_tags = pd.read_csv("book_tags.csv")
tags = pd.read_csv("tags.csv")

# Clean Data
books = books.drop_duplicates()
ratings = ratings.drop_duplicates()
book_tags = book_tags.drop_duplicates()
tags = tags.drop_duplicates()

books.columns = books.columns.str.lower().str.replace(" ", "_")
if "original_publication_year" in books.columns:
    books["original_publication_year"] = (
        books["original_publication_year"].fillna(-1).astype(int)
    )

# Merge Datasets
# Compute per-book stats: number of ratings and average rating
book_stats = ratings.groupby("book_id")["rating"].agg(["count", "mean"]).reset_index()
book_stats = book_stats.rename(columns={"count": "num_ratings", "mean": "avg_rating"})

# Merge stats into books
books = books.merge(book_stats, on="book_id", how="left")

# Merge tag names to identify sci-fi books
book_tags = book_tags.merge(tags, on="tag_id", how="left")

# Filter Sci-Fi Books
sci_fi_ids = book_tags[
    book_tags["tag_name"].str.contains("science-fiction", case=False, na=False)
]["goodreads_book_id"].unique()

sci_fi_books = books[books["goodreads_book_id"].isin(sci_fi_ids)].copy()
print("Total books in dataset:", len(books))
print("Total sci-fi books:", len(sci_fi_books))

# Ratings Distribution (Context)
plt.figure(figsize=(10, 5))
sns.histplot(
    books["avg_rating"], bins=30, kde=True, color="gray", label="All Books", alpha=0.5
)
sns.histplot(
    sci_fi_books["avg_rating"],
    bins=30,
    kde=True,
    color="blue",
    label="Sci-Fi Books",
    alpha=0.5,
)
plt.title("Distribution of Average Ratings (All vs Sci-Fi)")
plt.xlabel("Average Rating")
plt.legend()
plt.tight_layout()
plt.savefig("figures/ratings_distribution.png")
plt.show()


# Hidden Gems - Books
plt.figure(figsize=(10, 6))

# Scatterplot: popularity vs quality
sns.scatterplot(data=sci_fi_books, x="num_ratings", y="avg_rating", alpha=0.6)

# Hidden gems: high rating, low number of ratings
hidden_gems = sci_fi_books[
    (sci_fi_books["avg_rating"] > 4.3) & (sci_fi_books["num_ratings"] < 500)
]
sns.scatterplot(
    data=hidden_gems,
    x="num_ratings",
    y="avg_rating",
    color="red",
    s=80,
    label="Hidden Gems",
)

# Annotate top 5 hidden gems
for _, row in hidden_gems.head(5).iterrows():
    plt.text(row["num_ratings"] + 5, row["avg_rating"], row["title"], fontsize=8)

plt.title("Sci-Fi Hidden Gems (High Rating, Low Number of Ratings)")
plt.xlabel("Number of Ratings (Popularity)")
plt.ylabel("Average Rating (Quality)")
plt.xscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("figures/hidden_gems_books.png")
plt.show()

print("Top Hidden Gem Books:")
print(hidden_gems[["title", "authors", "num_ratings", "avg_rating"]].head(10))

# Hidden Gems - Authors
# Aggregate per author: average rating and total ratings
author_stats = (
    sci_fi_books.groupby("authors")
    .agg(
        avg_rating=("avg_rating", "mean"),
        total_ratings=("num_ratings", "sum"),
        book_count=("title", "count"),
    )
    .reset_index()
)

# Hidden gem authors: high average rating, low total ratings
hidden_authors = author_stats[
    (author_stats["avg_rating"] > 4.2) & (author_stats["total_ratings"] < 1000)
]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=author_stats, x="total_ratings", y="avg_rating", alpha=0.6)
sns.scatterplot(
    data=hidden_authors,
    x="total_ratings",
    y="avg_rating",
    color="red",
    s=80,
    label="Hidden Gem Authors",
)

# Annotate top 5 authors
for _, row in hidden_authors.head(5).iterrows():
    plt.text(row["total_ratings"] + 5, row["avg_rating"], row["authors"], fontsize=8)

plt.title("Sci-Fi Hidden Gem Authors (High Rating, Low Popularity)")
plt.xlabel("Total Number of Ratings (All Books by Author)")
plt.ylabel("Average Rating")
plt.xscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("figures/hidden_gems_authors.png")
plt.show()

print("Top Hidden Gem Authors:")
print(hidden_authors[["authors", "avg_rating", "total_ratings", "book_count"]].head(10))
