import csv
from collections import Counter
import re


def count_words_in_text(file_path):
    # Opening and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Using regular expressions to find all words (alphanumeric only)
    words = re.findall(r'\b\w+\b', text.lower())  # Convert to lowercase for case-insensitive counting

    # Counting the occurrences of each word
    word_counts = Counter(words)

    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)

    return top_30_words


def save_to_csv(word_counts, output_file):
    # Write the word counts to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Word', 'Count'])
        # Write the top 30 words and their counts
        writer.writerows(word_counts)


def main():
    input_file = 'combined.txt'
    output_csv = 'top 30.csv'

    # Counting words and get the top 30
    top_30_words = count_words_in_text(input_file)

    # Saving the top 30 words to a CSV file
    save_to_csv(top_30_words, output_csv)

    print(f"The top 30 words and their counts have been saved to {output_csv}")


if __name__ == "__main__":
    main()
