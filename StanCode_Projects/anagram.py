"""
File: anagram.py
Name: Cindy Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_lst = {}                 # This stores all the words found in the dictionary text file
cur_lst = []                  # This stores all the anagrams
count = 0                     #


def main():
    """
    This program reads a word input by the user and finds all the anagram of that word,
    continuing the process until the EXIT constant is entered.
    """

    global count, cur_lst
    print('Welcome to stanCode \"Anagram Generator\" or ' + str(EXIT) + ' to quit')

    # Continue program while -1 is not entered
    while True:
        s = str(input('Find anagrams for: '))
        start = time.time()
        if s == EXIT:
            break
        else:
            # count = 0
            # cur_lst = []
            find_anagrams(s)
            print(str(count) + ' anagrams: ' + str(cur_lst))
            count = 0
            # cur_lst = []

    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    # Create empty dictionary list
    global dict_lst
    # Open text file
    with open(FILE, 'r') as f:
        # read file line by line
        for line in f:
            value = line.strip()
            if value[0] in s:
                # 字典長度跟開頭有才加
                if len(value) == len(s):
                    # if value[0] in dict_lst:
                    # Append word to list
                    dict_lst[value[0]].append(value)
                else:
                    dict_lst[value[0]] = [value]


def find_anagrams(s):
    """
    :param s: string input entered by user
    :return:
    """
    print('Searching...')
    read_dictionary(s)
    find_anagrams_helper(s, '', '')


# create helper where s= input, current_str = current string, lst= list used to store found anagram,
# dict_lst= list containing words from dictionary file, len(s)= length of user input
def find_anagrams_helper(s, current_str, index):
    global count, cur_lst
    # Base Case
    if len(current_str) == len(s):
        if current_str not in cur_lst:
            if has_prefix(current_str):
                if current_str in dict_lst:
                    cur_lst.append(current_str)
                    count += 1
                    print('Found: ' + str(current_str))
    else:
        for i in range(len(s)):
            if str(i) not in index:
                # Choose
                index += str(i)
                # print(index)
                current_str += s[i]
                if has_prefix(current_str[0:3]):
                    # Explore
                    find_anagrams_helper(s, current_str, index)
                # Un-choose
                current_str = current_str[:-1]
                index = index[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
