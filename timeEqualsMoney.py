import time
import os

def clear_console():
    """Clear the console for both Windows and Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    """Convert seconds into hours, minutes, and seconds."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    hourly_rate = float(input("Enter your hourly rate (e.g., 25.50): $"))

    print("Press Enter to start the stopwatch.")
    input()  # Wait for the user to press Enter to start
    start_time = time.time()

    try:
        while True:
            elapsed_time = time.time() - start_time  # Calculate elapsed time in seconds
            formatted_time = format_time(elapsed_time)
            
            # Calculate money earned
            earnings_per_second = hourly_rate / 3600
            money_earned = elapsed_time * earnings_per_second

            # Clear the console and print the updated time and earnings
            clear_console()
            print(f"Elapsed Time: {formatted_time}")
            print(f"Money Earned: ${money_earned:.2f}")

            # Update every second
            time.sleep(1)
    
    except KeyboardInterrupt:
        # Stop the stopwatch when the user presses Ctrl+C
        print("\nStopwatch stopped.")
        formatted_time = format_time(elapsed_time)
        print(f"Final Elapsed Time: {formatted_time}")
        print(f"Final Money Earned: ${money_earned:.2f}")

if __name__ == "__main__":
    main()