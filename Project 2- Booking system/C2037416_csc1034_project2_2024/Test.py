from booking import *
from datetime import datetime

def main():
    start_date = datetime.strptime("04/11/2024" + " " + "9:00", "%d/%m/%Y %H:%M")
    booking_1 = Booking("FDC.G.41", start_date, 3, "CSC1034 Lecture", "jennifer.warrender@newcastle.ac.uk")
    print(booking_1)
    x = repr(booking_1)
    print(x)
main()
