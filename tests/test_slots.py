import unittest

from app.slots import can_book, slots_left


class BookingTests(unittest.TestCase):
    def test_counts_open(self):
        self.assertEqual(slots_left(20, 15), 5)

    def test_never_below_zero(self):
        self.assertEqual(slots_left(20, 25), 0)

    def test_small_booking_fits(self):
        self.assertTrue(can_book(20, 18, party_size=2))

    def test_full_day_refuses_booking(self):
        self.assertFalse(can_book(20, 20))

    def test_card_limit_refuses_a_bigger_booking(self):
        self.assertFalse(can_book(100, 0, party_size=3))
