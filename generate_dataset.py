import csv
import random

random.seed(42)

CURRENT_YEAR = 2026

# Undergraduate (4-year, 100-400 level) departments only.
# Postgraduate programmes (PGD/MSc/M.Phil/PhD) don't use 100-400 levels,
# so they're excluded from this dataset.
DEPARTMENTS = [
    "BSc Artificial Intelligence",
    "BSc Computer Science",
    "BSc Cybersecurity",
    "BSc Information Management",
    "BSc Software Engineering",
    "BSc Information Systems",
]

# entry_year (2-digit) -> level, for the 4 currently active cohorts
ENTRY_YEAR_TO_LEVEL = {
    26: 100,
    25: 200,
    24: 300,
    23: 400,
}

STUDENTS_PER_YEAR = 3000


def generate_ids_for_year(entry_year: int, count: int) -> list:
    """Unique 5-digit IDs (00001-99999) for one entry year."""
    numbers = random.sample(range(1, 100000), count)
    return [f"{entry_year:02d}/{n:05d}" for n in numbers]


def generate_dataset() -> list:
    dataset = []
    for entry_year, level in ENTRY_YEAR_TO_LEVEL.items():
        ids = generate_ids_for_year(entry_year, STUDENTS_PER_YEAR)
        for student_id in ids:
            dataset.append({
                "Student_ID": student_id,
                "Department": random.choice(DEPARTMENTS),
                "Level": level,
                "Attendance_Percentage": round(random.uniform(50.0, 100.0), 1),
                "Average_Examination_Score": round(random.uniform(35.0, 95.0), 1),
            })
    random.shuffle(dataset)
    return dataset


def write_to_csv(dataset: list, filename: str = "student_dataset.csv") -> None:
    fieldnames = [
        "Student_ID",
        "Department",
        "Level",
        "Attendance_Percentage",
        "Average_Examination_Score",
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dataset)
    print(f"Dataset with {len(dataset)} records written to {filename}")


if __name__ == "__main__":
    dataset = generate_dataset()
    write_to_csv(dataset)

    print("\nPreview of first 5 records:")
    for row in dataset[:5]:
        print(row)
