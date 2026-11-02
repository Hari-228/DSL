
undo_stack = []
redo_stack = []
document = ""

def change(text):
    global document
    undo_stack.append(document)
    document += text
    redo_stack.clear()

def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document += undo_stack.pop()
    else:
        print("Nothing to undo!")

def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document += redo_stack.pop()
    else:
        print("Nothing to redo!")


while True:
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter new text: ")
        change(text)
        print("Document:", document)

    elif choice == "2":
        undo()
        print("Document:", document)

    elif choice == "3":
        redo()
        print("Document:", document)

    elif choice == "4":
        print("Document:", document)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
