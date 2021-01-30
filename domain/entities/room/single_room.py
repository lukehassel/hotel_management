from domain.entities.room.room import Room


class SingleRoom(Room):
    def setRoomNumber(self, number):
        super().setRoomNumber(number)

    def getRoomNumber(self):
        return super().getRoomNumber()

    def setKey(self, key):
        super().setKey(key)

    def getKey(self):
        return super().getKey()