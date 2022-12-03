from abc import abstractmethod, ABC
from typing import Typevar,list,final

from cis301.phonebill.abstract_phonecall import abstract_phone_call

class abstract_phone_bill(ABC):
    def get_customer(self) -> str:
            returns
                the customers name
        pass

    def get_phonecalls(self)-> list[T]:
            returns:
                every call made

    def __str__(self) -> str:
            returns:
                a lay out of the phone bill
            return self.get_customer() + "phone bills that have" + len(self.get_phonecalls()) + "phone calls"
