__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

class Room:

    """
        This class represents a Room in the hotel management system.

        attribute RoomNumber: The Room Number.
        attribute Keys: The key of the Room.
    """

    RoomNumber = ""
    Keys = False

    def setRoomNumber(self, number):
        """
        Sets a new Room Number.

        :param number: The room number.
        """
        self.RoomNumber = number

    def getRoomNumber(self):
        """

        :return: Returns the Room number of the room.
        """
        return self.RoomNumber

    def setKey(self, key):
        """
        Sets The Room Number of the Room.
        :param key: The new Key.
        """
        self.Keys = key

    def getKey(self):
        """

        :return: Returns if the Key is in the hand of the Hotel or the Customer.
        """
        return self.Keys
