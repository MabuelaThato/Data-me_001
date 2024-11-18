# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    new_list = lst[::-1]
    return new_list  

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count = lst.count(element)
    return count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    keys = []

    for key,value2 in dct.items():
        if value == value2:
            keys.append(key)

    return keys

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    new_list = lst1 + lst2

    return sorted(new_list)

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    largest = numbers[0]
    second = 0
    for i in range(1,len(numbers)):
        if largest < numbers[i]:
            largest = numbers[i]
        
    if len(numbers) > 0:
        for _ in range(numbers.count(largest)):
            numbers.remove(largest)

    for num in numbers:
        if second < num:
            second = num

    if second == 0:
        return None
    else:
        return second

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1.count(str1[i]) == str2.count(str1[i]):
                pass
            else:
                return False
    else:
        return False

    return True

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    new = []
    for item in nested_list:
        new += item
    return new
flatten_list([[1, 2], [3, 4]]) 

def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    ls = set(lst)
    return list(ls)

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common = []

    for item in lst1:
        if item in lst2:
            common.append(item)
    return common
