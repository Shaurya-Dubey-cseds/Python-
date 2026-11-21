# Banking Transaction Pattern Analysis

## 1. Project Overview

This project analyzes a synthetic banking transaction dataset using **Python, Pandas, and NumPy**. It summarizes transaction amounts, channels, cities, account types, flagged records, and possible outliers.

> **Important:** The dataset is synthetic. A flagged transaction or statistical outlier is not proof of fraud.

## 2. Project Files

Keep these files together in the same project folder:

```text
Banking-Transaction-Analysis/
├── Banking_Analysis_Pandas_Numpy_Under_90_Lines.py
├── 10_bank_transactions_500.csv
└── README.md
```

The Python script expects the dataset to be named exactly `10_bank_transactions_500.csv`.

## 3. System Requirements

- Operating system: Windows 10/11, macOS, or Linux
- Python: 3.9 or later recommended
- IDE: PyCharm or Visual Studio Code (or a terminal)
- RAM: 2 GB minimum recommended
- Disk space: approximately 100 MB free
- Internet: required to install Python packages; not required to run after installation

## 4. Required Python Libraries

This project uses only these external libraries:

- **Pandas** — reading, cleaning, grouping, and analyzing tabular data
- **NumPy** — numerical operations and percentile calculations

Install them using:

```bash
python -m pip install pandas numpy
```

To check the installation:

```bash
python -c "import pandas, numpy; print('Libraries installed successfully')"
```

## 5. Download the Project

1. Open the GitHub repository containing this project.
2. Select **Code → Download ZIP**, or clone the repository:

```bash
git clone https://github.com/Shaurya-Dubey-cseds/Python-.git
```

3. Extract the ZIP file if you downloaded it.
4. Make sure the Python script and CSV dataset are in the same folder.

## 6. Run the Project in PyCharm

1. Open PyCharm.
2. Select **Open** and choose the project folder.
3. Open the PyCharm Terminal.
4. Install the libraries:

```bash
python -m pip install pandas numpy
```

5. Check that the CSV file is in the same folder as the Python script.
6. Open `Banking_Analysis_Pandas_Numpy_Under_90_Lines.py`.
7. Click the green **Run** button.

If PyCharm uses a virtual environment, install the libraries in that same environment through the PyCharm Terminal.

## 7. Run the Project from Windows Command Prompt

1. Open Command Prompt.
2. Change to the project folder. Example:

```bat
cd path\to\Banking-Transaction-Analysis
```

3. Install the libraries:

```bat
python -m pip install pandas numpy
```

4. Run the script:

```bat
python Banking_Analysis_Pandas_Numpy_Under_90_Lines.py
```

## 8. Analysis Performed

The program performs the following tasks:

1. Loads and inspects the transaction dataset.
2. Checks missing transaction amounts and fills them using the median.
3. Checks duplicate transaction IDs.
4. Calculates total credit and debit amounts.
5. Calculates mean, median, and standard deviation.
6. Summarizes transaction count and value by channel.
7. Calculates total transaction value by city.
8. Counts flagged records and calculates their percentage.
9. Calculates flagged-record statistics by channel.
10. Finds the ten largest transactions.
11. Calculates credit and debit totals by account type.
12. Identifies possible outliers using the IQR method.
13. Groups transactions into amount ranges.
14. Uses NumPy Boolean indexing to find transactions above 10,000.
15. Prints brief operational observations.

## 9. Output Files

After a successful run, the script creates these CSV files in the current working directory:

| Output file | Description |
|---|---|
| `duplicate_transaction_ids.csv` | Records with duplicate transaction IDs |
| `channel_summary.csv` | Transaction count and total value by channel |
| `city_summary.csv` | Transaction count and total value by city |
| `flagged_by_channel.csv` | Flagged-record summary by channel |
| `top_10_transactions.csv` | Ten largest transactions |
| `account_type_totals.csv` | Credit and debit totals by account type |
| `iqr_outliers.csv` | Records outside the IQR limits |
| `amount_band_summary.csv` | Count of transactions in each amount range |
| `transactions_above_10000.csv` | Transactions greater than 10,000 |
| `banking_analysis_output.csv` | Final analyzed dataset |

## 10. Common Problems and Solutions

### `ModuleNotFoundError: No module named 'pandas'`

Install the libraries in the Python environment used to run the script:

```bash
python -m pip install pandas numpy
```

### `FileNotFoundError: 10_bank_transactions_500.csv`

- Confirm that the CSV file is present.
- Check that its filename is exactly `10_bank_transactions_500.csv`.
- Keep it in the project folder and run the script with that folder as the working directory.

### The program runs with a different Python interpreter

In PyCharm, open **Settings → Project → Python Interpreter** and select the interpreter for your project. Then install Pandas and NumPy in that interpreter.

### Output files are not visible

The output CSV files are saved in the program's current working directory. Check the Run configuration's **Working directory** in PyCharm.

## 11. Limitations

- The dataset is synthetic and may not represent real banking activity.
- Flagged records are labels for analysis, not confirmed fraud cases.
- IQR outliers are statistical observations and require context before any action.
- Results depend on the quality and structure of the input CSV file.

## 12. Author

**Shaurya Dubey**

---

If you use or modify this project, make sure the dataset filename and column names match those expected by the Python script.
