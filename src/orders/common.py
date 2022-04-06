from enum import Enum

class OrderStatus(Enum):
    '''para imitar las opciones que le trabajo status pueda almacenar'''
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    
choices = [(tag, tag.value) for tag in OrderStatus]