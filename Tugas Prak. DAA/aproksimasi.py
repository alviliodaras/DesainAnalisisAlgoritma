def schedule_tasks(tasks, deadline):
    scheduled_tasks = []
    current_time = 0

    while current_time < deadline and tasks:
        next_task = max(tasks, key=lambda x: x['priority'])
        if current_time + next_task['duration'] <= deadline:
            scheduled_tasks.append(next_task)
            current_time += next_task['duration']
        tasks.remove(next_task)

    return scheduled_tasks

# Contoh penggunaan
tasks = [
    {'name': 'Tugas A', 'duration': 3, 'priority': 2},
    {'name': 'Tugas B', 'duration': 2, 'priority': 1},
    {'name': 'Tugas C', 'duration': 4, 'priority': 3},
    {'name': 'Tugas D', 'duration': 1, 'priority': 2}
]
deadline = 6

scheduled_tasks = schedule_tasks(tasks, deadline)

print("Tugas yang terjadwal:")
for task in scheduled_tasks:
    print(task['name'])
