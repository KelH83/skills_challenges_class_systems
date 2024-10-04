from lib.diary_entry import *

day_3 = DiaryEntry("Thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})

def test_creates_an_instance_of_DiaryEntry():
    assert isinstance(day_3, DiaryEntry)
    assert day_3.title ==  "Thur 4th Oct"
    assert day_3.contents == "Met with old friend again, need to update her number"
    assert day_3.contacts ==  {'Kimiko':'012345678'}

def test_format_returns_formatted_version_of_diary_entry():
    assert day_3.format() ==  "Thur 4th Oct: Met with old friend again, need to update her number"

def test_contacts_returns_the_dictionary_of_contacts():
    day_4 = DiaryEntry("Fri 5th Oct", "Met with Kiyomi and Kyoko, took down their numbers", {'Kyomi':'109876543', 'Kyoko':'55512345'})

    assert day_4.contacts ==  {'Kyomi':'109876543', 'Kyoko':'55512345'}