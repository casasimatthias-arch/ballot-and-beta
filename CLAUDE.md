# Ballot & Beta - project instructions

## What this is
Ballot & Beta is a public research project measuring how political and
regulatory events move stock prices, using event studies (market model,
abnormal returns, CAR/CAAR, t-stats). Tagline: "Every stock has a market
beta. I measure its ballot beta." Owner: Matthias, first-year student
learning finance and Python. Reference: MacKinlay (1997).

## How to work with me
- I am learning. Explain every new concept and every non-obvious line
  of code in plain English, briefly.
- Before writing code for anything non-trivial, show me a short plan
  and wait for my OK.
- Work in small steps. After each working step, suggest a git commit,
  but let me write the commit message.
- Never invent data, prices, dates or results. If data is missing,
  stop and tell me.
- Never write the analysis or conclusions of a study for me. You may
  fix grammar and point out weak arguments; the reasoning is mine.
- When something breaks, help me find the cause; don't fix it silently.

## Code rules
- Python 3.12, pandas, numpy, statsmodels, yfinance, matplotlib, plotly.
- Package code lives in src/ballotbeta/. One notebook per study in studies/.
- Every event is defined in events/<name>.yaml.
- Cache downloaded prices in data/cache/ (git-ignored).
- Every function in model.py has a test in tests/.
- Use trading days, not calendar days, for all windows.
- The engine must reproduce the hand-calculated benchmark in
  reference/excel-benchmark.md before any study is published.
