# Daycare Fees

Python module for evaluating daycare extra-hours fees, enrolment eligibility, and child pickup status. This repository is the implementation and test suite for **SE Lab 6: Code and Branch Coverage Analysis**.

## Overview

The application logic is contained in `daycare_fees.py` and exposes three functions:

- **`extra_hours_fee(age_group, hours, has_sibling)`** — validates the age group and hours, applies included-hour allowances and sibling discounts, and calculates any additional fee.
- **`enrolment_allowed(age_months, vacancies, is_immunisation_pending)`** — determines enrolment eligibility from the child's age, available vacancies, and immunisation status.
- **`pickup_status(minutes_left, is_aftercare, is_friday)`** — classifies pickup as on time, late, or overdue according to the applicable cutoff.

## Testing and Coverage

The project uses **pytest** for automated tests and **coverage.py** to measure statement and branch coverage.

| Test suite | Purpose | Recorded result |
|---|---|---|
| `CodeCoverageTest_610_daycare_fees.py` | Exercise executable statements in the application module | 21 passed · 100% statement coverage |
| `BranchCoverageTest_610_daycare_fees.py` | Exercise decision outcomes and branches | 30 passed · 100% branch coverage |

The coverage results are measured against `daycare_fees.py`. Statement and branch coverage are run independently.

## Getting Started

### Requirements

- Python 3
- pytest
- coverage.py

Install the test dependencies:

```bash
python -m pip install pytest coverage
```

### Run statement coverage

From the repository root:

```bash
python -m coverage erase
python -m coverage run --source=daycare_fees -m pytest CodeCoverageTest_610_daycare_fees.py
python -m coverage report -m
```

### Run branch coverage

```bash
python -m coverage erase
python -m coverage run --branch --source=daycare_fees -m pytest BranchCoverageTest_610_daycare_fees.py
python -m coverage report -m
```

## Repository Structure

```text
.
├── daycare_fees.py
├── test_daycare_fees.py
├── CodeCoverageTest_610_daycare_fees.py
├── BranchCoverageTest_610_daycare_fees.py
├── screenshots/
├── .gitignore
└── README.md
```

- `daycare_fees.py` — application module under test.
- `test_daycare_fees.py` — starter test file.
- `CodeCoverageTest_610_daycare_fees.py` — expanded statement-coverage tests.
- `BranchCoverageTest_610_daycare_fees.py` — branch-coverage tests.
- `screenshots/` — terminal evidence retained for the lab submission.

## Scope

This exercise focuses on designing tests to measure code and branch coverage of the supplied daycare-fees module. The application implementation is tested as provided; the additional work is in the test suites and coverage analysis.

---

**SE Lab 6 · Code and Branch Coverage Analysis**
