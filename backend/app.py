from flask import Flask, request, jsonify
import helpers

app = Flask(__name__)

@app.route('/find-permutations', methods=['POST'])
def find_permutations():
    data = request.json
    center_letter = data.get('centerLetter', '').strip().lower()
    additional_letters = [letter.strip().lower() for letter in data.get('additionalLetters', '').split(",")]

    input_csv_file = "most_words.csv"  # Replace this with the actual CSV file name if different

    sorted_permutations = helpers.generate_sorted_permutations(center_letter, additional_letters, input_csv_file)

    return jsonify({
        'success': True,
        'permutations': sorted_permutations
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
