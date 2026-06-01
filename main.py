import csv

def load_tasks(file_path):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == "__main__":
    print("Trade Automation Pipeline")
