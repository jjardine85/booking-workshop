"""Small booking application for the version-control workshop."""
import argparse

CONFIRMATION = "Booking confirmed for {attendees} attendee(s)."


def validate_attendees(attendees):
    """Validate an integer attendee count, raising ValueError if invalid."""
    if type(attendees) is not int:
        raise ValueError("Enter a whole number of attendees.")
    if attendees < 1:
        raise ValueError("At least one attendee is required.")
    if attendees > 10:
        raise ValueError("Maximum of 10 attendees allowed.")


def create_booking(attendees):
    """Return a confirmation for a valid booking."""
    validate_attendees(attendees)
    return CONFIRMATION.format(attendees=attendees)


def main():
    parser = argparse.ArgumentParser(description="Create a workshop booking.")
    parser.add_argument("attendees", type=int, help="Number of attendees")
    args = parser.parse_args()
    try:
        print(create_booking(args.attendees))
    except ValueError as error:
        parser.exit(1, f"Booking rejected: {error}\n")


if __name__ == "__main__":
    main()
