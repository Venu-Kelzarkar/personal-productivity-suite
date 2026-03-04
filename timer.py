import time

def countdown():
    seconds = int(input("Seconds: "))
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

def stopwatch():
    input("Press Enter to start")
    start = time.time()
    input("Press Enter to stop")
    print("Elapsed:", round(time.time() - start, 2), "seconds")

def start_timer():
    while True:
        print("\nTIMER")
        print("1. Countdown")
        print("2. Stopwatch")
        print("3. Back")

        ch = input("Choice: ")
        if ch == "1": countdown()
        elif ch == "2": stopwatch()
        elif ch == "3": break