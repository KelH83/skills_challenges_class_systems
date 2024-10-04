from lib.todo import *

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        if isinstance(todo, Todo):
            self.todos.append(todo)
        else:
            raise Exception("Only instances of Todo allowed!")

    def incomplete(self):
        incomplete_todos = []
        for todo in self.todos:
            if todo.complete == False:
                incomplete_todos.append(todo.task)
        return incomplete_todos

    def complete(self):
        complete_todos = []
        for todo in self.todos:
            if todo.complete == True:
                complete_todos.append(todo.task)
        return complete_todos

    def give_up(self):
        for todo in self.todos:
                todo.mark_complete()
