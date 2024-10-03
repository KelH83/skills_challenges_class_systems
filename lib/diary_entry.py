class DiaryEntry:
    def __init__(self, title, contents):
        if type(title) != str or type(contents) != str:
            raise Exception("Only strings are allowed!")
        self.title = title
        self.contents = contents

    def count_words(self):
        contents_list = self.contents.split()
        return len(contents_list)

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

    def reading_chunk(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int:
            raise Exception("Only integers are allowed!")
        text_list = self.contents.split()
        amount = wpm * minutes
        chunk_words = text_list[:amount]
        chunk = " ".join(chunk_words)
        self.contents = self.contents.replace(chunk, '')
        return chunk
