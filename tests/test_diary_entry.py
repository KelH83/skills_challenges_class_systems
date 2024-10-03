from lib.diary_entry import *
import pytest

diary_entry1 = DiaryEntry('Day 1', 'Command line')
diary_entry2 = DiaryEntry('Day 2', 'Python functions and lots of testing')
diary_entry3 = DiaryEntry('Day 3', '50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis arcu risus.')
diary_entry4 = DiaryEntry('Day 4', '200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla at ante')
diary_entry5 = DiaryEntry('Day 5', '200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla at ante')

def test_creates_an_instance():
    assert isinstance(diary_entry1, DiaryEntry)
    assert diary_entry1.title == "Day 1"
    assert diary_entry1.contents == "Command line"

def test_throws_error_when_given_incorrect_datatype():
    with pytest.raises(Exception) as e:
        diary_entry_error = DiaryEntry(123, 'hello')
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"

def test_counts_the_number_of_words_in_an_entry():
    assert diary_entry1.count_words() == 2
    assert diary_entry2.count_words() == 6
    assert diary_entry3.count_words() == 50
    assert diary_entry4.count_words() == 200

def test_the_number_of_minutes_needed_to_read_the_contents():
    assert diary_entry1.reading_time(50) == "Less than a minute"
    assert diary_entry2.reading_time(50) == "Less than a minute"
    assert diary_entry3.reading_time(50) == "1 minute"
    assert diary_entry4.reading_time(50) == "4 minutes"

def test_reading_time_throws_error_when_incorrect_datatypes_given():
    with pytest.raises(Exception) as e:
        diary_entry1.reading_time('hello')
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"

def test_that_reading_chunk_returns_a_chunk_of_text():
    assert diary_entry1.reading_chunk(50, 1) == "Command line"
    assert diary_entry3.reading_chunk(50, 1) == "50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis arcu risus."
    assert diary_entry4.reading_chunk(50, 1) == "200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin"

def test_that_reading_chunk_returns_the_next_chunk_of_text():
    diary_entry5.reading_chunk(50, 1)
    assert diary_entry5.reading_chunk(50, 1) == "et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam"

def tests_reading_chunk_throws_error_if_given_incorrect_datatypes():
    with pytest.raises(Exception) as e:
        diary_entry1.reading_chunk('hello', 3)
    error_message = str(e.value)
    assert error_message == "Only integers are allowed!"
