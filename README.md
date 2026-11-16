# Fictional Student Dataset

**Name:** Jim Joseph Onyedikachi
**Matric Number:** 24/15932
**Department:** Computer Science

A Python project that generates a fictional dataset of 20 university students.

## Fields

| Column | Description |
|--------|-------------|
| Student ID | Format `YY/NNNNN`, where the year prefix depends on level |
| Department | Computer Science, Cyber Security or Software Engineering |
| Level | 100, 200, 300 or 400 |
| Attendance Percentage | Between 40 and 100 |
| Average Examination Score | Between 20 and 100 (loosely tied to attendance) |

## Student ID format

| Level | ID prefix | Example |
|-------|-----------|---------|
| 100 | 26 | 26/12345 |
| 200 | 25 | 25/12345 |
| 300 | 24 | 24/12345 |
| 400 | 23 | 23/12345 |

## How to run

```bash
python generate_dataset.py
```

This creates `student_dataset.csv` in the same folder. A fixed random seed is
used, so the same dataset is produced every time.

## Files

- `generate_dataset.py` - the Python script that generates the data
- `student_dataset.csv` - the generated dataset (20 records)

All data is randomly generated and fictional.
