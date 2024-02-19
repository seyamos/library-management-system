#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Library:             
    def __init__(self):    # Constructer method - to open the books.txt file
        self.file = open("books.txt", "a+")

    def __del__(self):     # Destructor method - to close the file.
        self.file.close()
        
        
    def list_books(self):                      
        self.file.seek(0)    # To read and write the file go to the beginning of the file.
        lines = self.file.read().splitlines()  # Read the file and split it into rows. Get each row as a list element
      
        if not lines:
            print("book list is empty")
        else:                                  
            for line in lines:
                book_info = line.split(",")    # To split a row with a comma
                book_title, book_author = book_info[0], book_info[1]                      
                print(f"Title: {book_title}, Author: {book_author}")   
    
    def add_book(self):
        # Get details by asking the user
        book_title = input("Enter book title to add: ")         
        book_author = input("Enter book author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_title},{book_author},{release_year},{num_pages}\n"  # Create a row for book details

        self.file.write(book_info)         # Add the "book info" row to the file 
        print(f"{book_title}, added ")     
    
    def remove_book(self, title_to_delete):       
        self.file.seek(0)
        lines = self.file.read().splitlines()      
       
        # navigate each line of the file with a "for loop".              
        for i, line in enumerate(lines):      # Enumerate function returns both the index of the line and the content
            book_title = line.split(",")[0]   # Split the line with a comma and get its first element
            if book_title == title_to_delete: 
                del lines[i]                  
                print(f"{book_title}, deleted ")
                break
            
        self.file.seek(0)      # Returns to the beginning of the file.             
        self.file.truncate()   # Clears the contents of the file.
                                          
        for line in lines:                 # It loops through each line of the file again. 
            self.file.write(line + "\n")   # Adds other books back to the file.
            
    # Count by the title of the book. (extra feature)
    def count_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        book_counts = {}  # Create an empty dictionary
        
        for line in lines:
            book_title = line.split(",")[0]    # Get the title of each line inside the loop
            if book_title in book_counts:      # If this title already exists in dictionary 
                book_counts[book_title] += 1   # increase the corresponding value by one
            else:
                book_counts[book_title] = 1    # If not, assign the value 1

        for title, count in book_counts.items():  # Print each title and corresponding number in the dictionary
            print(f"{title}: {count} adet")
            
    
lib = Library()
           
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Count the books")
    print("q) Exit the program")
    
    menu_choice = input("Enter your choice (1/2/3/4 or q): ")  
    print("      ")    
        
    if menu_choice == "1":
        print("Kitap Listesi")
        lib.list_books()
    elif menu_choice == "2":
        lib.add_book()
    elif menu_choice == "3":
        title_to_delete = input("Enter book title to delete: ")
        lib.remove_book(title_to_delete)
    elif menu_choice == "4":
        print("Kitap Sayısı")
        lib.count_books()
    elif menu_choice == "q":     
        print("The program has been exited.")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or q.")

    print("      ")


# In[ ]:




