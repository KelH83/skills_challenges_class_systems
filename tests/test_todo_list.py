from lib.todo_list import *

todo_list = TodoList()

def test_creates_instance_of_todo_list():
    assert isinstance(todo_list, TodoList)
    assert todo_list.todos == []