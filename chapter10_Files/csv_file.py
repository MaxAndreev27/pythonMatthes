import csv
from pathlib import Path

csv_path = Path(__file__).parent / "test.csv"

print(csv_path)
with open(csv_path, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    writer.writerow(["user_id", "user_name", "comment_qty"])
    writer.writerow([5125, "john", 12])
    writer.writerow([1245, "sam", 55])
    writer.writerow([4665, "vinny", 25])

with open(csv_path, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    for line in reader:
        print(line)

    print(reader.line_num)
