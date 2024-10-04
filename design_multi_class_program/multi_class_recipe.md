## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

```
┌────────────────────────────┐
│ Diary                      │
│                            │
│ - add entries              │
│ - read entries             │
│ - read entries in a given  │
│   timeframe                │
│ - add todo to list         │
│ - read todo list           │
│ - add contacts to list     │
│ - read contact list        │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Diary entries           │
│                         │
│ - title                 │
│ - contents              │
└─────────────────────────┘

┌─────────────────────────┐
│ Task entries            │
│                         │
│ - task                  │
└─────────────────────────┘

┌─────────────────────────┐
│ Contact entries         │
│                         │
│ - names                 │
│ - phone numbers         │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary_entries: list of diary entries
    #   tasks: list of todo tasks
    #   contacts: list of contacts

    def __init__(self):
        pass # No code here yet

    def add_to_diary(self, entry):
        # Parameters:
        #   entry : an instance of a diary entry
        # Side-effects:
        #   Adds the instance to the diary entries list
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   todo : an instance of a todo task
        # Side-effects:
        #   Adds the instance to the todo list
        pass # No code here yet


    def read_whole_diary(self):
        # Parameters:
        #   none
        # Returns:
        #   A list of all of the diary entries
        pass # No code here yet

     def read_entries_with_timeframe(self, wpm, minutes):
        # Parameters:
        #   wpm: the words per minute the user can read
        #   minutes: the number of minutes the user has to read
        # Returns:
        #   A randomly selected diary entry that meets the criteria
        pass # No code here yet

    def read_todos(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all of the todos
        pass # No code here yet

    def read_contacts(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all of the contacts
        pass # No code here yet


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string
    #   contacts: dictionary

    def __init__(self, title, contents, contacts):
        # Parameters:
        #   title: string
        #   contents: string
        #   contacts: dictionary or null
        # Side-effects:
        #   Sets the title,content and contacts, properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the entry "TITLE: CONTENTS"
        pass # No code here yet

    def contacts(self):
        # Returns:
        #   The contacts dictionary
        pass # No code here yet




```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a Diary
When we add two entries
We see those entries reflected in the entries list
"""
new_diary = Diary()
day_1 = DiaryEntry("Tues 2nd Oct", "Did some coding", Null)
day_2 = DiaryEntry("Wed 3rd Oct", "Met with an old friend", Null)
new_diary.add_to_diary(day_1)
new_diary.add_to_diary(day_2)
new_diary.read_whole_diary() # => ["Tues 2nd Oct: Did some coding", "Wed 3rd Oct":Met with an old friend"]


"""
Given a Diary
When we add a diary entry with a contact number
We see that contact reflected in the contacts list
"""
new_diary = Diary()
day_3 = DiaryEntry("thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})
new_diary.add_to_diary(day_3)
new_diary.read_contacts() # => [{'Kimiko':'012345678'}]

"""
Given a Diary
When we call read entries with timeframe
We see a randomly selected entry that fits within the timeframe
"""
new_diary = Diary()
day_1 = DiaryEntry("Tues 2nd Oct", "Did some coding", Null)
day_2 = DiaryEntry("Wed 3rd Oct", "Met with an old friend", Null)
new_diary.add_to_diary(day_1)
new_diary.add_to_diary(day_2)
new_diary.read_entries_with_timeframe(50, 1) # => Randomly selected - ["Wed 3rd Oct":Met with an old friend"]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

"""
Given a Diary
When we create the instance
We see that empty lists have been created
"""
new_diary = Diary()
new_diary.diary_entries # => []
new_diary.tasks # => []
new_diary.contacts # => []


"""
Given a Diary
When we add tasks
We see those tasks reflected in the task list
"""
new_diary = Diary()
new_diary.add_todo("walk dogs")
new_diary.add_todo("feed cats")
new_diary.read_todos() # => ["walk dogs", "feed cats"]


"""
Given a DiaryEntry
When we create the instance
We see that the properties have been updated with thr given information
"""
day_3 = DiaryEntry("Thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})

day_3.title # =>  "Thur 4th Oct"
day_3.title # =>  "Met with old friend again, need to update her number"
day_3.title # =>  {'Kimiko':'012345678'}

"""
Given a DiaryEntry
When we call format
We see a formatted version of the title and contents of that entry
"""
day_3 = DiaryEntry("Thur 4th Oct", "Met with old friend again, need to update her number", {'Kimiko':'012345678'})

day_3.format() # =>  "Thur 4th Oct: Met with old friend again, need to update her number"

"""
Given a DiaryEntry
When we call contacts
We get a dictionary with contacts from that day
"""
day_4 = DiaryEntry("Fri 5th Oct", "Met with Kiyomi and Kyoko, took down their numbers", {'Kyomi':'109876543', 'Kyoko':'55512345'})

day_4.contacts # =>  {'Kyomi':'109876543', 'Kyoko':'55512345'}


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
