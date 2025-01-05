from enum import Enum

class CustomerType(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    @classmethod
    def get_priority(cls, customer_type):
        priorities = {
            cls.LOW: 'low',
            cls.MEDIUM: 'medium',
            cls.HIGH: 'high'
        }
        return priorities.get(customer_type)