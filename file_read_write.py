def file_read_write():
    try:
        # Ask user for input file name
        input_file = input("Enter the filename to read from: ")

        # Open the file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask user for output file name
        output_file = input("Enter the filename to write to: ")

        # Write modified content to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File has been read from '{input_file}' and written to '{output_file}' successfully!")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
file_read_write()
