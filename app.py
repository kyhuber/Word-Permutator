import csv
from itertools import product
from flask import Flask, render_template, request

app = Flask(__name__)

def filter_words_by_letter(input_letter, input_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        words_list = {row[0].lower() for row in csv_reader}

    filtered_words = {word for word in words_list if input_letter.lower() in word}

    return filtered_words

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        center_letter = request.form['center_letter'].strip().lower()
        additional_letters_input = request.form['additional_letters'].strip().lower()
        additional_letters = [letter.strip() for letter in additional_letters_input.split(",")]

        all_letters = [center_letter] + additional_letters

        input_csv_file = "https://github.com/kyhuber/Word-Permutator/blob/e6590ddf05c305db4d39b067c3d3745fd11ce049/backend/Most_words.csv"  # Replace with the path to your input CSV file

        filtered_words = filter_words_by_letter(center_letter, input_csv_file)

        # Limit the maximum length of permutations
        max_length_permutation = 12

        # Generate permutations of letters with repetitions and find the intersection with filtered words
        permutations_set = {permutation_word for length in range(4, max_length_permutation + 1)
                            for p in product(all_letters, repeat=length)
                            if (permutation_word := ''.join(p).lower()) in filtered_words}

        if permutations_set:
            # Sort the permutations alphabetically
            sorted_permutations = sorted(permutations_set)

            # Create a dictionary to group words by their starting letter
            grouped_lists = {}
            for word in sorted_permutations:
                starting_letter = word[0]
                if starting_letter not in grouped_lists:
                    grouped_lists[starting_letter] = []
                grouped_lists[starting_letter].append(word)

            # Render the results template
            return render_template('results.html', grouped_lists=grouped_lists)
        else:
            return "No words found in the dictionary."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
