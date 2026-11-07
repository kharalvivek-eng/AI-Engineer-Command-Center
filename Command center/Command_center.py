
import csv

print("""
        ==========================
         AI ENGINEER COMMAND CENTER
          Think. Build. Repeat.
        ==========================
""")

print("""
1. Add Study Session
2. View History
3. Search Session
4. View Statistics
5. Exit
""")

while True:

    choice = input("Enter your choice: ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Choose [1-5]")
        continue

    # 1. ADD STUDY SESSION
    if choice == "1":
        print("--- Add Study Session ---")

        study = input("What did you study? ")

        try:
            time = int(input("How many hours did you study? "))
            if time <= 0:
                print("Hours must be greater than zero.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        with open("history.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([study, time])

        print("\nSession recorded!")
        print(f"Subject: {study}")
        print(f"Hours: {time}")

    # 2. VIEW HISTORY
    elif choice == "2":
        print("--- View History ---")

        try:
            with open("history.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) >= 2:
                        print(f"{row[0]} - {row[1]} hours")

        except FileNotFoundError:
            print("No study history found.")

    # 3. SEARCH SESSIONS
    elif choice == "3":
        print("--- Search Sessions ---")

        keyword = input("Enter subject to search: ")
        found = False

        try:
            with open("history.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) >= 2 and keyword.lower() in row[0].lower():
                        print(f"{row[0]} - {row[1]} hours")
                        found = True

            if not found:
                print("No sessions found.")

        except FileNotFoundError:
            print("No study history found.")

    # 4. VIEW STATISTICS
    elif choice == "4":
        print("--- View Statistics ---")

        count = 0
        total = 0

        try:
            with open("history.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if len(row) >= 2:
                        try:
                            hours = int(row[1])
                        except ValueError:
                            continue

                        count += 1
                        total += hours

            if count > 0:
                average = total / count

                print("Total Sessions:", count)
                print("Total Study Hours:", total)
                print("Average Study Hours:", average)

            else:
                print("No study sessions found.")

        except FileNotFoundError:
            print("No study history found.")

    # 5. EXIT
    elif choice == "5":
        print("You selected: Exit")
        print("Keep learning. Keep building!")
        break
