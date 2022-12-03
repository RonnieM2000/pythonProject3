from cis302.phonebill.abstract_phonecall import abstract_phonecall
from datetime import tim, datetime

class PhoneCall(abstract_phonecall):
    time_format = "%H:%M"

    def __init__(self,caller,callee,start,end):
        self.caller = caller
        self.callee = callee
        self.start = start
        self.end = end

        self.parse_times(start,end)

    def parse_times(self,given_start,given_end):
        start = datetime.strptime((given_start,self.time_format))
        end = datetime.strptime((given_end,self.time_format))

        self.start = start.time()
        self.end = end.time()

    def get_caller(self)->str:
        return self.caller

    def get_callee(self)->str:
        return self.callee

    def get_starttime(self)->str:
        return self.start

    def get_starttime_string(self)->str:
        return self.start_str

    def get_endtime(self)->str:
        return self.end

    def get_endtime_string(self)->str:
        return self.end_str

