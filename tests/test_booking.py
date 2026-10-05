https://git-scm.com/cheat-sheet


"""Behaviour checks for the booking component."""
import unittest
from booking import create_booking, validate_attendees


class BookingTests(unittest.TestCase):
    def test_zero_attendees_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_attendees(0)

    def test_negative_attendees_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_attendees(-1)

    def test_one_attendee_is_accepted(self):
        validate_attendees(1)

    def test_five_attendees_are_accepted(self):
        validate_attendees(5)

    def test_ten_attendees_are_accepted(self):
        validate_attendees(10)

    def test_eleven_attendees_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_attendees(11)

    def test_non_integer_input_is_rejected(self):
        for value in ("2", 1.5, True, None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_attendees(value)

    def test_confirmation_includes_attendee_count(self):
        self.assertIn("5", create_booking(5))


if __name__ == "__main__":
    unittest.main()