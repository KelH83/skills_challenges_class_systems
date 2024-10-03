from lib.diary import *
from lib.diary_entry import *
import pytest


diary_entry1 = DiaryEntry('Day 1', 'Command line')
diary_entry2 = DiaryEntry('Day 2', 'Python functions')
diary_entry3 = DiaryEntry('Day 3', 'Python classes')
diary_entry4 = DiaryEntry('Day 4', '200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla at ante')
diary_entry5 = DiaryEntry('Day 5', '50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis arcu risus.')
diary_entry6 = DiaryEntry('Day 6', '250 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla at ante.50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis arcu risus.')


new_diary = Diary()
new_diary2 = Diary()
new_diary3 = Diary()


def test_instance_is_created():
    assert isinstance(new_diary, Diary)
    assert new_diary.diary_entries == []

def test_add_makes_a_new_entry_in_diary():
    new_diary.add(diary_entry1)
    assert len(new_diary.diary_entries) == 1

def test_add_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary.add('hello')
    error_message = str(e.value)
    assert error_message == "Only class instances are allowed!"

def test_add_makes_multiple_entries_in_diary():
    new_diary2.add(diary_entry1)
    new_diary2.add(diary_entry2)
    new_diary2.add(diary_entry3)
    assert len(new_diary2.diary_entries) == 3

def test_all_returns_a_list_of_all_entries():
    diary_list =  new_diary.all() 
    assert diary_list == [{diary_entry1.title:diary_entry1.contents}]
    diary_list2 =  new_diary2.all() 
    assert diary_list2 == [{diary_entry1.title:diary_entry1.contents},{diary_entry2.title:diary_entry2.contents},{diary_entry3.title:diary_entry3.contents}]

def test_count_words_returns_an_integer_of_total_words_in_diary():
    assert new_diary2.count_words() == 6

def test_reading_time_returns_number_of_minutes_needed_to_read_entire_diary():
    assert new_diary2.reading_time(50) == "Less than a minute"
    new_diary2.add(diary_entry4)
    assert new_diary2.reading_time(50) == "4 minutes"

def test_reading_time_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary2.reading_time('hello')
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"

def test_find_best_entry_returns_appropriate_entry_for_time():
    new_diary3.add(diary_entry4)
    new_diary3.add(diary_entry5)
    new_diary3.add(diary_entry6)
    assert new_diary3.find_best_entry_for_reading_time(50,1) == diary_entry5.contents
    assert new_diary3.find_best_entry_for_reading_time(200,1) == diary_entry4.contents

def test_find_best_entry_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary3.find_best_entry_for_reading_time('hello',1)
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"