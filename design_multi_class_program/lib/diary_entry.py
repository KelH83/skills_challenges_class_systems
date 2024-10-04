class DiaryEntry:

    def __init__(self, title, contents, contacts):
        self.title = title
        self.contents = contents
        self.contacts = contacts

    def format(self):
        return f"{self.title}: {self.contents}"

    def contacts_info(self):
        return self.contacts