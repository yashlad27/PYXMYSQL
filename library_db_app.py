import pymysql


def connect_to_db():
    """Prompt user for MySQL credentials and connect to LibraryDB."""
    while True:
        try:
            user = input("Enter MySQL username: ")
            password = input("Enter MySQL password: ")
            connection = pymysql.connect(
                host="localhost",
                user=user,
                password=password,
                database="librarylady",
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected to LibraryDB!")
            return connection
        except pymysql.MySQLError as e:
            print(f"Error connecting to database: {e}")
            print("Please try again.")


def fetch_genres(cursor):
    """Retrieve and display the list of genres."""
    cursor.execute("SELECT name FROM genre;")
    genres = [row["name"].lower() for row in cursor.fetchall()]

    if not genres:
        print("No genres found in the database!")
        return None

    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre.capitalize()}")

    return genres


from tabulate import tabulate  # Import tabulate for better table formatting

def call_book_has_genre(cursor, genre):
    """Call the stored procedure book_has_genre() and display results in a formatted table."""
    cursor.callproc("book_has_genre", [genre])
    results = cursor.fetchall()

    if not results:
        print(f"⚠️ No books found for genre '{genre.capitalize()}'.")
        return

    # Create a list of dictionaries for tabular display
    table_data = []
    for row in results:
        book_id = row.get("book_id", "N/A")
        title = row.get("title", "Unknown Title").strip()
        author = row.get("author", "Unknown Author").strip()
        pages = row.get("page_count", "N/A")
        publisher = row.get("publisher_name", "Unknown Publisher").strip()

        table_data.append([book_id, title, author, pages, publisher])

    # Define table headers
    headers = ["Book ID", "Title", "Author", "Pages", "Publisher"]

    # Print table using tabulate
    print("\n📚 Books in Selected Genre:")
    print(tabulate(table_data, headers=headers, tablefmt="grid", maxcolwidths=[15, 50, 20, 10, 30]))

def main():
    """Main function to run the menu-driven application."""
    connection = connect_to_db()
    cursor = connection.cursor()

    while True:
        print("\n Menu Options:")
        print("1: Generate a list of genres")
        print("2: Disconnect and exit")

        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            genres = fetch_genres(cursor)
            if not genres:
                continue

            while True:
                user_input = input("\nEnter a genre: ").strip().lower()
                if user_input in genres:
                    call_book_has_genre(cursor, user_input)
                    break
                else:
                    print("Invalid genre! Please choose from the listed genres.")

        elif choice == "2":
            print("Disconnecting from database.")
            cursor.close()
            connection.close()
            break

        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()