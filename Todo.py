
def addTask(tasks,task):
    tasks.append(task)

def removeTask(tasks,rmtask):
    tasks.remove(rmtask)
def viewTask(tasks):
    for x in tasks:
        print(x)

def main():
    tasks=[]
    while True:
        print("---Menu---")
        print("1.addTask")
        print("2.removeTask")
        print("3.viewTask")
        print("4.exit")

        choice=input("Enter your choice : ")

        if choice=='1':
            task = input("input a task : ")
            addTask(tasks,task)
        elif choice=='2':
            rmTask = input("enter a task that you want to remove : ")
            removeTask(tasks,rmTask)
        elif choice=='3':
            viewTask(tasks)
        elif choice=='4':
            print("----Terminating----")
            break
        else :
            print("invalid input")
main()