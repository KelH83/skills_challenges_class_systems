class LetterCounter:
    def __init__(self, text):
        self.text = text
        print

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            if not char.isalpha():
                continue
            if char not in counter.keys():
                counter[char] = counter.get(char, 1)
            else: 
                counter[char] += 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
