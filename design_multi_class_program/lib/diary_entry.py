class DiaryEntry:

    def __init__(self, title, contents, contacts):
        if type(title) != str or type(contents) != str:
            raise Exception("Only strings are allowed for title and contents!")
        if type(contacts) != dict and contacts != None:
            raise Exception("Only dictionary or None allowed for contacts!")
        self.title = title
        self.contents = contents
        self.contacts = contacts

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        word_count = self.format().split()
        return len(word_count)