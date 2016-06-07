"""
You are given an array strarr of strings and an integer k. Your task is to return
the first longest string consisting of k consecutive strings taken in the array.

Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


# First attempt
def longest_consec2(strarr, k):
    if k < 1 or k > len(strarr):
        return ''
    long = ''
    for i in range(len(strarr)):
        if len(''.join(strarr[i:i+k])) > len(long):
            long = ''.join(strarr[i:i+k])
    return long


# Improved
def longest_consec(strarr, k):
    if len(strarr) == 0 or k < 1 or k > len(strarr):
        return ''
    consecutive = [''.join(strarr[i:i + k]) for i in range(len(strarr))]
    return max(consecutive, key=lambda x: len(x))



print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
