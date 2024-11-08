def read_hashes_from_binary(input_file, output_file):
    try:
        with open(input_file, 'rb') as binary_file:
            # Read the entire binary file
            content = binary_file.read()

        for i in content:
            print(hex(i))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify input and output file paths
    input_file_path = 'hashes.bin'  # Change this to your input binary file path
    output_file_path = 'output_hashes.txt'  # Change this to your desired output text file path

    read_hashes_from_binary(input_file_path, output_file_path)

