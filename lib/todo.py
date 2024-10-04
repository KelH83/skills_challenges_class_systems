class Todo:
    def __init__(self, task):
        if type(task) != str:
            raise Exception("Only strings allowed!")
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True
