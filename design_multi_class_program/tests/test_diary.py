from lib.diary import *
import pytest

new_diary = Diary()

def test_creates_an_instance_of_Diary():
    assert isinstance(new_diary, Diary)
    assert new_diary.diary_entries == []
    assert new_diary.tasks == []
    assert new_diary.contacts == []

def test_add_todo_updates_todo_list():
    new_diary.add_todo("walk dogs")
    new_diary.add_todo("feed cats")
    assert new_diary.read_todos() == ["walk dogs", "feed cats"]

def test_add_todo_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary.add_todo(123)
    error_message = str(e.value)
    assert error_message == "Only strings allowed for todo tasks!"
