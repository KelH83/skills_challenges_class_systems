from lib.todo import *
import pytest

walk_dogs = Todo("Walk the dogs")

def test_creates_instance_of_todo():
    assert isinstance(walk_dogs, Todo)
    assert walk_dogs.task == "Walk the dogs"
    assert walk_dogs.complete == False

def test_instance_throws_error_with_incorrect_datatype():
    with pytest.raises(Exception) as e:
        walk_dogs = Todo(123)
    error_message = str(e.value)
    assert error_message == "Only strings allowed!"

def test_mark_complete_changes_to_true():
    walk_dogs.mark_complete()
    assert walk_dogs.complete == True
