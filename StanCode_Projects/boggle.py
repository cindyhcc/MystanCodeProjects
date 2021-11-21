"""
File: boggle.py
Name: 黃家祺
----------------------------------------
TODO:
"""

import time
import copy

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""

	"""
	# save user input boggle letters in a list
	start = time.time()
	boggle = []
	row_1 = (input('1 row of letters: '))
	if is_string_with_space(row_1):
		# append input into boggle
		boggle.append(row_1.split())
		row_2 = (input('2 row of letters: '))
		if is_string_with_space(row_2):
			# append input into boggle
			boggle.append(row_2.split())
			# append input into boggle
			row_3 = (input('3 row of letters: '))
			# check input format
			if is_string_with_space(row_3):
				boggle.append(row_3.split())
				row_4 = (input('4 row of letters: '))
				if is_string_with_space(row_4):
					boggle.append(row_4.split())
	set_permutations = get_permutations(boggle)
	read_dictionary(set_permutations)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_permutations(boggle):
	"""
	This functions loops over the boggle and get all letters of the boggle
	:param boggle:
	:return: list of permutations as a set
	"""
	set_permutations = set()
	counter = 0
	current_word = ""
	for x in range(4):
		for y in range(4):
			counter += 1
			words = word_search(boggle, x, y, found=[])
			if words:
				for word in words:
					set_permutations.add(word)
			words = None
	return sorted(list(set_permutations))


def is_string_with_space(check_input):
	"""
	This function checks if the string entered by user is alphabets with space included
	:param check_input: string input by user
	:return: bool
	"""
	check_input = check_input.lower()
	if ' ' in check_input:
		check_input.strip()
		for char in check_input:
			if char.isalpha() and len(check_input) <= 8:
				return True
			else:
				print('Illegal input')


def read_dictionary(set_permutations):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = {}
	# Open text file
	with open(FILE, 'r') as f:
		# read file line by line
		for line in f:
			# remove white spaces
			word = line.strip()
			dictionary[word] = 0
	counter = 0
	for word in set_permutations:
		if word.lower() in dictionary:
			counter += 1
			print('Found:' + str(word))
	print(f"There are {counter} words found")


def word_search(boggle, x, y, current_word="", found=[]):
	if x in (4, -1) or y in (4, -1):
		return
	if len(current_word) > 4:
		return

	if boggle[x][y] != "#":
		current_word = current_word + boggle[x][y]
		# make a copy of current boggle board
		new_boggle = copy.deepcopy(boggle)
		# make visited coordinates as "#"
		new_boggle[x][y] = "#"

		if len(current_word) >= 4:
			found.append(current_word.lower())

		neighbor = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for dx, dy in neighbor:
			word_search(new_boggle, x+dx, y+dy, current_word, found)
		return found


if __name__ == '__main__':
	main()
