# This program adds a log entry, reads and prints all logs.

# append mode
def add_log(log_value):
    with open("File IO/logs.txt", "a") as f:
        f.write(log_value + "\n")

# read mode
def read_logs():
    with open("File IO/logs.txt", "r") as f:
        data = f.read()
        print(data)

log_value = input("Enter log entry: ")
add_log(log_value)
read_logs()