import abc
from typing import TypeVar
from cis301.phonebill.abstract_phonebill import abstract_phone_bill

class phone_bill_parser():
    def __subclasshook__(cis,subclass):
        return (hasattr(subclass, 'dump') and callable(subclass.dump) or not_implemented)

    T = TypeVar('T', bounds=abstract_phone_bill)

    def parse(self)-> abstract_phone_bill:

        pass