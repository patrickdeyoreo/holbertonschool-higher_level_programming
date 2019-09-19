#!/usr/bin/env python3
# coding: utf-8

# In[269]:


from task import Task


# In[270]:


tasks = {}


# ## 0. Squared simple
#
# Write a function that computes the square value of all integers of a matrix.
#
# `square_matrix_simple(matrix=[])`
#
# * matrix is a 2 dimensional array
# * Returns a new matrix:
# * Same size as matrix
# * Each value should be the square of the value of the input
# * Initial matrix should not be modified
# * You are not allowed to import any module
# * You are allowed to use regular loops, map, etc.

# In[271]:


def square_matrix_simple(matrix=[]):
    """ Compute a new matrix with each element squared
    """
    if matrix is not None:
        return list(map(
            lambda row: list(map(
                lambda x: x ** 2, row
            )),
            matrix
        ))
    return None


# In[272]:


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)


# In[273]:


tasks[0] = Task(square_matrix_simple, main=main)


# In[274]:


tasks[0]()


# ## 1. Search and replace
#
# Write a function that replaces all occurrences of an element by another in a new list.
#
# `search_replace(my_list, search, replace)`
#
# * my_list is the initial list
# * search is the element to replace in the list
# * replace is the new element
# * You are not allowed to import any module

# In[275]:


def search_replace(my_list, search, replace):
    """ Create a new list with all occurrences of an element replaced
    """
    if my_list is not None:
        return [x if x != search else replace for x in my_list]
    return None


# In[276]:


def main():
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)


# In[277]:


tasks[1] = Task(search_replace, main=main)


# In[278]:


tasks[1]()


# ## 2. Unique addition
#
# Write a function that adds all unique integers in a list (only once for each integer).
#
# `uniq_add(my_list=[])`
#
# * You are not allowed to import any module

# In[279]:


def uniq_add(my_list=[]):
    """ Sum all unique integers in a list
    """
    if my_list is not None:
        return sum(set(my_list))
    return None


# In[280]:


def main():
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


# In[281]:


tasks[2] = Task(uniq_add, main=main)


# In[282]:


tasks[2]()


# ## 3. Present in both
#
# Write a function that returns a set of common elements in two sets.
#
# `common_elements(set_1, set_2)`
#
# * You are not allowed to import any module

# In[283]:


def common_elements(set_1, set_2):
    """ Print the elements common to two sets (i.e. union)
    """
    if set_1 is not None and set_2 is not None:
        return set(set_1) & set(set_2)
    return None


# In[284]:


def main():
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))


# In[285]:


tasks[3] = Task(common_elements, main=main)


# In[286]:


tasks[3]()


# ## 4. Only differents
#
# Write a function that returns a set of all elements present in only one set.
#
# `only_diff_elements(set_1, set_2)`
#
# * You are not allowed to import any module

# In[287]:


def only_diff_elements(set_1, set_2):
    """ Print the elements unique to each set (i.e. disjoint union)
    """
    if set_1 is not None and set_2 is not None:
        return set(set_1) ^ set(set_2)
    return None


# In[288]:


def main():
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))


# In[289]:


tasks[4] = Task(only_diff_elements, main=main)


# In[290]:


tasks[4]()


# ## 5. Number of keys
#
# Write a function that returns the number of keys in a dictionary.
#
# `number_keys(a_dictionary)`
#
# * You are not allowed to import any module

# In[291]:


def number_keys(a_dictionary):
    """ Compute the number of keys in a dictionary
    """
    if a_dictionary is not None:
        return len(a_dictionary)
    return None


# In[292]:


def main():
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))


# In[293]:


tasks[5] = Task(number_keys, main=main)


# In[294]:


tasks[5]()


# ## 6. Print sorted dictionary
#
# Write a function that prints a dictionary by ordered keys.
#
# `print_sorted_dictionary(a_dictionary)`
#
# * You can assume that all keys are strings
# * Keys should be sorted by alphabetic order
# * Only sort keys of the first level (don’t sort keys of a dictionary inside the main * dictionary)
# * Dictionary values can have any type
# * You are not allowed to import any module

# In[295]:


def print_sorted_dictionary(a_dictionary):
    """ Print the entries in a dictionary sorted by key
    """
    if a_dictionary is not None:
        for pair in sorted(a_dictionary.items(), key=lambda key,*_: key):
            print('{}: {}'.format(*pair))


# In[296]:


def main():
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)


# In[297]:


tasks[6] = Task(print_sorted_dictionary, main=main)


# In[298]:


tasks[6]()


# ## 7. Update dictionary
#
# Write a function that replaces or adds key/value in a dictionary.
#
# `update_dictionary(a_dictionary, key, value)`
#
# * key argument will be always a string
# * value argument will be any type
# * If a key exists in the dictionary, the value will be replaced
# * If a key doesn’t exist in the dictionary, it will be created
# * You are not allowed to import any module

# In[299]:


def update_dictionary(a_dictionary, key, value):
    """ Add or update a value a dictionary entry
    """
    if a_dictionary is not None:
        a_dictionary[key] = value
    return a_dictionary


# In[300]:


def main():
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)


# In[301]:


tasks[7] = Task(update_dictionary, main=main)


# In[302]:


tasks[7]()


# ## 8. Simple delete by key
#
# Write a function that deletes a key in a dictionary.
#
# `simple_delete(a_dictionary, key="")`
#
# * key argument will be always a string
# * If a key doesn’t exist, the dictionary won’t change
# * You are not allowed to import any module

# In[303]:


def simple_delete(a_dictionary, key=""):
    """ Delete a dictionary entry
    """
    if a_dictionary is not None:
        try:
            del a_dictionary[key]
        except KeyError:
            pass
        return a_dictionary
    return None


# In[304]:


def main():
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)


# In[305]:


tasks[8] = Task(simple_delete, main=main)


# In[306]:


tasks[8]()


# ## 9. Multiply by 2
#
# Write a function that returns a new dictionary with all values multiplied by 2.
#
# `multiply_by_2(a_dictionary)`
#
# * You can assume that all values are only integers
# * Returns a new dictionary
# * You are not allowed to import any module

# In[313]:


def multiply_by_2(a_dictionary):
    """ Create a new dictionary with all values doubled
    """
    if a_dictionary is not None:
        return {key: 2 * val for key, val in a_dictionary.items()}
    return None


# In[314]:


def main():
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)


# In[315]:


tasks[9] = Task(multiply_by_2, main=main)


# In[316]:


tasks[9]()


# ## 10. Best score
#
# Write a function that returns a key with the biggest integer value.
#
# `best_score(a_dictionary)`
#
# * You can assume that all values are only integers
# * If no score found, return None
# * You can assume all students have a different score
# * You are not allowed to import any module

# In[317]:


def best_score(a_dictionary):
    """ Retrieve the a key of the largest integer value
    """
    if a_dictionary:
        return max(a_dictionary.items(), key=lambda pair: pair[1], default=None)

    return None


# In[318]:


def main():
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))


# In[319]:


tasks[10] = Task(best_score, main=main)


# In[320]:


tasks[10]()


# ## 11. Multiply by using map
#
# Write a function that returns a list with all values multiplied by a number without using any loops.
#
# `mutiply_list_map(my_list=[], number=0)`
#
# * Returns a new list:
# * Same length as my_list
# * Each value should be multiplied by number
# * Initial list should not be modified
# * You are not allowed to import any module
# * You have to use map
# * Your file should be max 3 lines

# In[321]:


def mutiply_list_map(my_list=[], number=0):
    """ Create a list of the product each elements and the given number  """
    return None if list is None else list(map(lambda x: x * number, my_list))


# In[322]:


def main():
    my_list = [1, 2, 3, 4, 6]
    new_list = mutiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)


# In[323]:


tasks[11] = Task(mutiply_list_map, main=main)


# In[324]:


tasks[11]()

