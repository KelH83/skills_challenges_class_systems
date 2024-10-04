# from lib.diary import *
# from lib.diary_entry import *

# new_diary = Diary()

# def test_add_to_diary_updates_entries_list():
#     day_1 = DiaryEntry("Tues 2nd Oct", "Did some coding", None)
#     day_2 = DiaryEntry("Wed 3rd Oct", "Met with an old friend", None)
#     new_diary.add_to_diary(day_1)
#     new_diary.add_to_diary(day_2)
#     assert new_diary.read_whole_diary() ==["Tues 2nd Oct: Did some coding", "Wed 3rd Oct:Met with an old friend"]

# def test_read_contacts_returns_a_list_of_all_contacts():
#     day_3 = DiaryEntry("thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})
#     new_diary.add_to_diary(day_3)
#     assert new_diary.read_contacts() == [{'Kimiko':'012345678'}]

# def test_read_entries_with_timeframe_returns_appropriate_entry():
    # assert new_diary.read_entries_with_timeframe(50, 1) == #Check how to assert for multiple options