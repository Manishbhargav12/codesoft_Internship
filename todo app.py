def display(tasklist):
    print("These are your task :")
    for i,tasklist in enumerate(tasklist):
        print(f"{i+1}. {tasklist}")

def create(tasklist):
    task=str(input("Enter a new task:"))
    tasklist.append(task)

def update(tasklist):
    oldtask=str(input("Enter a old task:"))
    if oldtask in tasklist:
        tasklist.remove(oldtask)
        task=str(input("Enter a new task:"))
        tasklist.append(task)
    else:
        print("Task not found")
def delete(tasklist):
    oldtask=str(input("Enter your task which you want to delete:"))
    if oldtask in tasklist:
        tasklist.remove(oldtask)
    else:
        print("Task not found")

def todoapp():
    tasklist=[]
    totaltask=int(input("How many tasks are there:"))
    for i in range (1,totaltask+1):
        task=(input("Enter your task:"))
        tasklist.append(task)
        
    while True:
        display(tasklist)
        print(("Enter what do you want to do ? \n 1.add \n 2.update \n 3.delete \n 4.view \n 5.stop"))
        operation=int(input("Choose an option (1-5):"))
        if operation==1:
            create(tasklist)
        elif operation==2:
            update(tasklist)
        elif operation==3:
            delete(tasklist)
        elif operation==4:
            display(tasklist)
        elif operation==5:
            print("STOPPING...")
            break
        else:
            print("enter a valid integer")
todoapp()