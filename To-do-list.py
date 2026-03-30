todo_list=[]

#function of add the task
def add_task():
    task=input("Enter the Task :")
    todo_list.append({"task":task, "Status":"pending"})
    print("New Task is Added Succesfully\n :")
    
#function of view all the task
def view_task():
    print(" Your To Do List Task......:")
    if len(todo_list)==0:
        print(" No pending Task ")
    else:
        for index,task in enumerate(todo_list,1):
            print(f" {index} : {task['task']}  -  {task['Status']} ")
    print("\n")
    
#function to remove the task    
def remove_task():
    if len(todo_list)==0:
        print("\n List is Empty :")
    else:
        try:
            search_index=int(input("Enter the Task number that you want to remove:"))-1
            if 0 <=search_index<len(todo_list):
                removed_task=todo_list.pop(search_index)
                print(f"Task Removed : {removed_task}")
            else:
                print("Invalid Task Number..")
        except ValueError:
            print("Please Enter a Valid Task Number:")
            
#function to marke a task as done
def marke_done():
     if len(todo_list)==0:
        print("\n List is Empty :")
     else:
            try:
                search_index=int(input("Enter the Task number that you want to marke as complete:"))-1
                if 0 <=search_index<len(todo_list):
                        todo_list[search_index]['Status']='done'
                        print(f"Task {todo_list[search_index]['task']}  has been marked as done.")
                else:
                    print("Invalid Task Number..")
            except ValueError:
                print("Please Enter a Valid Task Number:")
        
#function to Display a Task
def menu():
    while(True):
        print("\n************Main Menu**************")
        print("1. Add  a  New Task :")
        print("2. View  all Task :")
        print("3. Remove Task :")
        print("4. Marke a Task :")
        print("5. Exit :")


        choice_=input(" Enter your Choice :")
        if choice_=="1":
            add_task()
        elif choice_=="2":
            view_task()
        elif choice_=="3":
            remove_task()
        elif choice_=="4":
            marke_done()
        elif choice_=="5":
            print("Existing from Application...!")
        else:
            print("Invalid Choice ! Try Again.!!!")
            
menu()            
            
        

    
    
