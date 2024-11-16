from datetime import date, time, timedelta, datetime

class Booking:

    def __init__(self, room, date1, time1, hours, title, contact):
        if not isinstance(room, str):
            raise TypeError("Room must be a string")
        self.room = room 

        if not isinstance(date1, date):
            raise TypeError("Start must be a date")
        if not self.is_weekday(date1):
            raise ValueError("Start date must be a weekday")
        self.date1 = date1
        

        if not Booking.is_within_hours(time1):
            raise ValueError("Start time must be within hours (9:00 - 18:00)")
        self.time1 = time1

        if not isinstance(hours, int):
            raise TypeError("Hours must be an integer")
        self.hours = hours

        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title

        if not isinstance(contact, str):
            raise TypeError("Contact must be a string")
        self.contact = contact

    def get_room(self):
        return self.room
    
    def get_date(self):
        return self.date1.date()
    
    def get_time(self):
        return self.time1.time()
    
    def get_start(self):
        start_datetime = datetime.combine(self.get_date(), self.get_time())
        return (start_datetime)
    
    
    @staticmethod
    def is_weekday(input_date):
        # Check if the start date is a weekday
        return input_date.weekday() < 5
    
    @staticmethod
    def is_within_hours(input_datetime):
        # Define hours
        start_time = time(9, 0)   # 9:00 AM
        end_time = time(18, 0)    # 6:00 PM

        # Get the time from the input
        input_time = input_datetime.time()
        
        # Check if input_time is within hours
        return start_time <= input_time <= end_time

    def get_hours(self):
        return self.hours

    def get_title(self):
        return self.title

    def get_contact(self):
        return self.contact

    def __str__(self):
        return "Booking: {}, {}, {}, {}, {}".format(
            self.get_room(), self.get_date(), self.get_time(), self.get_hours(),
            self.get_title(), self.get_contact())
    
    def __repr__(self):
        return "Booking({}, {}, {}, {}, {})".format(
            self.get_room(), self.get_start(), self.get_time(), self.get_hours(),
            self.get_title(), self.get_contact())

    #Check if two bookings are equal
    def __eq__(self, other):
        if isinstance (other, Booking):
            return (
                self.get_room() ==  other.get_room() and
                self.get_start() == other.get_start() and
                self.get_hours() == other.get_hours() and
                self.get_title() == other.get_title() and
                self.get_contact() == other.get_contact()
                )
        return False

    def __hash__(self):
        return hash((self.get_room(), self.get_start(), self.get_hours(),
                    self.get_title(), self.get_contact()))

    #Check if two bookings overlap
    def overlaps_with(self, other):
        if self.get_room() != other.get_room():
            return False
        
        start_1 = self.get_start()
        end_1 = start_1 + timedelta(hours=self.get_hours())

        start_2 = other.get_start()
        end_2 = start_2 + timedelta(hours=other.get_hours())
        
        return end_1 > start_2 and end_2 > start_1
