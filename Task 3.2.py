from transformers import AutoTokenizer
import collections
import csv


def count_unique_tokens(file_path, model_name="bert-base-uncased"):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = collections.Counter(tokens)

    return token_counts


def write_top_tokens_to_csv(token_counts, output_file, top_n=30):
    top_tokens = token_counts.most_common(top_n)
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Token', 'Count'])
        writer.writerows(top_tokens)


if __name__ == "__main__":
    input_file = "combined.txt"
    output_file = "top_tokens.csv"

    token_counts = count_unique_tokens(input_file)
    write_top_tokens_to_csv(token_counts, output_file)

    print(f"The top 30 most common tokens have been written to {output_file}")
