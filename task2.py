def write_and_append_to_file(filename):
    try:
        # Step 1: Write to the file
        user_input = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(user_input + '\n')
        print("Data successfully written to", filename)

        # Step 2: Append to the file
        append_input = input("\nEnter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(append_input + '\n')
        print("Data successfully appended.")

        # Step 3: Read and display file contents
        print("\nFinal content of", filename + ":")
        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    write_and_append_to_file("output.txt")
