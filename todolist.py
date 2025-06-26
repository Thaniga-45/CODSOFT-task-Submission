todolist=[]

#adding a new  task

def add_task():
    task = input("enter your task:")
    todolist.append({"task":task , "status":"pending"})
    print("new task added successfully!:\n")
    
# check the task for view
    
def view_task():
    print("your Todo List")
    if len(todolist)==0:
        print("no pending task")
    else:
        for index,task in enumerate(todolist,1):
            print(f" {index}. { task['task'] }  - {task['status'] }" )
    print('\n')
    
#remove a task from list
    
def remove_task():
    
    if len(todolist)==0:
        print("list is empty")
    else:
        
            search_index=int(input("enter the task number that  you want to remove :")) -1
            if 0<= search_index <len(todolist):
                remove_task= todolist.pop(search_index)
                print(f"Task Removed:{remove_task['task']}")
            else:
                print("invalid task number")
                print('\n')
                
 #create a mark completion process
                
def mark_done():
      if len(todolist)==0:
        print("list is empty")
      else:
        try:
            search_index=int(input("enter the task number that  you want to mark as complete :")) -1
            if 0<= search_index <len(todolist):
               todolist[search_index]['status'] ='done'
               print(f"task{ todolist [search_index]['task']}has been marked as Done.")
            else:
                print("invalid task number:\n")
        except ValueError:
            print("the")

#fuction as menu list
    
def menu():
    while(True):
        
        print("*** main menu ***")
        print("1.add a task")
        print("2.view all task")
        print("3.remove a task")
        print("4.Mark as completed")
        print("5.Exist")
        
        choices =input("enter your choices:")
        if choices =="1":
            add_task()
        elif choices=="2":
            view_task()
        elif choices=="3":
            remove_task()
        elif choices=="4":
            mark_done()
        elif choices=="5":
            print("Existing the application:\n")
            
        else :
            print("invalid choices! try again")
menu()
             
        
