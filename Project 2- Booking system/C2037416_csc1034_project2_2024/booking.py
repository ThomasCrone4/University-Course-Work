from datetime import date, time

class Booking:

    def __init__(self, room, start, hours, title, contact):
        if not isinstance(room, str):
            raise TypeError("Room must be a string")
        self.room = room 

        if not isinstance(start, date):
            raise TypeError("Start must be a date")
        if not self.is_weekday(start):
            raise ValueError("Start date must be a weekday")
        if not Booking.is_within_hours(start):
            raise ValueError("Start time must be within hours (9:00 - 18:00)")
        self.start = start

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

    def get_start(self):
        return self.start
    
    @staticmethod
    def is_weekday(input_date):
        # Check if the start date is a weekday (Monday to Friday)
        return input_date.weekday() < 5
    
    @staticmethod
    def is_within_hours(input_datetime):
        # Define opening hours
        start_time = time(9, 0)   # 9:00 AM
        end_time = time(18, 0)    # 6:00 PM

        # Extract the time part from the input datetime
        input_time = input_datetime.time()
        
        # Check if input_time is within business hours
        return start_time <= input_time <= end_time

    def get_hours(self):
        return self.hours

    def get_title(self):
        return self.title

    def get_contact(self):
        return self.contact

    def __str__(self):
        out = "Booking: {room}, {start}, {hours}, {title}, {contact}"
        return out.format(room = self.get_room(),
                          start = self.get_start(),
                          hours = self.get_hours(),
                          title = self.get_title(),
                          contact = self.get_contact())
    def __repr__(self):
        return (f"Booking(room= {self.room}, start= {self.start}, "
                f"hours= {self.hours}, title= {self.title}, "
                f"contact= {self.contact})")

    def __eq__(self, other):
        if obj1[room,start +hours] == obj1[room,start]
        pass
        """Returns true/false"""

    def __hash__(self):
        pass

    def overlaps_with(self, other):
        """if obj1[room,start +hours] == obj1[room,start]
            return True
        else: 
            return False
        pass
        Returns true/false"""
