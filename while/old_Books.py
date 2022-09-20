book_name = input()
count = 0
is_book_found = False
book_found = input()

while book_found != "No More Books":
    if book_name == book_found:
        is_book_found = True
        print(f"You checked {count} books and found it.")
        break
    else:
        count += 1
        book_found = input()
if not is_book_found:

    print(f"The book you search is not here!")
    print(f"You checked {count} books.")
