# Sci-Fi Hidden Gems Analysis

## Executive Summary
This project explores the Goodbooks-10k dataset to uncover “hidden gems” in science fiction—books and authors that are highly rated but haven’t received much attention. The goal is to identify under-the-radar titles that could be promoted or recommended to readers, helping publishers, platforms, and book enthusiasts discover quality content that might otherwise be overlooked.

---

## Business Problem
Platforms and publishers often focus on the most popular books, which can leave high-quality but lesser-known titles unnoticed. The central question this project addresses is:

**Which sci-fi books and authors are hidden gems—highly rated, but under-the-radar?**

---

## Methodology
1. **Data Loading & Cleaning**  
   Loaded books, ratings, and tag data, removed duplicates, standardized column names, and handled missing publication years.

2. **Filter Sci-Fi Books**  
   Selected books tagged as “science-fiction” using the Goodbooks-10k tags.

3. **Hidden Gems Analysis**  
   - **Books:** Identified books with high average ratings but low number of ratings.  
   - **Authors:** Identified authors with consistently high-rated works but relatively low total ratings.

4. **Visualization**  
   - Ratings distribution for context: all books vs. sci-fi books.  
   - Scatterplots highlighting hidden gem books and authors.  
   - Annotated top hidden gems for easy identification.

---

## Key Findings
- Hidden gems exist across the dataset: high-quality books that are not widely read.  
- Examples include books with >4.3 average rating but <500 ratings.  
- Authors with consistently high-rated but low-popularity works represent opportunities to diversify recommendations.  
- These insights can help platforms highlight quality content that may otherwise go unnoticed.

---

## Business Recommendations
1. **Promote Hidden Gems**  
   Feature these books and authors in recommendation engines, curated lists, or newsletters.

2. **Spotlight Underrated Authors**  
   Highlight authors with strong but under-recognized works to boost engagement.

3. **Marketing Opportunities**  
   Reissue older high-quality books or create themed collections featuring hidden gems.

---

## Next Steps
- Explore sub-genres (cyberpunk, dystopian, space opera) for hidden gems.  
- Develop an interactive dashboard for users to filter and discover hidden gems dynamically.  
- Refine author-level metrics to handle multi-author books individually.  
- Analyze book descriptions or reviews to uncover additional trends or quality signals.

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

