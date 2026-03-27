class Book:
    def __init__(self, title, author, pages, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved

        self.material = "бумага"
        self.has_text = True

    def print_details(self):
        if self.is_reserved:
            print(f"Название: {
                    self.title}, Автор: {
                    self.author}, страниц: {
                    self.pages}, " f"материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {
                    self.title}, Автор: {
                    self.author}, страниц: {
                    self.pages}, " f"материал: {self.material}")


book1 = Book("Идиот", "Достоевский", 500, "978-5-1234")
book2 = Book("Война и мир", "Толстой", 1200, "978-5-5678")
book3 = Book("Мастер и Маргарита", "Булгаков", 450, "978-5-9012")
book4 = Book("1984", "Оруэлл", 300, "978-5-3456")
book5 = Book("Преступление и наказание", "Достоевский", 600, "978-5-7890")

book3.is_reserved = True

print("--- Книги ---")
book1.print_details()
book2.print_details()
book3.print_details()
book4.print_details()
book5.print_details()


class SchoolBook(Book):
    def __init__(
        self,
        title,
        author,
        pages,
        isbn,
        subject,
        school_class,
        has_exercises,
        is_reserved=False,
    ):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def print_details(self):
        if self.is_reserved:
            print(f"Название: {
                    self.title}, Автор: {
                    self.author}, страниц: {
                    self.pages}, " f"предмет: {
                    self.subject}, класс: {
                    self.school_class}, зарезервирована")
        else:
            print(
                f"Название: {
                    self.title}, Автор: {
                    self.author}, страниц: {
                    self.pages}, "
                f"предмет: {self.subject}, класс: {self.school_class}"
            )


textbook1 = SchoolBook("Алгебра", "Иванов", 200, "978-11-111", "Математика", 9, True)
textbook2 = SchoolBook(
    "История России", "Петров", 350, "978-22-222", "История", 8, False
)
textbook3 = SchoolBook("Физика", "Сидоров", 280, "978-33-333", "Физика", 10, True)

textbook2.is_reserved = True

print("\n---Учебники---")
textbook1.print_details()
textbook2.print_details()
textbook3.print_details()
