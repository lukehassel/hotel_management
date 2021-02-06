__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"


import random

from domain.entities.customer import Customer
from domain.entities.room.double_room import DoubleRoom
from domain.entities.room.room import Room
from domain.entities.room.single_room import SingleRoom
from domain.entities.room.suite import Suite


class ReceptionUseCase:
    """

    Class for creating new customers

    :attribute reservations: Holds all the reservations.
    """

    reservations = []

    def createReservation(self, name, visits, room_type):
        """

        Creates a new Customer in the system.

        :param name: The name of the new customer.
        :param visits: The hotel visits of the new customer.
        :param room_type: The room type the new customer wants to rent.
        """
        customer = Customer()
        customer.setName(name)
        customer.setHotelVisits(visits)
        customer.setCustomerId(random.randint(999, 999999999999))

        room = Room()

        if isinstance(room_type, type(DoubleRoom())):
            room = DoubleRoom()
        if isinstance(room_type, type(SingleRoom())):
            room = SingleRoom()
        if isinstance(room_type, type(Suite())):
            room = Suite()

        room.setKey(False)
        room.setRoomNumber(random.randint(1, 300))
        customer.setRoom(room)

        self.reservations.append(customer)
