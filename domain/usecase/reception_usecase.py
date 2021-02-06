import random

from domain.entities.customer import Customer
from domain.entities.room.double_room import DoubleRoom
from domain.entities.room.room import Room
from domain.entities.room.single_room import SingleRoom
from domain.entities.room.suite import Suite


class ReceptionUseCase:
    reservations = []

    def createReservation(self, name, visits, room_type):

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

    def get_reservations(self):
        return self.reservations
