"""Compare the yfinance download with the hand-built Excel prices (sheet "Data")."""

from pathlib import Path

import pandas as pd

from ballotbeta.data import download_prices

EXCEL = Path(__file__).resolve().parents[1] / "reference" / "BallotBeta_01_Brexit_Persimmon.xlsx"

excel = pd.read_excel(EXCEL, sheet_name="Data", usecols=["Date", "PSN", "FTSE"])
excel = excel.set_index(pd.to_datetime(excel["Date"]).dt.normalize()).drop(columns="Date")

prices = download_prices(["PSN.L", "^FTSE"], "2015-01-01", "2016-07-31")

for excel_col, ticker in [("PSN", "PSN.L"), ("FTSE", "^FTSE")]:
    yahoo = prices[ticker]
    common = excel.index.intersection(yahoo.index)
    only_excel = excel.index.difference(yahoo.index)
    only_yahoo = yahoo.index.difference(excel.index)

    print(f"\n=== {excel_col} (Excel) vs {ticker} (yfinance) ===")
    print(f"Matching dates: {len(common)}")
    print(f"Only in Excel:  {len(only_excel)} {[str(d.date()) for d in only_excel]}")
    print(f"Only in Yahoo:  {len(only_yahoo)} {[str(d.date()) for d in only_yahoo]}")

    for col in ["Close", "Adj Close"]:
        diff = (excel.loc[common, excel_col] - yahoo.loc[common, col]).abs()
        print(f"Largest difference vs {col:9}: {diff.max():.4f} on {diff.idxmax().date()}")
