def get_task(tasks):
    tasks_after = []
    next = tasks[0]
    if len(tasks) >= 2:
        tasks_after = tasks[1:]
    return (next, tasks_after)

def run_task(process, current_time, time_quantum, tasks, last_preempt_time):
    if process.burst_time <= time_quantum:
        current_time += process.burst_time
    else:
        current_time += time_quantum
        process.burst_time -= time_quantum
        tasks.append(process)
    last_preempt_time[process.id] = current_time
    return (current_time, tasks, last_preempt_time)

def RR_scheduling(process_list, time_quantum):
    result_schedule = []
    tasks = []
    last_preempt_time = dict()
    process_list_len = len(process_list)

    current_time = 0
    waiting_time = 0

    while len(tasks) or len(process_list):
        if len(tasks):
            (process, tasks) = get_task(tasks)
            waiting_time += current_time - last_preempt_time[process.id]
            result_schedule.append((current_time, process.id))
            (current_time, tasks, last_preempt_time)=run_task(process, current_time, time_quantum, tasks, last_preempt_time)
        else:
            current_time = process_list[0].arrive_time
        if len(process_list):
            new_incoming_tasks = []
            not_arrived_tasks = []
            for process in process_list:
                if process.arrive_time <= current_time:
                    new_incoming_tasks.append(process)
                else:
                    not_arrived_tasks.append(process)
            process_list = not_arrived_tasks
            tasks = new_incoming_tasks + tasks
            for process in new_incoming_tasks:
                last_preempt_time[process.id] = process.arrive_time
    return result_schedule, float(waiting_time)/float(process_list_len)
