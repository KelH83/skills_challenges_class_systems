class Diary:
    def __init__(self):
        self.diary_entries = []
        self.tasks = []
        self.contacts = []

    def add_to_diary(self, entry):
        # Parameters:
        #   entry : an instance of a diary entry
        # Side-effects:
        #   Adds the instance to the diary entries list
        pass # No code here yet

    def add_todo(self, todo):
        self.tasks.append(todo)


    def read_whole_diary(self):
        # Parameters:
        #   none
        # Returns:
        #   A list of all of the diary entries
        pass # No code here yet

    def read_entries_with_timeframe(self, wpm, minutes):
        # Parameters:
        #   wpm: the words per minute the user can read
        #   minutes: the number of minutes the user has to read
        # Returns:
        #   A randomly selected diary entry that meets the criteria
        pass # No code here yet

    def read_todos(self):
        return self.tasks

    def read_contacts(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all of the contacts
        pass # No code here yet