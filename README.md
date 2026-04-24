#  News App

A simple desktop news application built using Python and Tkinter that fetches the latest news using the News API and displays it in a clean GUI.

---

## Features

* Fetches latest news articles
* Displays title, description, and image
* "Next" and "Previous" navigation
* "Read More" button opens full article in browser
* Handles missing images with a placeholder

---

## Tech Stack

* Python
* Tkinter (GUI)
* Requests (API calls)
* Pillow (image handling)
* python-dotenv (environment variables)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-app.git
cd news-app
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup environment variables

Create a `.env` file in the root directory:

```
NEWS_API_KEY=your_api_key_here
```

⚠️ Do NOT share or upload this file.

---

### 4. Run the app

```bash
python inshorts-clone.py
```

---

## Project Structure

```
news-app/
│── inshorts-clone.py
│── requirements.txt
│── .env.example
│── .gitignore
```

---

## Environment Variables

Create a `.env.example` file:

```
NEWS_API_KEY=your_api_key_here
```

Users should copy it:

```bash
cp .env.example .env
```

---

## Common Issues

**API key shows None**

* Check `.env` file name (not `.env.txt`)
* Ensure it's in the correct directory
* Make sure encoding is UTF-8

**No articles error**

* Verify API key is valid
* Check API response using `print()`

---

## Future Improvements

* Add search functionality
* Add categories (sports, tech, etc.)
* Improve UI/UX
* Add loading indicators

---

## License

This project is open-source and free to use.
