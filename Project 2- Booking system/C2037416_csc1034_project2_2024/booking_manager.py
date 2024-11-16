from booking import Booking
from datetime import date, datetime, timedelta
import csv
class BookingManager:

    def __init__(self, bookings=None):
        self.bookings = bookings if bookings is not None else []

    def get_bookings(self):
        return self.bookings

    def __str__(self):
        return 'Booking Manager: {self.bookings}'

    def __repr__(self):
        return 'Booking Manager: booking = {self.bookings}'

    def add_booking(self, booking):
        for existing_booking in self.bookings:
            if booking.overlaps_with(existing_booking):
                raise ValueError("Booking overlaps with existing booking")

        self.bookings.append(booking)

    def remove_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)

    def edit_booking(self, old_booking, new_booking):
        if old_booking in self.bookings:
            self.bookings.remove(old_booking)
            self.bookings.append(new_booking)

    def search_by_room(self, room):
        found = []
        for booking in self.bookings:
            if room == booking.get_room():
                found.append(booking)
        return found


    def search_by_start(self, date1, time1):
        found = []
        for booking in self.bookings:
            if date1 == booking.get_date() and time1 == booking.get_time():
                found.append(booking)
        return found

    def search_for_room_timetable(self, date_from, date_to, room):
        for booking in self.bookings:
            if date_from in Booking.get_start and date_to in Booking.get_start and room in Booking.get_room:
                return self.bookings

    def get_available_rooms(self, start, hours, all_rooms):
        end = start + timedelta(hours=hours)
        occupied_rooms = set()
        for booking in self.bookings:
            booking_start = booking.get_start()
            booking_end = booking_start + timedelta(hours=booking.get_hours())
            
            if start < booking_end and end > booking_start: # Check for overlap
                occupied_rooms.add(booking.get_room()) # If overlap is true add room to set
                print(f"Room {booking.get_room()} is occupied at stated time")

        if not occupied_rooms:
            print("All rooms are available")
        
        available_rooms = [room for room in (all_rooms) if room not in occupied_rooms]
        return available_rooms
                


    def load_from_file(self, file_name):
        with open(file_name, "r") as read_file:
            read = csv.reader(read_file)
            next(read)  # Skip the first row
            for row in read:
                room,date1,time1,hours,title,contact = row
                booking = Booking(
                    room=room,
                    date1=datetime.strptime(date1, "%d/%m/%Y"),  # Ensures date1 is a date 
                    time1=datetime.strptime(time1, "%H:%M"),  # Ensures time1 is a time 
                    hours=int(hours), 
                    title=title,
                    contact=contact
                )
                self.bookings.append(booking)


    def save_to_file(self, file_name):
        # Save bookings to a CSV file
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for booking in self.bookings:
                writer.writerow([
                    booking.get_room(),
                    booking.get_start(),
                    booking.get_hours(),
                    booking.get_title(),
                    booking.get_contact()
                ])