class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = len(self.text) -1
        while i > -1:
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i -= 1
        return self.text
