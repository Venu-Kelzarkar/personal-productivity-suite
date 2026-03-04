import json
from datetime import datetime
import json
from datetime import datetime

DATA_FILE = "data/notes.json"

class NotesManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(DATA_FILE, "r") as f:
                self.notes = json.load(f)
        except:
            self.notes = []

    def save_notes(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, title, content):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(note)
        self.save_notes()
        print("✅ Note added!")

    def view_notes(self):
        if not self.notes:
            print("No notes found.")
            return

        for note in self.notes:
            print("\nID:", note["id"])
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("Created:", note["created"])

    def search_notes(self, keyword):
        found = [n for n in self.notes if keyword.lower() in n["title"].lower()]
        if not found:
            print("No notes found.")
            return
        for note in found:
            print(f"\nID:{note['id']} | Title:{note['title']}")

    def edit_note(self, note_id, new_content):
        for note in self.notes:
            if note["id"] == note_id:
                note["content"] = new_content
                note["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("✏️ Note updated!")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        self.notes = [n for n in self.notes if n["id"] != note_id]
        self.save_notes()
        print("🗑 Note deleted!")

    def export_txt(self):
        with open("data/notes.txt", "w", encoding="utf-8") as f:
            for note in self.notes:
                f.write(f"ID: {note['id']}\n")
                f.write(f"Title: {note['title']}\n")
                f.write(f"Content: {note['content']}\n")
                f.write("-"*20 + "\n")
        print("📄 Notes exported to notes.txt")

    def export_csv(self):
        import csv
        with open("data/notes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Title", "Content", "Created"])
            for note in self.notes:
                writer.writerow([note["id"], note["title"], note["content"], note["created"]])
        print("📊 Notes exported to notes.csv")


def start_notes_manager():
    manager = NotesManager()

    while True:
        print("\nNOTES MANAGER")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Back")

        choice = input("Choice: ")

        if choice == "1":
            manager.view_notes()
        elif choice == "2":
            manager.add_note(input("Title: "), input("Content: "))
        elif choice == "3":
            manager.search_notes(input("Keyword: "))
        elif choice == "4":
            manager.edit_note(int(input("ID: ")), input("New content: "))
        elif choice == "5":
            manager.delete_note(int(input("ID: ")))
        elif choice == "6":
            manager.export_txt()
        elif choice == "7":
            manager.export_csv()
        elif choice == "8":
            break