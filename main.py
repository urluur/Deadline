num_tasks = int(input())
tasks = [] # list of tuples (deadline, time_to_complete)

# read all tasks from stdin
for _ in range(num_tasks):
  deadline, time_to_complete = map(int, input().split())
  tasks.append((deadline, time_to_complete))

# sort by time to complete
tasks.sort(key=lambda task: task[1])


total_time_elapsed = 0
total_score = 0

# calculate total score
for task in tasks:
  deadline, time_to_complete = task
  task_score = deadline - (time_to_complete + total_time_elapsed)
  total_score += task_score
  total_time_elapsed += time_to_complete

print(total_score)