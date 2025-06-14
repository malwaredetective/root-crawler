import sqlite3

def create_database():
    # Create the SQLite Database
    conn = sqlite3.connect('root_crawler.db')
    cursor = conn.cursor()

    # Create a Table with the Specified Schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS levels (
            level INTEGER NOT NULL,
            difficulty TEXT NOT NULL,
            hint TEXT NOT NULL,
            flag TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        )
    ''')

    print("The table was created successfully!")

    # LEVEL (INT), DIFFICULTY (STRING), HINT (STRING), FLAG (STRING), COMPLETED (BOOL)
    data = [
        (0, 'easy', 'Enumerate your SUDO privileges.', '207eeec707affb4ab39ffb63dc3df9e8', False),
        (1, 'medium', 'This operating system seems outdated. Thoroughly enumerate all aspects of your SUDO configuration, including what version of SUDO you are running.', '739d80f289f091f1d5faf12cfd25fe83', False),
        (2, 'hard', 'This challenge will test your knowledge about cracking passwords. What files does your low-privilege user have read access to? Be on the hunt for something that does not belong.', '0e818a27a3fea74347a605528f334e3f', False),
        (3, 'easy', 'What files does your low-privilege user have write access to? Keep an eye out for something that does not belong.', '370b6eb5bc21ff135c9a92c371c4f422', False),
        (4, 'easy', 'What files does your low-privilege user have write access to? Be on the hunt for something that does not belong.', 'b93841e55f11579f2203690ce64be128', False),
        (5, 'easy', 'Everybody makes mistakes. Think about the actions your past self took to solve this challenge.', 'd216d3c4b24304fc4674c728c2ececf4', False),
        (6, 'easy', 'Did we really need root privileges to compile this binary?', '8ee7c23a901076e22e8b6ec407c190fd', False),
        (7, 'medium', 'I think you are more than CAPABLE of solving the problem. Enumerate carefully and check for binaries with elevated privileges.', '49f17dbc98399bf6b9753487b48a6ff3', False),
        (8, 'medium', 'I think you are more than CAPABLE of solving the problem. Enumerate carefully and check for binaries with elevated privileges.', '93b02d0e7fee22a6efd60585989ccdcd', False),
        (9, 'medium', 'The vim binary that khub provided you can do more than just read files.', '144f541844236aaac836ae692552c262', False),
        (10, 'easy', 'What other files could you read?', '6430891943122750375619a89b596833', False),
        (11, 'medium', 'I forgot the password, I wonder if there is a way that I use a dictionary attack to crack the password?', 'd87f33aad39073e70d184d10ddb6562b', False),
        (12, 'medium', 'How does Python know where to look to find other modules?', '4d9a6b848f0a30e67acaa797e4c68b49', False), 
        (13, 'medium', 'Thoroughly enumerate all aspects of your SUDO configuration', '29a23565f022a110bc2b895c7ddd2d75', False),
        (14, 'medium', 'Thoroughly enumerate all aspects of your SUDO configuration', 'a623362224d97f447b70ea9dfd13cca4', False),
        (15, 'medium', 'What version of exiftool is installed?', '815825d292b7c79656b61b5917b49e9b', False),
        (16, 'hard', 'Wildcards can be dangerous ...', 'eaed4b44cef9917de41953cc2f2a0806', False),
        (17, 'easy', 'Where does WordPress store it\'s configuration files?', '78c994e2cba1dc7531dd1bbe30de7583', False),
        (18, 'medium', 'When was the last time this instances packages were updated?', '66ffe0e495cd6d7a3f550c3c72989616', False),
        (19, 'hard', 'How are these logs getting rotated?', 'null', False)
    ]
    
    cursor.executemany('''
        INSERT INTO levels (level, difficulty, hint, flag, completed)
        VALUES (?, ?, ?, ?, ?)
    ''', data)

    print("The data was inserted successfully!")

    # Commit the Changes and Close the Connection
    conn.commit()
    conn.close()
    print("The database connection was closed.")

if __name__ == "__main__":
    create_database()
