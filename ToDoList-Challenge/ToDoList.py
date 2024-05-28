         
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def isCompleted(self):
        return self.completed

    def markCompleted(self):
        self.completed = True

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def addToDo(self, task):
        newNode = Node(task)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def markToDoAsCompleted(self, title):
        current = self.head
        while current is not None:
            if current.task.getTitle() == title:
                current.task.markCompleted()
                return
            current = current.next
    # def markToDoAsCompleted(self,title):
#         current = self.head
#         prev =None
        
#         while current!=None:
#             if current.task.getTitle() == title:
#                 prev.next = current.next
#             else:
#                 prev = current
#                 current = current.next
#                 prev.next=current
    def viewToDoList(self):
        current = self.head
        nums = 0
        while current is not None:
            nums += 1
            task = current.task
            status = "Completed" if task.isCompleted() else "Not Completed"
            print(f"Task {nums}: {task.getTitle()} - {task.getDescription()} [{status}]")
            current = current.next

task1 = Task("Task 1", "Description 1")
task2 = Task("Task 2", "Description 2")
task3 = Task("Task 3", "Description 3")

todo_list = ToDoList()
todo_list.addToDo(task1)
todo_list.addToDo(task2)
todo_list.addToDo(task3)

todo_list.viewToDoList()

todo_list.markToDoAsCompleted("Task 2")
print("\nAfter marking Task 2 as completed:\n")
todo_list.viewToDoList()
