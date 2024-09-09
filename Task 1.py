import csv
import os

def extract_text_from_csv(output_file):
    current_directory = os.getcwd()  # Get the current working directory
    with open(output_file, 'w') as txt_file:
        for filename in os.listdir(current_directory):
            if filename.endswith('.csv'):
                csv_path = os.path.join(current_directory, filename)
                with open(csv_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        txt_file.write(' '.join(row) + '\n')

if __name__ == "__main__":
    output_file = input("Enter the name of the output .txt file: ")
    extract_text_from_csv(output_file)
    print(f"Text from all CSV files has been written to {output_file}")
