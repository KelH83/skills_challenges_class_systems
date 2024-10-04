from lib.diary import *
from lib.diary_entry import *
import pytest

new_diary = Diary()
new_diary2 = Diary()
new_diary3 = Diary()

def test_add_to_diary_updates_entries_list():
    day_1 = DiaryEntry("Tues 2nd Oct", "Did some coding", None)
    day_2 = DiaryEntry("Wed 3rd Oct", "Met with an old friend", None)
    new_diary.add_to_diary(day_1)
    new_diary.add_to_diary(day_2)
    assert new_diary.read_whole_diary() ==["Tues 2nd Oct: Did some coding", "Wed 3rd Oct: Met with an old friend"]

def test_read_contacts_returns_a_list_of_all_contacts():
    day_3 = DiaryEntry("thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})
    day_4 = DiaryEntry("Fri 5th Oct", "Need to update Yomi's number", {'Kiyomi':'555645678'})
    new_diary2.add_to_diary(day_3)
    new_diary2.add_to_diary(day_4)
    assert new_diary2.read_contacts() == [{'Kimiko':'012345678'},{'Kiyomi':'555645678'}]

def test_read_entries_with_timeframe_returns_appropriate_entry():
    day1 = DiaryEntry('Day 1', '50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis', None)
    day2 = DiaryEntry('Day 2', '200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla', None)
    new_diary3.add_to_diary(day1)
    new_diary3.add_to_diary(day2)
    assert new_diary3.read_entries_with_timeframe(50, 1) == 'Day 1: 50 words. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vehicula, justo at tristique consectetur, velit nunc efficitur leo, eget tristique orci lacus quis elit. Vivamus eget arcu lorem. Vivamus finibus velit bibendum neque bibendum dignissim. Integer convallis erat nibh, ut cursus quam posuere id. Etiam quis'
    assert new_diary3.read_entries_with_timeframe(200, 1) == 'Day 2: 200 words in total.A Duis vestibulum leo in dui gravida, quis facilisis nunc consectetur. Vivamus dapibus lacinia enim ut rhoncus. Pellentesque et odio diam. Vivamus a turpis eu diam facilisis pulvinar non eget libero. Pellentesque pretium commodo orci eu efficitur. Sed feugiat dolor arcu, a scelerisque nulla molestie et. Proin et tortor ut sapien sodales bibendum quis et tortor. Phasellus vitae ornare dolor, eu tincidunt ex. In hac habitasse platea dictumst. Donec elementum ligula non orci condimentum, a mattis felis aliquam.Phasellus lectus dolor, sagittis vitae egestas non, venenatis quis dolor. Nunc quis augue sapien. Ut laoreet leo nisi. Nunc aliquam fringilla aliquet. Duis laoreet nec dolor ac condimentum. Nullam tincidunt tristique sapien eget laoreet. Nam euismod blandit libero, id commodo felis facilisis et.Suspendisse scelerisque consequat nisi, a commodo risus dignissim non. Morbi malesuada tellus ut sapien iaculis, eu pellentesque justo interdum. Donec quis nunc erat. Nunc porta sodales sem, varius sodales ex vulputate vitae. Donec et fringilla tortor. Morbi rhoncus massa non mollis volutpat. Duis lobortis libero sed erat bibendum euismod. Ut a arcu gravida, tincidunt nisi sit amet, sodales arcu. Fusce lobortis varius nibh, vel luctus massa ultricies ac. Aenean convallis dui vitae erat maximus suscipit. Nulla'

def test_red_entries_with_timeframe_throws_error_for_incorrect_datatype():
    with pytest.raises(Exception) as e:
        new_diary3.read_entries_with_timeframe(50, 'hello')
    error_message = str(e.value)
    assert error_message == "Only integers allowed for words per minute or minutes available!"
