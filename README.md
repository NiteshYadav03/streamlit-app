# Streamlit App: Chapter-wise Guide

This repository contains a series of Streamlit app chapters, each demonstrating different features and capabilities of Streamlit. Below is a chapter-wise overview:

---

## Chapter 1: Basic Streamlit App

- Introduces the basics of Streamlit.
- Displays titles, subheaders, and text.
- Demonstrates the use of a `selectbox` for user input.
- Shows how to display user selections and success messages.

**File:** [chapter-1.py](chapter-1.py)

---

## Chapter 2: User Input Widgets

- Explores various Streamlit widgets for user input:
  - Button
  - Checkbox
  - Radio buttons
  - Slider
  - Text input
  - Number input
  - Date input
- Handles user interactions and displays responses.

**File:** [chapter-2.py](chapter-2.py)

---

## Chapter 3: Layouts, Sidebar, and Markdown

- Demonstrates layout management using columns.
- Shows how to add a sidebar for user preferences.
- Uses expanders for additional options.
- Includes a Markdown example with formatted text and code blocks.

**File:** [chapter-3.py](chapter-3.py)

---

## Chapter 4: Data Analysis and Visualization

- Allows users to upload a CSV file (sample: [cars.csv](cars.csv)).
- Displays a preview of the uploaded data.
- Shows descriptive statistics of the data.
- Visualizes data using bar, line, and area charts.

**File:** [chapter-4.py](chapter-4.py)

---

## Chapter 5: Live Currency Converter

- Implements a live currency converter using an external API.
- Takes user input for the amount in USD.
- Fetches real-time exchange rates.
- Converts the amount to a selected currency and displays the result.

**File:** [chapter-5.py](chapter-5.py)

---

## Requirements

- Python 3.12+
- Streamlit (see [pyproject.toml](pyproject.toml) for dependencies)

## Getting Started

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    Or use the dependencies listed in [pyproject.toml](pyproject.toml).

2. Run a chapter:
    ```sh
    streamlit run chapter-1.py
    ```
    Replace `chapter-1.py` with any chapter file you want to explore.

---

## License

This project is