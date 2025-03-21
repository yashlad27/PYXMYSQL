# LibraryDB Application

## Overview
This Python program connects to the **MySQL database (`librarylady`)**, retrieves book genres, allows users to select a genre, and displays books in that category using a **well-formatted table**.  
It uses **`pymysql`** for database connectivity and **`tabulate`** for table formatting.

---

## Installation and Setup

### **1. Prerequisites**
Ensure you have:
- **Python 3.x installed** (`python --version`)
- **MySQL Server installed and running**
- **Database `librarylady` set up with the required tables**
- **Stored procedure `book_has_genre(genre_p)` correctly implemented**

---

### **2. Install Required Python Libraries**
Run the following command to install dependencies:
```bash
pip install pymysql tabulate
```

---

## Running the Application

### **1. Start the Program**
To run the Python script, navigate to the project folder and execute:
```bash
python library_db_app.py
```

### **2. Enter MySQL Credentials**
The program will prompt for:
```
Enter MySQL username: root
Enter MySQL password: test123
```
**Note:** Ensure you use the correct credentials for MySQL.

---

## Features

### **1. Main Menu**
Once connected, the following options appear:
```
📌 Menu Options:
1: Generate a list of genres
2: Disconnect and exit
```
- **Enter `1`** to display available book genres.
- **Enter `2`** to disconnect and exit.

### **2️⃣ Selecting a Genre**
After choosing `1`, you will see a list of genres like:
```
Available Genres:
1. Mystery
2. Fantasy
3. Science Fiction
4. Accounting
5. Thriller
...
```
- **Type a genre name exactly as listed** (case-insensitive).
- Example:
  ```
  Enter a genre: Accounting
  ```

### **3. Displaying Books in a Genre**
If books exist for the genre, they will be displayed in a **formatted table**:
```
📚 Books in Selected Genre:
+---------------+----------------------------------------------------+----------------------+--------+------------------------+
| Book ID       | Title                                              | Author               | Pages  | Publisher              |
+---------------+----------------------------------------------------+----------------------+--------+------------------------+
| 9780749460211 | How to Understand Business Finance: Edition 2      | Unknown Author       | 176    | Kogan Page Publishers  |
| 9780814416259 | The Essentials of Finance and Accounting for       | Unknown Author       | 320    | AMACOM                 |
|               | Nonfinancial Managers                              |                      |        |                        |
| 9781601638618 | Financial Statements, Revised and Expanded Edition | Unknown Author       | 288    | Red Wheel/Weiser       |
+---------------+----------------------------------------------------+----------------------+--------+------------------------+
```
- If **no books exist** for a genre, the program displays:
  ```
  No books found for genre 'Romance'.
  ```

### **4️⃣ Handling Errors**
- **Invalid genres** prompt the user to enter again.
- **Invalid menu selections** display:
  ```
  Invalid choice! Please enter 1 or 2.
  ```
---