from domain.entities.room.room import Room


class Customer:
    customerId = ""
    name = ""
    room = Room()
    hotel_visits = 0

    def setCustomerId(self, customerId: str):
        self.customerId = customerId

    def getCustomerId(self):
        return self.customerId

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name

    def setHotelVisits(self, hotel_visits: int):
        self.hotel_visits = hotel_visits

    def getHotelVisits(self):
        return self.hotel_visits
