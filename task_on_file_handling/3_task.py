def check_file_closed(filename):
    try:
        file = open(filename, 'r')
        if (file.closed):
            print("The file is closed.")
        else:
            print("The file is open.")

    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the filename to check:")
check_file_closed(filename)
