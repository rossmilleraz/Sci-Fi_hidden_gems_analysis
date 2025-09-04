# Sci-Fi Books Analysis

## Executive Summary
I explored the Goodbooks-10k dataset to understand trends, ratings, and popularity in science fiction books. Beyond looking at the usual top-rated and most popular titles, I wanted to dig a little deeper to find “hidden gems”—books and authors that are highly rated but haven’t gotten as much attention. This project combines data cleaning, analysis, and visualization to highlight trends and uncover actionable insights for publishers, book platforms, or anyone interested in discovering underrated sci-fi reads.

---

## The Business Problem
Publishers and book platforms often face the challenge of deciding which books to promote or highlight. Popular titles dominate attention, but there are likely high-quality books that fly under the radar. The key question I aimed to answer was:

**Which sci-fi books and authors are hidden gems—well-loved by those who read them, but not widely discovered?**

---

## Methodology
Here’s the approach I took:
1. **Data Loading**  
   Loaded `books.csv`, `ratings.csv`, `book_tags.csv`, and `tags.csv` from the [Goodbooks-10k dataset](https://github.com/zygmuntz/goodbooks-10k).

2. **Data Cleaning**  
   Removed duplicates, standardized column names, and handled missing publication years.

3. **Data Merging**  
   Calculated the number of ratings and average rating per book, then merged these stats with the book dataset. Added tag names to identify science fiction books.

4. **Filtering Sci-Fi Books**  
   Selected all books tagged as “science-fiction.”

5. **Exploratory Data Analysis (EDA)**  
   - Compared average ratings of sci-fi books vs. all books.  
   - Identified top authors and most-rated books.  
   - Looked at publications per decade.

6. **Hidden Gems Analysis**  
   Found books with high ratings but low number of ratings. Did the same for authors with consistently high-rated but under-the-radar books.

7. **Visualization**  
   Used Matplotlib and Seaborn to create plots for rating distributions, publication trends, top authors, top books, and hidden gems.

---

## Skills Demonstrated
- Data cleaning and wrangling with pandas  
- Aggregation, grouping, and filtering for EDA  
- Visualization with Matplotlib and Seaborn  
- Creating reproducible, portfolio-ready Python code  
- Translating data into business insights and recommendations

---

## Key Findings
- The dataset has about 10,000 books, with ~800 tagged as sci-fi.  
- Sci-fi books have a slightly higher average rating (~3.95) than the overall average (~3.9).  
- Sci-fi publications surged after 1960, especially post-1980.  
- Top authors include Isaac Asimov, Arthur C. Clarke, and Philip K. Dick.  
- Most-rated books include classics like *Dune* and *Ender’s Game*.  
- Hidden gems reveal books and authors with high ratings but low visibility—potential candidates for promotion or recommendations.

---

## Business Recommendations
1. **Promote Hidden Gems**  
   Include highly-rated but lesser-known books and authors in recommendations, newsletters, or curated lists.

2. **Spotlight Underrated Authors**  
   Highlight authors whose work is consistently good but under-read.

3. **Marketing & Reprints**  
   Consider reissuing older sci-fi books with strong ratings or creating themed collections.

4. **Publishing Insights**  
   Use publication trends by decade to inform reprint strategies or curated collections.

---

## What’s Next
- Dive deeper into sub-genres like cyberpunk, space opera, or dystopian sci-fi.  
- Track how book ratings evolve over time.  
- Build interactive dashboards for exploring hidden gems dynamically.  
- Analyze author-level metrics more granularly (splitting multi-author books).  
- Explore NLP techniques to analyze book descriptions or reviews for trends.

---

## Dataset
- [Goodbooks-10k Dataset](https://github.com/zygmuntz/goodbooks-10k)  
- Files used: `books.csv`, `ratings.csv`, `book_tags.csv`, `tags.csv`

---

## How to Run
1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install pandas matplotlib seaborn
