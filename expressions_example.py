def read_user_score(filename):
    """
    Reads a numeric score from a text file.
    
    Demonstrates try/except/else/finally:
    - try: attempt to open and read the file
    - except: handle specific errors if something goes wrong
    - else: process the data only if reading succeeded
    - finally: always runs, used here for cleanup confirmation
    """

    file = None

    try:
        # Risky: file might not exist, or might not be readable
        file = open(filename, "r")
        content = file.read().strip()
        score = int(content)  # Risky: content might not be a number

    except FileNotFoundError:
        # File doesn't exist at all
        print(f"Error: '{filename}' not found.")
        return None

    except ValueError:
        # File exists but the content isn't a valid number
        print(f"Error: File content is not a valid number.")
        return None

    else:
        # Only runs if try succeeded with zero exceptions
        print(f"Score loaded successfully: {score}")
        return score

    finally:
        # Always runs — success or failure
        if file:
            file.close()
        print("File operation complete.")
