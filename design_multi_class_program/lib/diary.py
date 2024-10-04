class Diary:
    def __init__(self):
        self.diary_entries = []
        self.tasks = []
        self.contacts = []

    def add_to_diary(self, entry):
        self.diary_entries.append(entry)
        self.contacts.append(entry.contacts)

    def add_todo(self, todo):
        if type(todo) != str:
            raise Exception("Only strings allowed for todo tasks!")
        self.tasks.append(todo)

    def read_whole_diary(self):
        formatted_list = []
        for entry in self.diary_entries:
            formatted_list.append(entry.format())
        return formatted_list

    def read_entries_with_timeframe(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int:
            raise Exception("Only integers allowed for words per minute or minutes available!")
        for entry in self.diary_entries:
            if entry.count_words()/wpm == minutes:
                return entry.format()

    def read_todos(self):
        return self.tasks

    def read_contacts(self):
        return self.contacts