import csv
from itertools import product
from flask import Flask, render_template, request

app = Flask(__name__)

def filter_words_by_letter(input_letter, input_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        words_list = [row[0].lower() for row in csv_reader]

    filtered_words = [word for word in words_list if input_letter.lower() in word]

    return filtered_words

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def show_results():
    center_letter = request.form.get('center_letter')
    additional_letters = request.form.get('additional_letters').split(',')

    # Combine the center letter and additional letters into all_letters list
    all_letters = [center_letter] + [letter.strip().lower() for letter in additional_letters]

    # Load the CSV file containing valid words
    input_csv_file = "Michigan_Words.csv"  # Replace with the path to your input CSV file
    filtered_words = filter_words_by_letter(center_letter, input_csv_file)

    # Limit the maximum length of permutations
    max_length_permutation = len(max(filtered_words, key=len))
    
    # Limit the maximum length of permutations to the length of the longest word
    max_length_permutation = min(max_length_permutation, 9)  # You can adjust the limit as needed

    # Generate permutations of letters with repetitions and find the intersection with filtered words
    permutations_set = {permutation_word for length in range(4, max_length_permutation + 1)
                        for p in product(all_letters, repeat=length)
                        if (permutation_word := ''.join(p).lower()) in filtered_words}

        # Sort the permutations alphabetically
    sorted_permutations = sorted(permutations_set)
    
    return render_template('index.html', center_letter=center_letter, additional_letters=', '.join(additional_letters), results=permutations_set)

if __name__ == '__main__':
    app.run(debug=True)
