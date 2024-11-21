def read_and_write_file():
    try:
        # File to read
        input_file = "input.txt"

        # Check if the file exists, create if it doesn't
        try:
            with open(input_file, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print("Input file doesn't exist. Creating a sample file.")
            with open(input_file, "w") as file:
                file.write("Hello, this is the original content.\n")
            with open(input_file, "r") as file:
                content = file.read()

        print("Original Content:\n", content)

        # Modify content
        modified_content = content.replace("original", "modified")

        # Write to a new file
        output_file = "output.txt"
        with open(output_file, "w") as file:
            file.write(modified_content)

        print("Modified content written to 'output.txt'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    read_and_write_file()
