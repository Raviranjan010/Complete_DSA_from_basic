#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Book Node Structure
struct Book {
    int id;
    string title;
    string author;
    bool isIssued;
    Book* next;
};

// Head pointer for Linked List
Book* head = nullptr;

// Function to create a new book node
Book* createBook(int id, string title, string author) {
    Book* newBook = new Book;
    newBook->id = id;
    newBook->title = title;
    newBook->author = author;
    newBook->isIssued = false;
    newBook->next = nullptr;
    return newBook;
}

// Function to add a new book
void addBook() {
    int id;
    string title, author;
    cout << "\nEnter Book ID: ";
    cin >> id;
    cin.ignore();
    cout << "Enter Book Title: ";
    getline(cin, title);
    cout << "Enter Author Name: ";
    getline(cin, author);

    Book* newBook = createBook(id, title, author);

    if (head == nullptr) {
        head = newBook;
    } else {
        Book* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newBook;
    }
    cout << "✅ Book Added Successfully!\n";
}

// Function to display all available books
void displayBooks() {
    if (head == nullptr) {
        cout << "\n📚 No books available in the library.\n";
        return;
    }

    cout << "\n📖 Available Books:\n";
    cout << "-----------------------------------------------\n";
    Book* temp = head;
    while (temp != nullptr) {
        cout << "ID: " << temp->id << " | Title: " << temp->title
             << " | Author: " << temp->author
             << " | Status: " << (temp->isIssued ? "Issued" : "Available") << endl;
        temp = temp->next;
    }
    cout << "-----------------------------------------------\n";
}

// Function to search for a book by ID or Title
void searchBook() {
    if (head == nullptr) {
        cout << "\n📚 No books available.\n";
        return;
    }

    int choice;
    cout << "\nSearch Book By:\n1. ID\n2. Title\nEnter choice: ";
    cin >> choice;
    cin.ignore();

    Book* temp = head;
    bool found = false;

    if (choice == 1) {
        int id;
        cout << "Enter Book ID: ";
        cin >> id;

        while (temp != nullptr) {
            if (temp->id == id) {
                cout << "\n✅ Book Found!\n";
                cout << "ID: " << temp->id << ", Title: " << temp->title
                     << ", Author: " << temp->author
                     << ", Status: " << (temp->isIssued ? "Issued" : "Available") << endl;
                found = true;
                break;
            }
            temp = temp->next;
        }
    } else if (choice == 2) {
        string title;
        cout << "Enter Book Title: ";
        getline(cin, title);

        while (temp != nullptr) {
            if (temp->title == title) {
                cout << "\n✅ Book Found!\n";
                cout << "ID: " << temp->id << ", Title: " << temp->title
                     << ", Author: " << temp->author
                     << ", Status: " << (temp->isIssued ? "Issued" : "Available") << endl;
                found = true;
                break;
            }
            temp = temp->next;
        }
    } else {
        cout << "❌ Invalid choice!\n";
        return;
    }

    if (!found)
        cout << "❌ Book not found.\n";
}

// Function to issue a book
void issueBook() {
    if (head == nullptr) {
        cout << "\n📚 No books available.\n";
        return;
    }

    int id;
    cout << "\nEnter Book ID to Issue: ";
    cin >> id;

    Book* temp = head;
    while (temp != nullptr) {
        if (temp->id == id) {
            if (!temp->isIssued) {
                temp->isIssued = true;
                cout << "✅ Book Issued Successfully!\n";
            } else {
                cout << "❌ Book is already issued.\n";
            }
            return;
        }
        temp = temp->next;
    }
    cout << "❌ Book not found.\n";
}

// Function to return a book
void returnBook() {
    if (head == nullptr) {
        cout << "\n📚 No books available.\n";
        return;
    }

    int id;
    cout << "\nEnter Book ID to Return: ";
    cin >> id;

    Book* temp = head;
    while (temp != nullptr) {
        if (temp->id == id) {
            if (temp->isIssued) {
                temp->isIssued = false;
                cout << "✅ Book Returned Successfully!\n";
            } else {
                cout << "❌ Book was not issued.\n";
            }
            return;
        }
        temp = temp->next;
    }
    cout << "❌ Book not found.\n";
}

// Function to sort books alphabetically by title
void sortBooks() {
    if (head == nullptr || head->next == nullptr) {
        cout << "\n📚 Not enough books to sort.\n";
        return;
    }

    for (Book* i = head; i != nullptr; i = i->next) {
        for (Book* j = i->next; j != nullptr; j = j->next) {
            if (i->title > j->title) {
                swap(i->id, j->id);
                swap(i->title, j->title);
                swap(i->author, j->author);
                swap(i->isIssued, j->isIssued);
            }
        }
    }
    cout << "✅ Books Sorted Alphabetically!\n";
}

// Main Menu
int main() {
    int choice;
    do {
        cout << "\n========== 📚 Library Book Management System 📚 ==========\n";
        cout << "1. Add New Book\n";
        cout << "2. Display All Books\n";
        cout << "3. Search Book\n";
        cout << "4. Issue Book\n";
        cout << "5. Return Book\n";
        cout << "6. Sort Books Alphabetically\n";
        cout << "7. Exit\n";
        cout << "===========================================================\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: addBook(); break;
            case 2: displayBooks(); break;
            case 3: searchBook(); break;
            case 4: issueBook(); break;
            case 5: returnBook(); break;
            case 6: sortBooks(); break;
            case 7: cout << "👋 Exiting... Thank you!\n"; break;
            default: cout << "❌ Invalid choice! Please try again.\n";
        }
    } while (choice != 7);

    return 0;
}
