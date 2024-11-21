def error_handling_lab():
    try:
        # Prompt user for filename
        filename = input("Enter the filename to read: ").strip()

        if not filename:
            print("No filename entered. Exiting.")
            return

        # Attempt to read the file
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:\n", content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    error_handling_lab()
