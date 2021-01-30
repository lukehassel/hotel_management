class Room:
    RoomNumber = ""
    Keys = False

    def setRoomNumber(self, number):
        self.RoomNumber = number

    def getRoomNumber(self):
        return self.RoomNumber

    def setKey(self, key):
        self.Keys = key

    def getKey(self):
        return self.Keys
