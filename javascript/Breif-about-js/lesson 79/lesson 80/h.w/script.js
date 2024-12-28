// Base class
class Book {
    constructor(title, author, year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    // Static method
    static isBookInstance(obj) {
        return obj instanceof Book;
    }

    // Method to display book info
    displayInfo() {
        return `Title: ${this.title}, Author: ${this.author}, Year: ${this.year}`;
    }
}

// Derived class
class Library {
    constructor(name) {
        this.name = name;
        this.books = [];
    }

    // Method to add a book to the library
    addBook(book) {
        if (Book.isBookInstance(book)) {
            this.books.push(book);
        } else {
            console.log("Only instances of Book can be added.");
        }
    }

    // Method to display library info
    displayLibraryInfo() {
        let bookInfo = this.books.map(book => book.displayInfo()).join("<br>");
        return `Library: ${this.name}<br>Books:<br>${bookInfo}`;
    }
}

// Create instances
const book1 = new Book("to wish", "Harper Lee", 1960);
const myLibrary = new Library("City Library");
myLibrary.addBook(book1);
myLibrary.addBook(new Book("1984", "George Orwell", 1949));

// Display information
document.getElementById("book1").innerHTML = book1.displayInfo();
document.getElementById("library").innerHTML = myLibrary.displayLibraryInfo();
