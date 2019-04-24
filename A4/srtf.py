from queue import PriorityQueue
from process import Process_SRTF

def SRTF_scheduling(process_list):
    tasks = []
    waiting_time = 0
    for process in process_list:
        tasks.append(Process_SRTF(process.id, process.arrive_time, process.burst_time))
        waiting_time -= process.burst_time
    current_time = 0
    result_schedule = []
    current_process = -1
    previous_process = -1
    queue = PriorityQueue()
    while not queue.empty() or tasks:
        while tasks and tasks[0].arrive_time <= current_time:
            queue.put(tasks[0])
            tasks = tasks[1:]
        if queue.empty():
            current_time = tasks[0].arrive_time
            continue
        current_process = queue.get()
        if previous_process != current_process:
            result_schedule.append((current_time, current_process.id))
        if tasks and current_time + current_process.burst_time > tasks[0].arrive_time:
            current_process.burst_time -= tasks[0].arrive_time - current_time
            current_time = tasks[0].arrive_time
            queue.put(current_process)
        else:
            current_time += current_process.burst_time
            waiting_time += current_time - current_process.arrive_time
        previous_process = current_process

    average_waiting_time = waiting_time/float(len(process_list))
    return result_schedule, average_waiting_time
