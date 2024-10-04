from lib.todo_list import *
from lib.todo import *
import pytest

todo_list = TodoList()
walk_dogs = Todo("walk dogs")
feed_cats = Todo("feed cats")
stand_up = Todo("Makers standup")
code = Todo("Continue coding")


def test_add_puts_instance_of_todo_into_list():
    todo_list.add(walk_dogs)
    assert len(todo_list.todos) == 1
    assert todo_list.todos[0].task == "walk dogs"
    assert todo_list.todos[0].complete == False
    todo_list.add(feed_cats)
    assert len(todo_list.todos) == 2
    assert todo_list.todos[1].task == "feed cats"
    assert todo_list.todos[1].complete == False

def test_add_throws_error_with_incorrect_datatype():
    with pytest.raises(Exception) as e:
        todo_list.add("Cook lunch")
    error_message = str(e.value)
    assert error_message == "Only instances of Todo allowed!"

def test_incomplete_returns_a_list_of_incomplete_todos():
    assert todo_list.incomplete() == ["walk dogs","feed cats"]

def test_complete_returns_a_list_of_complete_todos():
    walk_dogs.mark_complete()
    assert todo_list.complete() == ["walk dogs"]
    assert todo_list.incomplete() == ["feed cats"]

def test_give_up_marks_all_items_as_complete():
    todo_list.add(stand_up)
    todo_list.add(code)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == ["walk dogs", "feed cats", "Makers standup", "Continue coding"]