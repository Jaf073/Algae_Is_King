def read_hashes_from_binary(input_file, output_file):
    try:
        with open(input_file, 'rb') as binary_file:
            # Read the entire binary file
            content = binary_file.read()
        
        # Split content by the stop byte (0xFF)
        hashes = content.split(b'\xFF')
        
        # Decode bytes to string and filter out empty hashes
        decoded_hashes = []
        for hash in hashes:
            if hash:
                decoded_hash = hash.decode('utf-8', errors='ignore')  # Decode with error handling
                # Remove non-ASCII characters
                filtered_hash = ''.join(filter(lambda x: x.isascii(), decoded_hash))
                decoded_hashes.append(filtered_hash)

        # Write the decoded hashes to the output text file
        with open(output_file, 'w') as text_file:
            for hash in decoded_hashes:
                if hash:  # Write only non-empty hashes
                    text_file.write(f"{hash}\n")

        print(f"Successfully extracted {len(decoded_hashes)} hashes to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify input and output file paths
    input_file_path = 'hashes.bin'  # Change this to your input binary file path
    output_file_path = 'ListHash.txt'  # Change this to your desired output text file path
    
    read_hashes_from_binary(input_file_path, output_file_path)
