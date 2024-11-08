def extract_words_from_file(file_path):
    words_list = []  # List to hold the words from each line

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip leading/trailing whitespace and split line into words
                words = line.strip().split()
                words_list.extend(words)  # Append the list of words to the main list

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return words_list

# Example usage
if __name__ == "__main__":
    file_path = 'bad_passwords.txt'  # Replace with your text file path
    result = extract_words_from_file(file_path)
    print(result)
