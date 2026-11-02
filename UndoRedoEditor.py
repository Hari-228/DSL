class stack:
    def __init__(self):
        self.itmes=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if self.items.is_empty():
            return None
        return self.items.pop() # Removes and returns the top of the stack
    def peek(self):
        if self.items.is_empty():
            return None 
        return self.items[-1] #REturns the top of the stack i.e the last element of the stack
    def is_empty(self):
        return  len(self.items)==0
    def size(self):
        return len(self.items)

class UndoRedoEditor:
    def __init__(self):
        self.doc=""
        self.undos=stack()
        self.redos=stack()
    def make_change(self,text):
        #Push the current state of the doc to the undostack and then append the text 
        self.undos.push(self.doc)
        self.doc+=text
        self.redos=stack() #clear redp history on new change
        print(f"Change made:added '{text}'")
        self.dispays()
    def undo (self):
        if self.undos.is_empty():
            print("Nothing to Undo")
            return 
        print(f"Top of the stack {self.undos.peek()}")
        self.redos.push(self.doc) #stores the current state of the stack 
        self.doc=self.undos.pop()
        print("Undo performed")
        self.displays()
    def redo(self):
        if self.redos.is_empty():
            print("Nothong to redo")
            return 
        print(f"Top if the stack {self.redos.peek()}")
        self.undos.push(self.doc) # storing the current state 
        self.doc=self.redos.pop()
        print("Redo performed")
        self.displays()
    def displays(self):
        print("Current document:",self.doc)
        print(f"Top of undo stack:{self.undos.peek()}")
        print(f"Top of redo stack:{self.redos.peek()}")
    def main():
        editor=UndoRedoEditor()
        while True:
         print("""
========== Undo/Redo Text Editor ==========
1. Make a Change
2. Undo
3. Redo
4. Display Document State
5. Exit
=============================================
""")
         choice=input("Enter your choice from (1-5): ")
         match choice:
             case 1:
                 text=input("Enter to the document")
                 editor.make_change()
             case 2:
                 editor.undo()
             case 3:
                 editor.redo()
             case 4:
                 editor.displays()
             case 5:
                 print("Exited Editor")
                 return 
             case _:
                 print("Entered Invalid choice")

if __name__ == "__main__":
    main()

             
        


        
