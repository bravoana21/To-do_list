# To-do List

def add_task(todo_list):
    new_task = input('Which new task do you want to add?    ')
    todo_list.setdefault(new_task, '[ ]')
    return todo_list

def view_tasks(todo_list):
    for task, mark in todo_list.items():
        print(mark + ' ' + task)

def mark_task(todo_list):
    while True:
        done_task = input('Which task do you want to mark?  ')
        if done_task in todo_list:
            todo_list[done_task] = '[#]'
            delete_tasks = input('''Do you want to eliminate any marked task?
            a. Yes, the one just marked.        b. Yes, another one.
            c. Yes, all marked tasks.           d. No.
                                 ''')
            if delete_tasks == 'a':
                del todo_list[done_task]
            elif delete_tasks == 'b':
                done_task2 = input('Which task do you want to eliminate?  ')
                del todo_list[done_task2]
            elif delete_tasks == 'c':
                for task, mark in todo_list.items():
                    if mark == '[#]':
                        del todo_list[task]
            elif delete_tasks != 'd':
                print('Please write a valid option.')

            other_tasks = input('''Do you want to mark any other task?
            a. Yes.        b. No.
                                 ''')
            if other_tasks == 'a':
                continue
            elif other_tasks != 'b':
                print('Please write a valid option.')
            
            return todo_list
        else:
            rethink = input('''Maybe you rather add a new option or view the list.
            a. yes, I'd like to add a new option.        
            b. yes, I'd like to view the list
            c. no
                                ''')
            if rethink == 'a':
                return add_task(todo_list)
            elif rethink == 'b':
                return view_tasks(todo_list)
            elif rethink != 'c':
                print('Please write a valid option.')

todo_list = {}
print('Hi there!')
while True:
    user_response = input('''What would you like to do? (please write only one letter [a, b, c, d])
            a. Add a task.        b. View tasks.
            c. Mark tasks.        d. Exit program.
                          ''')
    if user_response == 'a':
        add_task(todo_list)
    elif user_response == 'b':
        view_tasks(todo_list)
    elif user_response == 'c':
        mark_task(todo_list)
    elif user_response == 'd':
        print('It was a pleasure, goodbye.')
        break
    else:
        print('Please write a valid option.')