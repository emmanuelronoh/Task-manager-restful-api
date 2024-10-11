tasks = {}
next_id = 1

def add_task(title):
    global next_id
    tasks[next_id] = {"id": next_id, "title": title, "done": False}
    next_id += 1
    return tasks[next_id - 1]

def get_tasks():
    return list(tasks.values())

def get_task(task_id):
    return tasks.get(task_id)

def update_task(task_id, title, done):
    if task_id in tasks:
        tasks[task_id]['title'] = title
        tasks[task_id]['done'] = done
        return tasks[task_id]
    return None

def delete_task(task_id):
    return tasks.pop(task_id, None)
