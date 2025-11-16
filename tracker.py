import sys

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
        print("Unknown command. {command}")
    
    
def handle_add():
    print("TODO: Implement add functionality")
    
def handle_list():
    print("TODO: Implement list functionality")
    
def handle_summary():
    print("TODO: Implement summary functionality")
    
if __name__ == "__main__":
    main()