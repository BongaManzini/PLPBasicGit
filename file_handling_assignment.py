def create_and_write_file():
    try:
        with open('my_file.txt', 'w') as file:
            # Write three lines of text including strings and numbers
            file.write("This is the first line.\n")
            file.write("The number is 12345.\n")
            file.write("Here is the third line of text.\n")
        print("File 'my_file.txt' created and written successfully.")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating or writing to the file: {e}")
    
    finally:
        print("File creation and writing attempt finished.")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            # Read the contents of the file
            contents = file.read()
            # Display the contents on the console
            print("Contents of 'my_file.txt':")
            print(contents)
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    
    finally:
        print("File reading attempt finished.")

def append_to_file():
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            # Append three additional lines of text
            file.write("This is an appended line 1.\n")
            file.write("This is an appended line 2.\n")
            file.write("This is an appended line 3.\n")
        print("Additional lines appended successfully.")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")
    
    finally:
        print("File appending attempt finished.")
      
create_and_write_file()
read_file()
append_to_file()
read_file()  # To verify that the content has been appended
