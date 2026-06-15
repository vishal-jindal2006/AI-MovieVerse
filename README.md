# 🎬 AI MovieVerse

AI MovieVerse is an intelligent movie recommendation system that helps users discover movies based on their interests using Machine Learning techniques. The project combines Content-Based Filtering and Collaborative Filtering to generate accurate and relevant movie recommendations.

---

## 🚀 Features

✅ Hybrid Recommendation Engine

✅ Content-Based Filtering

✅ Collaborative Filtering

✅ TMDB API Integration

✅ Movie Posters

✅ Ratings & Release Dates

✅ Genres Information

✅ Cast Details

✅ Movie Overview

✅ Official Trailer Links

✅ IMDb Integration

✅ Autocomplete Movie Search

✅ Load More Recommendations

✅ Responsive Modern UI

✅ TMDB Response Caching

✅ Parallel API Requests for Faster Loading

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorization
* Cosine Similarity

### Frontend

* HTML5
* CSS3
* JavaScript

### APIs

* TMDB API (The Movie Database)

### Data Processing

* Pandas
* NumPy

---

## 🧠 Recommendation System Architecture

AI MovieVerse uses a Hybrid Recommendation System:

### 1. Content-Based Filtering

Movies are recommended based on genre similarity using:

* TF-IDF Vectorizer
* Cosine Similarity

### 2. Collaborative Filtering

Movies are recommended based on user ratings and behavior patterns from the MovieLens dataset.

### 3. Hybrid Recommendation

Results from both recommendation systems are combined to generate more accurate recommendations.

---

## ⚡ Performance Optimizations

To improve speed and user experience:

* TMDB API response caching
* Parallel API requests using ThreadPoolExecutor
* Optimized recommendation ranking
* Load More functionality
* Efficient movie lookup

---

## 📂 Project Structure

MovieVerse-AI/
│
├── app.py
│
├── config.py
│
├── dataset/
│   ├── movies.csv
│   ├── ratings.csv
│   └── links.csv
│
├── recommendation/
│   ├── content_based.py
│   ├── collaborative.py
│   ├── hybrid.py
│   └── tmdb.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md

---

## 📸 Key Features

### 🔍 Smart Search

Autocomplete-powered movie search for quick and accurate movie selection.

### 🎯 Hybrid Recommendations

Combines machine learning algorithms to provide better recommendations.

### 🎬 Rich Movie Details

Each recommendation includes:

* Poster
* Rating
* Release Date
* Genres
* Runtime
* Cast
* Overview
* Trailer Link
* IMDb Link

---

## ▶️ Installation

Clone the repository:

git clone https://github.com/vishal-jindal2006/AI-MovieVerse.git

Move into project directory:

cd MovieVerse-AI

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open browser:

http://127.0.0.1:5000

---

## 📊 Dataset

This project uses the MovieLens dataset for movie and ratings data.

Dataset includes:

* 9,700+ Movies
* 100,000+ Ratings
* 600+ Users

---

## 🎯 Future Improvements

* User Authentication
* Personalized Watchlists
* Trending Movies Section
* Movie Detail Modal
* Advanced Recommendation Models
* User Rating System
* Cloud Database Integration

---

## 👨‍💻 Developer

**Vishal Jindal**

📧 Email: [jindalvishal2006@gmail.com](mailto:jindalvishal2006@gmail.com)

---

## ⭐ Support

If you like this project, consider giving it a star on GitHub.

---

### 🎬 AI MovieVerse

**Explore Your Movie Universe**
