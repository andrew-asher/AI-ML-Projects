# Book Recommendation Engine using KNN

## Project Overview

This project is a book recommendation system developed using the K-Nearest Neighbors (KNN) algorithm. It uses the Book-Crossings dataset, which contains 1.1 million ratings of 270,000 books by 90,000 users, to recommend similar books based on user ratings.

## Dataset

The dataset used in this project is the Book-Crossings dataset. It includes:
- **Ratings:** 1.1 million ratings on a scale of 1-10.
- **Books:** Information on 270,000 books.
- **Users:** Ratings from 90,000 users.

## Project Structure

The project consists of a single Jupyter notebook file, which includes the following main sections:

1. **Import Libraries:**
   - Import necessary libraries such as NumPy, pandas, scipy, and sklearn.

2. **Load Data:**
   - Download and unzip the dataset files.
   - Load the books and ratings data into pandas dataframes.

3. **Data Cleaning and Filtering:**
   - Filter out users with fewer than 200 ratings and books with fewer than 100 ratings to ensure statistical significance.

4. **Merge Data:**
   - Merge the ratings data with book titles.

5. **Create User-Item Matrix:**
   - Create a user-item matrix where rows represent books and columns represent users. The values in the matrix are the ratings.

6. **Train KNN Model:**
   - Use the NearestNeighbors model from sklearn to fit the user-item matrix.

7. **Recommendation Function:**
   - Implement the `get_recommends` function to find and return the top 5 similar books to a given book.

8. **Testing:**
   - Test the `get_recommends` function with provided test cases.

## Installation and Usage

To run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/book-recommendation-engine.git
