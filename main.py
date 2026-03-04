import calculator
import notes_manager
import timer
import file_organizer
import unit_converter
import backup
import sys

def show_main_menu():
    print("\n" + "="*40)
    print("   PERSONAL PRODUCTIVITY SUITE")
    print("="*40)
    print("1. Calculator Tool")
    print("2. Notes Manager")
    print("3. Timer & Stopwatch")
    print("4. File Organizer")
    print("5. Unit Converter")
    print("6. Backup & Restore")
    print("7. Exit")

def main():
    while True:
        show_main_menu()
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            calculator.start_calculator()

        elif choice == "2":
            notes_manager.start_notes_manager()

        elif choice == "3":
            timer.start_timer()

        elif choice == "4":
            file_organizer.start_file_organizer()

        elif choice == "5":
            unit_converter.start_converter()

        elif choice == "6":
            print("\n1. Create Backup")
            print("2. Restore Backup")
            b = input("Choice: ")
            if b == "1":
                backup.create_backup()
            elif b == "2":
                backup.restore_backup()

        elif choice == "7":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n⚠️ Unexpected error occurred:", e)
        print("Please restart the application.")