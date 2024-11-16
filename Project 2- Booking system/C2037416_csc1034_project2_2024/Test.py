from booking import Booking
from booking_manager import BookingManager
from datetime import datetime, timedelta, time

def main():
    
    # Loading sample data
    manager = BookingManager()
    manager.load_from_file("sample_data.csv")

    # Test overlapping bookings and test data
    start_date_1 = datetime.strptime("04/11/2024", "%d/%m/%Y")
    start_time_1 = datetime.strptime("13:00", "%H:%M")
    start_date_2 = datetime.strptime("04/11/2024", "%d/%m/%Y")
    start_time_2 = datetime.strptime("14:00", "%H:%M")
    booking_1 = Booking("FDC.G.41", start_date_1, start_time_1, 3, "CSC1034 Lecture", "jennifer.warrender@newcastle.ac.uk")
    booking_2 = Booking("FDC.G.41", start_date_2, start_time_2, 3, "CSC1034 Lecture", "jennifer.warrender@newcastle.ac.uk")
    
    # Check if equal
    assert booking_1 != booking_2, "Bookings should not be equal"

    # Check if overlap
    assert booking_1.overlaps_with(booking_2), "Bookings should overlap"
    
    # Print bookings
    print("Booking 1:", booking_1)
    print("Booking 2:", booking_2)

    # Test overlapping bookings
    booking_3 = Booking("FDC.G.43", start_date_1, start_time_1 - timedelta(hours=3), 1, "CSC1035 Tutorial", "john.doe@newcastle.ac.uk")
    assert not booking_1.overlaps_with(booking_3), "Bookings should not overlap"

    # Test adding a booking
    manager.add_booking(booking_1)

    # Try adding an overlapping booking 
    try:
        manager.add_booking(booking_2)
    except ValueError:
        print("Booking overlaps with another booking")

    # Add non-overlapping booking
    manager.add_booking(booking_3)

    # Testing search by room
    bookings_in_room = manager.search_by_room("FDC.G.41")
    assert len(bookings_in_room) == 7, "There should be 7 bookings in room FDC.G.41"

    # Testing search by start
    bookings_at_start = manager.search_by_start(start_date_1.date(),start_time_1.time())
    assert len(bookings_at_start) == 1, "There should be 1 booking starting at start_date_1"

    # Testing get available rooms - should return FDC.G.41 and USB.1.006
    all_rooms = ["FDC.G.41", "FDC.G.42", "FDC.G.43", "FDC.G.44", "FDC.G.45", "USB.1.006", "USB.1.007", "USB.1.008"]
    chosen_datetime = datetime.strptime("14/11/2024 10:30", "%d/%m/%Y %H:%M")
    available_1 = manager.get_available_rooms(chosen_datetime, 3, all_rooms)
    print("Available rooms:", available_1)
    print("All tests passed.")


main()

