__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

from domain.entities.room.room import Room


class Customer:

    """
        This class represents a Customer of the hotel.

        attribute customerId: The Id of the Customer.
        attribute name: The name of the Customer.
        attribute room: The room the Customer has booked.
        attribute hotel_visits: The hotel visits the customer has made in the past.
    """

    customerId = ""
    name = ""
    room = Room()
    hotel_visits = 0

    def getRoom(self):
        """

        :returns: The room of the customer.
        """
        return self.room

    def setRoom(self, room):
        """

        :param room: Sets the room of the customer.
        """
        self.room = room

    def setCustomerId(self, customerId: str):
        """

        :param customerId: Sets a new customer Id of the customer.
        """
        self.customerId = customerId

    def getCustomerId(self):
        """

        :returns: The customer Id.
        """
        return self.customerId

    def setName(self, name: str):
        """

        :param name: Sets the name of the customer.
        """
        self.name = name

    def getName(self):
        """

        :returns: The name of the Customer.
        """
        return self.name

    def setHotelVisits(self, hotel_visits: int):
        """

        :param hotel_visits: Sets the number of hotel visits of the customer.
        """
        self.hotel_visits = hotel_visits

    def getHotelVisits(self):
        """

        :returns: The Hotel Visits of the customer.
        """
        return self.hotel_visits
