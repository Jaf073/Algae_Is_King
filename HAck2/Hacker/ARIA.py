def read_hashes_from_binary(input_file, output_file):
    decoded_hashes = []
    try:
        with open(input_file, 'rb') as binary_file:
            # Read the entire binary file
            content = binary_file.read()
        
        # Split content by the stop byte (0xFF)
        #hashes = content.split(b'\xFF')
        hashes = content.split()

        # Decode bytes to string and filter out empty hashes
        for hash in hashes:
            decoded_hashes.append(hash.decode('utf-8'))

        #decoded_hashes = [hash.decode('utf-8') for hash in hashes if hash]
        #print(decoded_hashes)
        print("NEWLIST")
        newline = []
        for i in decoded_hashes:
            texx = ""
            for c in i:
                if c == 'ÿ':
                    newline.append(texx)
                else:
                    texx += c
        print(newline)

        #print(f"Successfully extracted {len(decoded_hashes)} hashes to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify input and output file paths
    input_file_path = 'hashes.bin'  # Change this to your input binary file path
    output_file_path = 'output_hashes.txt'  # Change this to your desired output text file path
    
    read_hashes_from_binary(input_file_path, output_file_path)
