# expense-tracker

## Overview
This is a Flask-based web application that helps users track their income and expenses. It provides insights through monthly budget reports, visualizations of income versus expenses, and categorization of transactions.

---

## Features
- **Add Transactions**: Log income or expenses with categories, descriptions, and dates.
- **Monthly Reports**: Get total income, total expenses, and remaining balance.
- **Visualization**:
  - Pie chart for expense distribution by category.
  - Bar chart for income vs. expenses comparison.
- **Recent Transactions**: Display the latest 5 transactions.
- **Responsive Design**: Built using TailwindCSS and Chart.js for clean and interactive UI.

---

## Setup Instructions

### Prerequisites
Ensure the following are installed:
- Python 3.8 or later
- Flask (`pip install flask`)
- Chart.js (CDN included in HTML)
- TailwindCSS (CDN included in HTML)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/` to view the application.

---

## Folder Structure
```
expense-tracker/
├── app.py             # Main Flask application
├── templates/
│   ├── index.html     # Main dashboard page
├── static/
│   └── styles.css     # Custom styles (optional)
├── expenses.json      # Data storage for transactions
├── requirements.txt   # Python dependencies
```

---

## Usage
1. **Add Transactions**: Fill out the form on the dashboard to log your income or expenses.
2. **View Reports**: Check monthly income, expenses, and balance.
3. **Visualize Data**: Use the charts to analyze expense distribution and income versus expenses.
4. **Recent Transactions**: Review the last five logged transactions.

---

## Technologies Used
- **Back-End**: Flask (Python)
- **Front-End**: HTML, TailwindCSS, Chart.js
- **Database**: JSON file for local storage

---

## Future Enhancements
- Add user authentication.
- Enable cloud storage (e.g., Firebase, AWS).
- Provide yearly reports and export options (PDF/CSV).
- Integrate email notifications for budget overspending.

