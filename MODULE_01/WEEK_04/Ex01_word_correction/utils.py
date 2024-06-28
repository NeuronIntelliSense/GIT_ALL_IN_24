import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levenshtein_distance(src_word, tar_word):
    if len(src_word) == 0:
        return len(tar_word)

    if len(tar_word) == 0:
        return len(src_word)

    # Initialize the matrix
    rows = len(src_word) + 1
    cols = len(tar_word) + 1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows):
        matrix[i][0] = i

    for i in range(1, cols):
        matrix[0][i] = i

    # Update the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if src_word[i-1] == tar_word[j-1]:
                sub_cost = 0
            else:
                sub_cost = 1

            matrix[i][j] = min(matrix[i-1][j] + 1,
                               matrix[i][j-1] + 1,
                               matrix[i-1][j-1] + sub_cost)

    return matrix[rows-1][cols-1]


def run(file_path):
    vocabs = load_vocab(file_path)

    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word: ')

    if st.button("Compute"):
        lv_distances = {}
        for vocab in vocabs:
            lv_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(
            sorted(lv_distances.items(), key=lambda item: item[1]))

        correct_word = list(sorted_distances.keys())[0]
        st.write(f'Correct word: {correct_word}')

        col1, col2 = st.columns(2)
        col1.write('Vocabulary: ')
        col1.write(vocabs)

        col2.write('Distances: ')
        col2.write(sorted_distances)
