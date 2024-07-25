from datetime import datetime, timedelta, time

# Initialize data structure to store bookings
seats = {i: [] for i in range(1, 28)}

# Define the slot timings for each duration
slot_timings = {
    1: [(time(7, 0), time(8, 0)), (time(8, 0), time(9, 0)), (time(9, 0), time(10, 0)), 
        (time(10, 0), time(11, 0)), (time(11, 0), time(12, 0)), (time(12, 0), time(13, 0)), 
        (time(13, 0), time(14, 0)), (time(14, 0), time(15, 0)), (time(15, 0), time(16, 0)), 
        (time(16, 0), time(17, 0)), (time(17, 0), time(18, 0)), (time(18, 0), time(19, 0)), 
        (time(19, 0), time(20, 0)), (time(20, 0), time(21, 0))],
    2: [(time(7, 0), time(9, 0)), (time(8, 0), time(10, 0)), (time(9, 0), time(11, 0)),
        (time(10, 0), time(12, 0)), (time(11, 0), time(13, 0)), (time(12, 0), time(14, 0)),
        (time(13, 0), time(15, 0)), (time(14, 0), time(16, 0)), (time(15, 0), time(17, 0)),
        (time(16, 0), time(18, 0)), (time(17, 0), time(19, 0)), (time(18, 0), time(20, 0)),
        (time(19, 0), time(21, 0))],
    3: [(time(7, 0), time(10, 0)), (time(8, 0), time(11, 0)), (time(9, 0), time(12, 0)),
        (time(10, 0), time(13, 0)), (time(11, 0), time(14, 0)), (time(12, 0), time(15, 0)),
        (time(13, 0), time(16, 0)), (time(14, 0), time(17, 0)), (time(15, 0), time(18, 0)),
        (time(16, 0), time(19, 0)), (time(17, 0), time(20, 0)), (time(18, 0), time(21, 0))],
    6: [(time(7, 0), time(13, 0)), (time(8, 0), time(14, 0)), (time(9, 0), time(15, 0)),
        (time(10, 0), time(16, 0)), (time(11, 0), time(17, 0)), (time(12, 0), time(18, 0)),
        (time(13, 0), time(19, 0)), (time(14, 0), time(20, 0)), (time(15, 0), time(21, 0))],
    9: [(time(7, 0), time(16, 0)), (time(8, 0), time(17, 0)), (time(9, 0), time(18, 0)),
        (time(10, 0), time(19, 0)), (time(11, 0), time(20, 0)), (time(12, 0), time(21, 0))],
    12: [(time(7, 0), time(19, 0)), (time(8, 0), time(20, 0)), (time(9, 0), time(21, 0))]
}

# Function to check for overlapping slots considering the booking end date
def is_overlapping(existing_slots, new_slot, current_date):
    for slot in existing_slots:
        if slot['end_date'] > current_date and not (new_slot[1] <= slot['start_time'] or new_slot[0] >= slot['end_time']):
            return True
    return False

# Function to remove expired bookings
def remove_expired_bookings(current_date):
    for seat in seats:
        seats[seat] = [slot for slot in seats[seat] if slot['end_date'] > current_date]

# Function to book a slot
def book_slot():
    duration = int(input("Enter slot duration (1, 2, 3, 6, 9, 12 hours): "))
    if duration not in slot_timings:
        print("Invalid duration.")
        return

    # List available seats
    print("Available seats:")
    for seat in seats:
        print(seat, end=" ")
    print()

    seat_no = int(input("Choose a seat number: "))
    if seat_no not in seats:
        print("Invalid seat number.")
        return

    # List available slots for the chosen seat
    current_date = datetime.now()
    remove_expired_bookings(current_date)
    print(f"Available {duration}-hour slots for seat {seat_no}:")
    available_slots = [slot for slot in slot_timings[duration] if not is_overlapping(seats[seat_no], slot, current_date)]
    if not available_slots:
        print("No available slots for this seat.")
        return

    for idx, slot in enumerate(available_slots):
        print(f"{idx + 1}. {slot[0].strftime('%I:%M %p')} - {slot[1].strftime('%I:%M %p')}")

    slot_choice = int(input("Choose a slot number: ")) - 1
    if slot_choice < 0 or slot_choice >= len(available_slots):
        print("Invalid slot choice.")
        return

    chosen_slot = available_slots[slot_choice]

    # Ask for the number of months
    months = int(input("How many months are you booking the slot for? "))

    # Calculate the end date of the booking
    end_date = current_date + timedelta(days=30 * months)

    # Book the slot
    seats[seat_no].append({
        'start_time': chosen_slot[0],
        'end_time': chosen_slot[1],
        'end_date': end_date
    })
    print(f"Slot booked for seat {seat_no} from {chosen_slot[0].strftime('%I:%M %p')} to {chosen_slot[1].strftime('%I:%M %p')} for {months} month(s).")

# Main program
while True:
    print("Courage Library Slot Booking System")
    print("1. Book a Slot")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_slot()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")
