import abc
from typing import TypeVar
from cis301.phonebill.abstract_phone_bill_ import abstract_phone_bill

class phone_bill_dumper():
    def _subclasshook__(cis,subclass):
        return (hasattr(subclass,'dump') and callable(subclass.dump) or not_implemented)

    T = TypeVar('T',bounds= abstract_phone_bill)

    def dump(bill:T):
        if not isinstance(bill,abstract_phone_bill):
            raise expectation("Invalid object type. Expected types of abstract methods ")
        pass

