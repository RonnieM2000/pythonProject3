from abc import ABC, abstractmethod
from datetime import date
from typing import final

class abstract_phonecall(ABC):
    def get_caller(self) -> str:

            returns:
                the number of the caller

        pass

    def get_callee(self) -> str:
            returns:
                the number of the person that was called
        pass

    def get_starttime(self) -> date:
            returns:
                what time the phone call was placed
        pass

    def get_endtime(self) -> date:
            returns:
                what time the call was ended
        pass

    def __str__ (self)->str:

            return:
                "The phone call was recieved from"+ self.get_caller()+"placed to"+self.get_callee()+\
                "from"+ self.get_starttime_string()+\ "to" + self.get_endtime_string()