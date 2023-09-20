"""
Return the Objects Keys and Values by Timothy Eden
Date Last Modified: July 2, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/9HWMgvjF7p3zhWBdk
"""


def keys_and_values(d):
    keys = []
    values = []
    result = []
    for k in d:
        keys.append(k)
    keys.sort()
    for i in keys:
        values.append(d[i])
    result.append(keys)
    result.append(values)
    return result


def main():
    assert keys_and_values({"a": 1, "b": 2, "c": 3}) == \
           [["a", "b", "c"], [1, 2, 3]]
    assert keys_and_values({"a": "Apple", "b": "Microsoft", "c": "Google"}) == \
           [["a", "b", "c"], ["Apple", "Microsoft", "Google"]]
    assert keys_and_values({"key1": True, "key2": False, "key3": True}) == \
           [["key1", "key2", "key3"], [True, False, True]]


if __name__ == '__main__':
    main()
