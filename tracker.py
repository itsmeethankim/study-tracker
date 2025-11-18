import json
from pathlib import Path
import sys

DATA_FILE = Path("data/sessions.json") #Defines where my data file is and that is under data folder 

def main():
    if len(sys.argv) < 2:
        print("Usage python tracker.py [add | list | summary]")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        handle_add()
    elif command == "list":
        handle_list()
    elif command == "summary":
        handle_summary()
    else:
        print(f"Unknown command. {command}")



#This is how we read a .json file and then read the data from it. In another function or something
# we can call this function to get the data from the file.
def load_sessions():
    """Load sessions from the data file."""
    # TODO: Implement loading logic
    with DATA_FILE.open("r", encoding="utf-8") as file: #Open the data file in read mode
        data = json.load(file) #Read the JSON and turn into python object and store in data variable
    return data

    
def handle_add():
    print("TODO: Implement add functionality")
    
def handle_list():
    sessions = load_sessions()
    
    if not sessions:
        print("There are no sessions recorded.")
        return
    
    for s in sessions:
        course = s['course']
        duration = s['duration']
        date = s['date']
        print(f"Course: {course}, Duration: {duration}, Date: {date}")
    
def handle_summary():
    print("TODO: Implement summary functionality")
    
if __name__ == "__main__":
    main()