# 🍿 CineSync: Intelligent Movie Matchmaker

CineSync is a sleek, AI-powered movie recommendation engine built on Django and advanced machine learning algorithms. By leveraging content-based filtering (TF-IDF & SVD), CineSync analyzes thousands of movies to find the perfect match for your movie nights.

No more endless scrolling. Tell CineSync a movie you love, and it handles the rest.

---

## ✨ What Makes CineSync Special?

* **🧠 Smart Recommendations:** Uses natural language processing on movie plots, genres, and metadata to find visually and thematically similar films.
* **⚡ Blazing Fast:** Built to handle anything from a small curations of 2K movies to massive 1M+ movie datasets with sub-50ms query times.
* **🔎 Intelligent Search:** Fuzzy-matching autocomplete ensures you find the movie you're looking for, even if you misspell it.
* **📱 Beautiful Interface:** A responsive, mobile-friendly web UI that looks great on any device.
* **🔌 REST API Ready:** Easily integrate CineSync's logic into other frontends or mobile apps.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, Django 6.0
* **Data Science:** Scikit-Learn, Pandas, NumPy
* **Storage:** Parquet (for highly efficient vector storage)
* **Frontend:** HTML5, CSS3, Vanilla JS
* **Deployment Support:** Ready for Heroku, Render, and Docker

---

## 🚀 Quick Setup Guide

Get CineSync running on your local machine in minutes using our pre-built demo model!

### 1. Clone & Enter
```bash
git clone https://github.com/Mehak-991/cinesync.git
cd cinesync
```

### 2. Setup Virtual Environment
```bash
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies & Migrate
```bash
pip install -r requirements.txt
python manage.py migrate
```

### 4. Launch the Server
```bash
python manage.py runserver
```
Visit `http://localhost:8000` in your browser. The app works right out of the box with the included 2,000-movie dataset!

---

## 🧠 Training Your Own Model

Want to scale up? CineSync includes a complete training pipeline.
Check out `training/guide.md` for detailed instructions on how to feed the system larger TMDB datasets and configure the SVD dimensionality reduction.

## 🤝 Contributing
Contributions, issues, and feature requests are always welcome! Feel free to check the issues page if you want to contribute.

## 📄 License
This project is open-source and ready for the world.
