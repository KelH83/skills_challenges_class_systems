from lib.diary import *
import pytest

new_diary = Diary()

def test_instance_is_created():
    assert isinstance(new_diary, Diary)
    assert new_diary.diary_entries == []

def test_add_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary.add('hello')
    error_message = str(e.value)
    assert error_message == "Only class instances are allowed!"

def test_all_returns_an_empty_list():
    assert new_diary.all() == []

def test_count_words_returns_zero():
    assert new_diary.count_words() == 0

def test_reading_time_returns_correct_response_for_empty_entires():
    assert new_diary.reading_time(50) == "Diary is empty"

def test_find_best_returns_correct_response_for_empty_entires():
    assert new_diary.find_best_entry_for_reading_time(50,2) == "Diary is empty"