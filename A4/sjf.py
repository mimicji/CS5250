from queue import PriorityQueue
from process import Process_SJF

def SJF_scheduling(process_list, alpha=0.5, init_time = 5):
    tasks = []
    waiting_time = 0
    for process in process_list:
        tasks.append(Process_SJF(process.id, process.arrive_time, process.burst_time))
        waiting_time -= process.arrive_time
    result_schedule = []
    queue = PriorityQueue()
    current_time = 0
    pred_history = {}
    while not queue.empty() or tasks:
        while (tasks) and (tasks[0].arrive_time <= current_time):
            process = tasks[0]
            tasks = tasks[1:]
            if process.id in pred_history:
                new_pred = alpha * pred_history[process.id][1] + (1 - alpha) * pred_history[process.id][0]
                pred_history[process.id] = [new_pred, process.burst_time]
            else:
                pred_history[process.id] = [init_time, process.burst_time]
            process.pred_time = pred_history[process.id][0]
            queue.put(process)
        if queue.empty():
            current_time = tasks[0].arrive_time
            continue

        current_process = queue.get()
        if (not result_schedule or current_process != previous_process):
            result_schedule.append((current_time, current_process.id))
        waiting_time += current_time
        current_time += current_process.burst_time
        previous_process = current_process
    average_waiting_time = waiting_time / float(len(process_list))
    return result_schedule, average_waiting_time
