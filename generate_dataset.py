"""
Name:          Jim Joseph Onydeikachi
Matric Number: 24/15932
Department:    Computer Science

Fictional Student Dataset Generator
-----------------------------------
Generates a fictional dataset of students with:
  1. Student ID
  2. Department
  3. Level
  4. Attendance Percentage
  5. Average Examination Score

Student ID format (YY/NNNNN) depends on the level:
  100 level -> 26/xxxxx
  200 level -> 25/xxxxx
  300 level -> 24/xxxxx
  400 level -> 23/xxxxx

All data is randomly generated and fictional.
"""

import csv
import random

# Seed so that the same dataset is produced every time the script is run
random.seed(42)

NUM_STUDENTS = 20
OUTPUT_FILE = "student_dataset.csv"

DEPARTMENTS = ["Computer Science", "Cyber Security", "Software Engineering"]

# Level -> year prefix used in the student ID
LEVEL_PREFIX = {
    100: "26",
    200: "25",
    300: "24",
    400: "23",
}


def generate_student_id(level, used_ids):
    """Create a unique ID like 24/12345 based on the student's level."""
    prefix = LEVEL_PREFIX[level]
    while True:
        number = random.randint(10000, 99999)
        student_id = f"{prefix}/{number}"
        if student_id not in used_ids:
            used_ids.add(student_id)
            return student_id


def generate_attendance():
    """Attendance percentage between 40 and 100."""
    return round(random.uniform(40, 100), 1)


def generate_exam_score(attendance):
    """
    Average exam score between 20 and 100.
    Students with higher attendance tend to score slightly higher,
    which makes the dataset more realistic.
    """
    base = 20 + (attendance - 40) * 0.8   # rises with attendance
    noise = random.uniform(-12, 12)
    score = max(20, min(100, base + noise))
    return round(score, 1)


def generate_dataset(n):
    used_ids = set()
    rows = []
    for _ in range(n):
        level = random.choice(list(LEVEL_PREFIX.keys()))
        attendance = generate_attendance()
        rows.append({
            "Student ID": generate_student_id(level, used_ids),
            "Department": random.choice(DEPARTMENTS),
            "Level": level,
            "Attendance Percentage": attendance,
            "Average Examination Score": generate_exam_score(attendance),
        })
    # Sort by level then ID for a neat file
    rows.sort(key=lambda r: (r["Level"], r["Student ID"]))
    return rows


def save_to_csv(rows, filename):
    fieldnames = [
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score",
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    data = generate_dataset(NUM_STUDENTS)
    save_to_csv(data, OUTPUT_FILE)
    print(f"Dataset created: {OUTPUT_FILE} ({len(data)} students)")
    print("\nFirst 5 records:")
    for row in data[:5]:
        print(row)
