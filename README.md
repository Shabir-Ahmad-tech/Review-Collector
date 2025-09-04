
# 💎 Smart Review Collector

A simple but polished Python tool that helps businesses collect, manage, and analyze customer reviews.

Think of it as a lightweight review management system you can run straight from your terminal. Add customers, log their reviews, generate luxury-styled reports, and even export everything to CSV — all in one place.

---

## ✨ Features

* **Customer Management**
  Add customers with name, email, and purchased product. Data is stored safely in JSON files.

* **Review Collection**
  Attach reviews to customers with ratings (1–5) and comments.

* **Luxury-Styled Reports**
  Generates a neat, console-based report with stats, product breakdowns, and recent reviews.

* **CSV Export**
  Export reviews into a clean CSV file for further analysis.

* **Sample Data Generator**
  Quickly populate the system with sample customers and reviews for testing.

---

## 🚀 How to Use

1. Clone or download this repo.

2. Run the program:

   ```bash
   python app.py
   ```

3. You’ll see a luxury-styled menu like this:

   ```
   ══════════════════════════════════════════════════
               💎 SMART REVIEW COLLECTOR 💎
   ══════════════════════════════════════════════════
   1. Add Customer
   2. Add Review
   3. Generate Report
   4. Export to CSV
   5. View All Data
   6. Add Sample Data
   7. Exit
   ══════════════════════════════════════════════════
   ```

4. Pick an option and follow the prompts.

---

## 📂 Data Storage

* Customers → stored in `customers.json`
* Reviews → stored in `reviews.json`
* CSV exports → default `reviews_export.csv` (or your chosen filename)

Your data stays local, no external database needed.

---

## 🛠 Requirements

* Python 3.7+ (no external libraries required)

---

## 📊 Example Output

Here’s a snippet of what a generated report looks like:

```
╔══════════════════════════════════════════════════╗
║               LUXURY REVIEW REPORT               ║
╠══════════════════════════════════════════════════╣
║  Total Reviews: 6                                ║
║  Average Rating: 4.3/5 ⭐⭐⭐⭐                ║
╠══════════════════════════════════════════════════╣
║  Premium Watch             4.5/5 ⭐⭐⭐⭐      ║
║  Luxury Perfume            3.0/5 ⭐⭐⭐         ║
╠══════════════════════════════════════════════════╣
║                 RECENT REVIEWS                   ║
╠══════════════════════════════════════════════════╣
║  2025-09-04 14:22   5/5 Emma Johnson             ║
║    "Exceptional quality and craftsmanship..."    ║
╚══════════════════════════════════════════════════╝
```

---

## Author
*** Shabir Ahmad ***
