import Queue

def update_queue(current_time, tasks, queue):
    # This ugly implementation is to solve the problem raised below
    new_queue = Queue.Queue()
    while tasks and tasks[0].arrive_time <= current_time:
        new_queue.put(tasks[0])
        tasks = tasks[1:]
    while not queue.empty():
        new_queue.put(queue.get())
    return tasks, new_queue

def RR_scheduling(tasks, time_quantum):
    result_schedule = []
    process_list_len = len(tasks)
    queue = Queue.Queue()
    current_time = 0
    waiting_time = 0
    current_process = -1
    previous_process = -1
    for process in tasks:
        waiting_time -= process.burst_time + process.arrive_time
    while not queue.empty() or tasks:
        tasks, queue = update_queue(current_time, tasks, queue)
        if queue.empty():
            current_time = tasks[0].arrive_time
            continue
        current_process = queue.get()
        if previous_process != current_process:
            result_schedule.append((current_time, current_process.id))
        if current_process.burst_time > time_quantum:
            current_process.burst_time -= time_quantum
            current_time += time_quantum
            # There is a problem here:
            #   If a new process arrives,
            #   it should have a priority to all existing processes or not?
            #   In this version, the answer is 'yes'.
            tasks, queue = update_queue(current_time, tasks, queue)
            queue.put(current_process)
        else:
            current_time += current_process.burst_time
            waiting_time += current_time
        previous_process = current_process
    average_waiting_time = waiting_time/float(process_list_len)
    return result_schedule, average_waiting_time
