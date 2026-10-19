# Excel benchmark - Study 01: Brexit and Persimmon

These numbers were calculated by hand in
`reference/BallotBeta_01_Brexit_Persimmon.xlsx`. The Python engine must
reproduce them before any study is published.

## Setup
- Stock: Persimmon (PSN.L)
- Benchmark: FTSE 100
- Estimation window: 1 Jun 2015 to 20 May 2016 (248 daily returns)
- Event window: 23, 24 and 27 Jun 2016 (days -1, 0, +1)

## Market model (estimation window)
| Parameter      | Value    |
|----------------|----------|
| Alpha (per day)| 0.000758 |
| Beta           | 0.7636   |
| Residual sigma | 0.01591  |
| R^2            | 0.260    |

## Abnormal returns (event window)
| Day | Date        | Abnormal return |
|-----|-------------|-----------------|
| -1  | 23 Jun 2016 | -0.44%          |
| 0   | 24 Jun 2016 | -25.22%         |
| +1  | 27 Jun 2016 | -11.94%         |

## Cumulative result
- CAR (-1 to +1): -37.61%
- t-stat of the CAR: -13.65

## Tolerance
Small differences are expected if the engine uses adjusted prices.
A CAR difference above 0.5 percentage points means a bug.
