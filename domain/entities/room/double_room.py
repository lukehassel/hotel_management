__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

from domain.entities.room.room import Room


class DoubleRoom(Room):
    """
        Represents a Double Room in the Hotel.
    """

    def setRoomNumber(self, number):
        """
            All methods are overridden from the Room Class.
            For more information take a look at the Room Class.
        """
        super().setRoomNumber(number)

    def getRoomNumber(self):
        """
            All methods are overridden from the Room Class.
            For more information take a look at the Room Class.
        """
        return super().getRoomNumber()

    def setKey(self, key):
        """
            All methods are overridden from the Room Class.
            For more information take a look at the Room Class.
        """
        super().setKey(key)

    def getKey(self):
        """
            All methods are overridden from the Room Class.
            For more information take a look at the Room Class.
        """
        return super().getKey()
