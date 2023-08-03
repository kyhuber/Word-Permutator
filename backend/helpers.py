import os
import csv
from itertools import product

def filter_words_by_letter(input_letter, input_file):
    # Construct the CSV file path within the backend directory
    csv_file_path = os.path.join(os.path.dirname(__file__), input_file)

    # Read words from the CSV file and filter them based on input_letter
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        words_list = {row[0].lower() for row in csv_reader}

    filtered_words = {word for word in words_list if input_letter.lower() in word}

    return filtered_words

def generate_sorted_permutations(center_letter, additional_letters, input_file):
    all_letters = [center_letter] + additional_letters
    filtered_words = filter_words_by_letter(center_letter, input_file)

    # Limit the maximum length of permutations
    max_length_permutation = 8

    # Generate permutations of letters with repetitions and find the intersection with filtered words
    permutations_set = {permutation_word for length in range(4, max_length_permutation + 1)
                        for p in product(all_letters, repeat=length)
                        if (permutation_word := ''.join(p).lower()) in filtered_words}

    # Convert the set of permutations to a sorted list
    sorted_permutations = sorted(permutations_set)

    return sorted_permutations
