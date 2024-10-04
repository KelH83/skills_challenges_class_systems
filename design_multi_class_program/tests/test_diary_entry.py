from lib.diary_entry import *
import pytest

day_3 = DiaryEntry("Thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})

def test_creates_an_instance_of_DiaryEntry():
    assert isinstance(day_3, DiaryEntry)
    assert day_3.title ==  "Thur 4th Oct"
    assert day_3.contents == "Met with old friend again, need to update her number"
    assert day_3.contacts ==  {'Kimiko':'012345678'}

def test_creat_instance_throws_error_for_incorrect_datatypes():
    with pytest.raises(Exception) as e:
        day1_error = DiaryEntry(123, 'hello', {'Kimiko':'012345678'})
    error_message = str(e.value)
    assert error_message == "Only strings are allowed for title and contents!"
    with pytest.raises(Exception) as e:
        day1_error = DiaryEntry('Day', 123, {'Kimiko':'012345678'})
    error_message = str(e.value)
    assert error_message == "Only strings are allowed for title and contents!"
    with pytest.raises(Exception) as e:
        day1_error = DiaryEntry('day1', 'hello', 123)
    error_message = str(e.value)
    assert error_message == "Only dictionary or None allowed for contacts!"

def test_format_returns_formatted_version_of_diary_entry():
    assert day_3.format() ==  "Thur 4th Oct: Met with old friend again, need to update her number"

def test_contacts_returns_the_dictionary_of_contacts():
    day_4 = DiaryEntry("Fri 5th Oct", "Met with Kiyomi and Kyoko, took down their numbers", {'Kyomi':'109876543', 'Kyoko':'55512345'})

    assert day_4.contacts ==  {'Kyomi':'109876543', 'Kyoko':'55512345'}

def test_count_words_returns_the_right_number():
    day_4 = DiaryEntry("Fri 5th Oct", "Met with Kiyomi and Kyoko, took down their numbers", {'Kyomi':'109876543', 'Kyoko':'55512345'})
    assert day_4.count_words() == 12