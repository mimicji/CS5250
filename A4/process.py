class Process:
    last_scheduled_time = 0
    id = -1
    arrive_time = -1
    burst_time = -1

    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time

    #for printing purpose
    def __repr__(self):
        return ('[id %d : arrival_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))

class Process_SJF(Process):
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
        self.pred_time = 0
    def __lt__(self, other):
        return self.pred_time < other.pred_time or self.pred_time == other.pred_time and self.arrive_time < other.arrive_time
