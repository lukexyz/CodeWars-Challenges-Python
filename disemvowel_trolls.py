from test import Test
'''
Description:

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
'''


# First attempt
def disemvowel(string):
    return ''.join([letter for letter in string if letter.lower() not in 'aeiou'])


# Refining soltion
def disemvowel2(s):
    return s.translate("aeiouAEIOU")


test = Test()
test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!",)
test.report()
