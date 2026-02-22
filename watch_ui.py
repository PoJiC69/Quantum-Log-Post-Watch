import time

def display_watch():
    while True:
        # Get the current UTC time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        # Clear the console (works for Unix-based systems)
        print("\033c", end="")  # This may not work on all systems, consider using 'os.system("cls" if os.name == "nt" else "clear")' for cross-platform
        # Display the time
        print("Current UTC Time:\n")
        print(f"   {current_time}   ")
        print("\nPress Ctrl+C to exit.")
        time.sleep(1)

if __name__ == "__main__":
    display_watch()