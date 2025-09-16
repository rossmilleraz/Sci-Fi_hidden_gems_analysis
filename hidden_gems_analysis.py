import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

# Configure logging for clean runtime messages
# Greatly helps debug 
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Apply a consistent Seaborn style
sns.set(style="whitegrid", palette="muted", font_scale=1.1)


def load_data():
    """
    load Goodbooks-10k dataset files.
    returns:
        books (pd.DataFrame), ratings (pd.DataFrame), book_tags (pd.DataFrame), tags (pd.DataFrame)
    """
    logging.info("Loading datasets...")
    books = pd.read_csv("books.csv")
    ratings = pd.read_csv("ratings.csv")
    book_tags = pd.read_csv("book_tags.csv")
    tags = pd.read_csv("tags.csv")

    return books, ratings, book_tags, tags


def clean_data(books, ratings, book_tags, tags):
    """
    clean and standardize datasets:
    remove duplicates
    standardize column names
    handle missing values for publication year
    """
    logging.info("Cleaning data...")

    books = books.drop_duplicates()
    ratings = ratings.drop_duplicates()
    book_tags = book_tags.drop_duplicates()
    tags = tags.drop_duplicates()

    books.columns = books.columns.str.lower().str.replace(" ", "_")

    if "original_publication_year" in books.columns:
        books["original_publication_year"] = (
            books["original_publication_year"].fillna(-1).astype(int)
        )

    return books, ratings, book_tags, tags


def merge_data(books, ratings, book_tags, tags):
    """
    Merge books with ratings 
    """
    logging.info("Merging datasets...")

    # Aggregate ratings per book
    book_stats = ratings.groupby("book_id")["rating"].agg(["count", "mean"]).reset_index()
    book_stats = book_stats.rename(columns={"count": "num_ratings", "mean": "avg_rating"})

    books = books.merge(book_stats, on="book_id", how="left")

    # Add tag names to book_tags
    book_tags = book_tags.merge(tags, on="tag_id", how="left")

    return books, book_tags


def filter_sci_fi_books(books, book_tags):
    """
    Filter dataset for sci-fi
    """
    logging.info("Filtering for sci-fi books...")
    sci_fi_ids = book_tags[
        book_tags["tag_name"].str.contains("science-fiction", case=False, na=False)
    ]["goodreads_book_id"].unique()

    sci_fi_books = books[books["goodreads_book_id"].isin(sci_fi_ids)].copy()

    logging.info(f"Total books: {len(books)}, Sci-Fi books: {len(sci_fi_books)}")
    return sci_fi_books


def plot_and_save(fig, filename):
    """
    Save a matplotlib figure as PNG in the 'plots' folder.
    """
    os.makedirs("plots", exist_ok=True)
    filepath = os.path.join("plots", filename)
    fig.savefig(filepath, bbox_inches="tight")
    logging.info(f"Saved plot: {filepath}")


def plot_ratings_distribution(books, sci_fi_books):
    """
    Plot and save distribution of ratings (all vs sci-fi).
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(books["avg_rating"], bins=30, kde=True, color="gray", label="All Books", alpha=0.5, ax=ax)
    sns.histplot(sci_fi_books["avg_rating"], bins=30, kde=True, color="blue", label="Sci-Fi Books", alpha=0.5, ax=ax)
    ax.set_title("Distribution of Average Ratings (All vs Sci-Fi)")
    ax.set_xlabel("Average Rating")
    ax.legend()
    plt.show()
    plot_and_save(fig, "ratings_distribution.png")


def plot_hidden_gem_books(sci_fi_books, min_rating=4.3, max_ratings=500):
    """
    Plot hidden gem sci-fi books (high rating, low number of ratings).
    """
    hidden_gems = sci_fi_books[
        (sci_fi_books["avg_rating"] >= min_rating) & (sci_fi_books["num_ratings"] <= max_ratings)
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=sci_fi_books, x="num_ratings", y="avg_rating", color="lightgray", alpha=0.5, ax=ax
    )
    sns.scatterplot(
        data=hidden_gems, x="num_ratings", y="avg_rating", color="red", s=60, label="Hidden Gems", ax=ax
    )
    ax.set_title("Hidden Gem Sci-Fi Books")
    ax.set_xlabel("Number of Ratings")
    ax.set_ylabel("Average Rating")
    ax.legend()
    plt.show()
    plot_and_save(fig, "hidden_gem_books.png")

    return hidden_gems


def plot_hidden_gem_authors(hidden_gems):
    """
    Plot authors with multiple hidden gem books.
    """
    author_counts = hidden_gems["authors"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=author_counts.values, y=author_counts.index, color="green", ax=ax)
    ax.set_title("Top Hidden Gem Sci-Fi Authors")
    ax.set_xlabel("Number of Hidden Gem Books")
    ax.set_ylabel("Author")
    plt.show()
    plot_and_save(fig, "hidden_gem_authors.png")


def main():
    # Step 1: Load
    books, ratings, book_tags, tags = load_data()

    # Step 2: Clean
    books, ratings, book_tags, tags = clean_data(books, ratings, book_tags, tags)

    # Step 3: Merge
    books, book_tags = merge_data(books, ratings, book_tags, tags)

    # Step 4: Filter Sci-Fi
    sci_fi_books = filter_sci_fi_books(books, book_tags)

    # Step 5: Visualizations
    plot_ratings_distribution(books, sci_fi_books)
    hidden_gems = plot_hidden_gem_books(sci_fi_books)
    plot_hidden_gem_authors(hidden_gems)


if __name__ == "__main__":
    main()
