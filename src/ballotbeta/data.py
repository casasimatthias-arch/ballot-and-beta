"""Download daily prices with yfinance and cache them as CSV files."""

from pathlib import Path

import pandas as pd
import yfinance as yf

# data/cache/ at the project root (this file is src/ballotbeta/data.py)
CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "cache"


def _cache_path(ticker: str, start: str, end: str) -> Path:
    # "^FTSE" -> "FTSE" so the file name is safe on Windows
    safe = ticker.replace("^", "").replace(".", "_")
    return CACHE_DIR / f"{safe}_{start}_{end}.csv"


def download_prices(tickers: list[str], start: str, end: str) -> dict[str, pd.DataFrame]:
    """Return {ticker: DataFrame with columns Close and Adj Close}, indexed by date.

    start and end are "YYYY-MM-DD". end is INCLUSIVE here: yfinance treats
    end as exclusive, so we ask it for one extra day.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    yf_end = (pd.Timestamp(end) + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    result = {}

    for ticker in tickers:
        path = _cache_path(ticker, start, end)

        if path.exists():
            df = pd.read_csv(path, index_col="Date", parse_dates=True)
            print(f"{ticker}: loaded from cache ({path.name})")
        else:
            # auto_adjust=False keeps both the plain Close and the Adj Close columns
            raw = yf.download(ticker, start=start, end=yf_end,
                              auto_adjust=False, progress=False)
            if raw.empty:
                raise ValueError(f"No data returned for {ticker} ({start} to {end}).")
            # yfinance returns two-level column names (field, ticker); keep only the field
            if isinstance(raw.columns, pd.MultiIndex):
                raw.columns = raw.columns.get_level_values(0)
            df = raw[["Close", "Adj Close"]]
            df.index.name = "Date"
            df.to_csv(path)
            print(f"{ticker}: downloaded from the internet, saved to {path.name}")

        result[ticker] = df

    return result
