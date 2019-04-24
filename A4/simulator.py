#!/usr/bin/python
import copy
import argparse
from process import Process
from fcfs import FCFS_scheduling
from rr import RR_scheduling
from srtf import SRTF_scheduling
from sjf import SJF_scheduling

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', action='store', default='./input.txt')
parser.add_argument('--time_quantum', action='store', default=2)
parser.add_argument('--init_time', action='store', default=5)
parser.add_argument('--alpha', action='store', default=0.5)
args = parser.parse_args()


def read_input():
    result = []
    input_file = args.input_file
    with open(input_file) as f:
        for line in f:
            array = line.split()
            if (len(array)!= 3):
                IOError("Wrong input format")
            result.append(Process(int(array[0]),int(array[1]),int(array[2])))
    return result

def write_output(file_name, schedule, avg_waiting_time):
    with open(file_name,'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f \n'%(avg_waiting_time))


def main():
    process_list = read_input()
    print ("---- Printing Input ----")
    for process in process_list:
        print (process)
    print ("---- Simulating FCFS ----")
    FCFS_schedule, FCFS_avg_waiting_time =  FCFS_scheduling(process_list)
    write_output('FCFS.txt', FCFS_schedule, FCFS_avg_waiting_time )
    print ("---- Simulating RR ----")
    rr_process = copy.deepcopy(process_list)
    time_quantum = args.time_quantum
    RR_schedule, RR_avg_waiting_time =  RR_scheduling(rr_process,time_quantum )
    write_output('RR.txt', RR_schedule, RR_avg_waiting_time )
    print ("---- Simulating SRTF ----")
    srtf_process = copy.deepcopy(process_list)
    SRTF_schedule, SRTF_avg_waiting_time =  SRTF_scheduling(srtf_process)
    write_output('SRTF.txt', SRTF_schedule, SRTF_avg_waiting_time )
    print ("---- Simulating SJF ----")
    alpha = float(args.alpha)
    init_time = args.init_time
    sjf_process = copy.deepcopy(process_list)
    SJF_schedule, SJF_avg_waiting_time =  SJF_scheduling(sjf_process, alpha, init_time)
    write_output('SJF.txt', SJF_schedule, SJF_avg_waiting_time)
    print ("---- Normal Exit ----")
    return

if __name__ == '__main__':
    main()
