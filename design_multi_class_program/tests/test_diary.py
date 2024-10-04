from lib.diary import *

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