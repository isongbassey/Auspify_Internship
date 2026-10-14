tasks =  []
 
while True:
    task = input("Enter a task:")
    if task == "done":
        break
    
    tasks.append({"name":task, "completed": False})
    
for task in tasks:
    print(task["name"])
 
    
while True:
    completed_task = input("Enter a task you have completed:")
    if completed_task == "done":
        break
    
    for task in tasks:
        if task["name"] == completed_task:
            task["completed"] = True
            
for task in tasks:
    print(task)
    
while True:
    delete_task = input("delete task you want to remove:")
    if delete_task == "done":
        break
 
    for task in tasks:
        if task["name"] == delete_task:
            tasks.remove(task)
            break
           
for task in tasks:
    print(task)
