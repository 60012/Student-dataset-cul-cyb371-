# Student-dataset-cul-cyb371-

# Fictional Student Dataset — CUL-CYB 371 Assignment Two

A Python script that generates a fictional student dataset covering
undergraduate (100–400 level) programmes in the College of Computing and
Information System.

## Student ID scheme

Format: `YY/NNNNN` (year of entry / random 5-digit number), e.g. `24/35677`.

Level is derived from year of entry relative to the current academic year
(2026):

| Year of Entry | Level |
|---|---|
| 26 | 100lvl |
| 25 | 200lvl |
| 24 | 300lvl |
| 23 | 400lvl |

Up to 3,000 fictional students are generated per entry year (4 years ×
3,000 = 12,000 students total).

## Departments

Only undergraduate (4-year, 100–400 level) programmes are included —
postgraduate programmes (PGD/M.Sc/M.Phil/Ph.D) don't use a 100–400 level
structure, so they're excluded:

- BSc Artificial Intelligence
- BSc Computer Science
- BSc Cybersecurity
- BSc Information Management
- BSc Software Engineering
- BSc Information Systems

## Fields

| Field | Description |
|---|---|
| Student_ID | `YY/NNNNN` identifier (year of entry / random number) |
| Department | Undergraduate programme |
| Level | Academic level (100, 200, 300, or 400), derived from year of entry |
| Attendance_Percentage | Attendance rate (%) |
| Average_Examination_Score | Average exam score (%) |

## Usage

```bash
python3 generate_dataset.py
```

This creates `student_dataset.csv` in the same directory (12,000 rows at
default settings; remove the `random.seed(42)` line for different random
data on each run).

## Files

- `generate_dataset.py` — the generator script
- `student_dataset.csv` — the generated dataset
