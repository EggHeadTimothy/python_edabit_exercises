"""
Converting Dictionaries to Lists by Timothy Eden
Date Last Modified: July 2, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/PgsQAdNvsEAkese8X
"""


def to_list(dct):
    result = []
    if dct == {}:
        return result
    else:
        for k in dct:
            kvp = [k, dct[k]]
            result.append(kvp)
    result = sorted(result)
    return result


def main():
    assert to_list({"a": 1, "b": 2}) == [["a", 1], ["b", 2]]
    assert to_list({'foo': 33, 'bar': 45, 'baz': 67}) == [["bar", 45], ["baz", 67], ["foo", 33]]
    assert to_list({"shrimp": 15, "tots": 12}) == [["shrimp", 15], ["tots", 12]]
    assert to_list({}) == []


if __name__ == '__main__':
    main()
