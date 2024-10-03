from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        if not isinstance(entry, DiaryEntry):
            raise Exception("Only class instances are allowed!")
        self.diary_entries.append(entry)

    def all(self):
        return [{entry.title: entry.contents} for entry in self.diary_entries]

    def count_words(self):
        counter = 0
        for entry in self.diary_entries:
            counter += entry.count_words()
        return counter

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise Exception("Only integers are allowed!")
        
        num_of_words = self.count_words()
        minutes = round(num_of_words/wpm)
        if minutes <1:
            return "Less than a minute"
        elif minutes == 1:
            return "1 minute"
        else:
            return f"{minutes} minutes"

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int:
            raise Exception("Only integers are allowed!")
        for entry in self.diary_entries:
            if entry.count_words()/wpm == minutes:
                return entry.contents
            


