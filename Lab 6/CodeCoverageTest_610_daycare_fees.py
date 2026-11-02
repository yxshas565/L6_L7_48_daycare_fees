import pytest
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


class TestExtraHoursFee:

    def test_unknown_age_group(self):
        with pytest.raises(ValueError):
            extra_hours_fee("school", 30, False)

    def test_negative_hours(self):
        with pytest.raises(ValueError):
            extra_hours_fee("infant", -1, False)

    def test_hours_within_included_limit(self):
        assert extra_hours_fee("toddler", 20, False) == 0

    def test_hours_equal_included_limit(self):
        assert extra_hours_fee("preschool", 30, False) == 0

    def test_sibling_adjustment(self):
        assert extra_hours_fee("toddler", 30, True) == 0

    def test_infant_extra_fee(self):
        assert extra_hours_fee("infant", 25, False) == 70

    def test_non_infant_extra_fee(self):
        assert extra_hours_fee("toddler", 30, False) == 45

    def test_infant_high_extra_fee(self):
        assert extra_hours_fee("infant", 41, False) == 462

    def test_non_infant_high_extra_fee(self):
        assert extra_hours_fee("preschool", 51, False) == 294


class TestEnrolmentAllowed:

    def test_immunisation_pending_age_sufficient(self):
        assert enrolment_allowed(12, 0, True) is True

    def test_immunisation_pending_age_insufficient(self):
        assert enrolment_allowed(11, 5, True) is False

    def test_age_below_minimum(self):
        assert enrolment_allowed(5, 3, False) is False

    def test_no_vacancies(self):
        assert enrolment_allowed(24, 0, False) is False

    def test_valid_enrolment(self):
        assert enrolment_allowed(24, 2, False) is True


class TestPickupStatus:

    def test_aftercare_on_time(self):
        assert pickup_status(20, True, False) == "on_time"

    def test_regular_pickup_on_time(self):
        assert pickup_status(10, False, False) == "on_time"

    def test_friday_cutoff(self):
        assert pickup_status(20, False, True) == "on_time"

    def test_aftercare_late(self):
        assert pickup_status(10, True, False) == "late"

    def test_regular_pickup_late(self):
        assert pickup_status(0, False, False) == "late"

    def test_overdue(self):
        assert pickup_status(-6, False, False) == "overdue"

    def test_friday_overdue(self):
        assert pickup_status(4, False, True) == "overdue"
