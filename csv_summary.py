
import csv
from collections import Counter

# Step 1: Specify the CSV file name
file_name = "employees.csv"

# Step 2: Specify which column we want to count
column_name = "department"

# Step 3: Create an empty counter
department_counts = Counter()

# Step 4: Keep track of total records
total_records = 0

# Step 5: Open and read the CSV file
with open(file_name, "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    # Step 6: Read each row one by one
    for row in reader:

        total_records += 1

        department = row[column_name].strip()

        if department:
            department_counts[department] += 1
        else:
            department_counts["(blank)"] += 1

# Step 7: Print the summary
print("========== CSV SUMMARY ==========")

print(f"\nTotal records: {total_records}")

print("\nDepartment counts:")

for department, count in department_counts.items():
    print(f"{department}: {count}")

print("\n=================================")
