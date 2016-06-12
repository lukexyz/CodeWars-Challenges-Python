from test import Test
import collections

'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic
characters that occur more than once in the given string. The given string can be
assumed to contain only uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
'''


# first attempt
def duplicate_count2(text):
    k = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            k += 1
    return k


# refined
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


test = Test()
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)
test.assert_equals(duplicate_count("Indivisibilities"), 2)
test.assert_equals(duplicate_count("Doggydog"), 3)
test.report()
