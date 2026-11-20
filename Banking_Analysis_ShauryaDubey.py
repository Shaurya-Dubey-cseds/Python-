#Name-Shaurya Dubey
#GIthub Repository Link-https://github.com/Shaurya-Dubey-cseds/Python-.git
#Admission Number-2026B15410215
#User Id-shaurya.26b15410215@abes.ac.in
import pandas as pd
import numpy as np
df = pd.read_csv("10_bank_transactions_500.csv")
print("139. Dataset shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe(include="all"))
amount = "Transaction_Amount"
missing = df[amount].isna().sum()
df[amount] = pd.to_numeric(df[amount], errors="coerce")
median = df[amount].median()
df[amount] = df[amount].fillna(median)
print("\n140. Missing amounts:", missing, "| Filled with median:", median)
duplicates = df[df["Transaction_ID"].duplicated(keep=False)]
print("\n141. Duplicate IDs:", df["Transaction_ID"].duplicated().sum())
duplicates.to_csv("duplicate_transaction_ids.csv", index=False)
kind = df["Transaction_Type"].astype(str).str.lower().str.strip()
credit = kind == "credit"
debit = kind == "debit"
credits, debits = df.loc[credit, amount].sum(), df.loc[debit, amount].sum()
print("\n142. Credits:", credits, "| Debits:", debits)
print("\n143. Mean:", df[amount].mean(), "Median:", df[amount].median(),
      "Standard deviation:", df[amount].std())
channel = df.groupby("Channel").agg(
    Transaction_Count=(amount, "count"), Total_Value=(amount, "sum"))
print("\n144. Channel summary:\n", channel)
channel.to_csv("channel_summary.csv")
city = df.groupby("City")[amount].agg(["count", "sum"])
city.columns = ["Transaction_Count", "Total_Value"]
print("\n145. City summary:\n", city)
city.to_csv("city_summary.csv")
flag = df["Flagged"].astype(str).str.lower().str.strip().isin(
    ["yes", "true", "1", "flagged"])
df["Flagged_Binary"] = flag.astype(int)
flag_count = flag.sum()
flag_percent = flag.mean() * 100
print("\n146. Flagged:", flag_count, "Percentage:", round(flag_percent, 2), "%")
flag_channel = df.groupby("Channel")["Flagged_Binary"].agg(["count", "sum", "mean"])
flag_channel["mean"] = flag_channel["mean"] * 100
print("\n147. Flagged percentage by channel:\n", flag_channel)
flag_channel.to_csv("flagged_by_channel.csv")
top10 = df.nlargest(10, amount)
print("\n148. Top 10 transactions:\n", top10)
top10.to_csv("top_10_transactions.csv", index=False)
account = df.groupby(["Account_Type", "Transaction_Type"])[amount].sum().unstack(fill_value=0)
print("\n149. Account type totals:\n", account)
account.to_csv("account_type_totals.csv")
q1, q3 = np.percentile(df[amount], [25, 75])
iqr = q3 - q1
outliers = df[(df[amount] < q1 - 1.5 * iqr) | (df[amount] > q3 + 1.5 * iqr)]
print("\n150. IQR outliers:", len(outliers))
outliers.to_csv("iqr_outliers.csv", index=False)
df["Amount_Band"] = pd.cut(df[amount], [-np.inf, 1000, 5000, 10000, 50000, np.inf],
    labels=["Below 1,000", "1,000-5,000", "5,000-10,000", "10,000-50,000", "Above 50,000"])
bands = df["Amount_Band"].value_counts(sort=False)
print("\n151. Amount bands:\n", bands)
bands.to_csv("amount_band_summary.csv")
high = df.loc[df[amount].to_numpy() > 10000]
print("\n152. Transactions above 10,000:", len(high))
high.to_csv("transactions_above_10000.csv", index=False)
print("\n153. OBSERVATIONS")
print("1. Highest-volume channel:", channel["Transaction_Count"].idxmax())
print("2. Highest-value city:", city["Total_Value"].idxmax())
print("3. Flagged records:", flag_count, "(", round(flag_percent, 2), "% )")
print("4. IQR outliers:", len(outliers), "- review in context; not necessarily suspicious.")
print("5. Compare credit/debit totals over time before changing banking policies.")
df.to_csv("banking_analysis_output.csv", index=False)
print("\nAnalysis completed. Results saved as CSV files.")
print("Note: Data is synthetic; Flagged labels are not proof of fraud.")
