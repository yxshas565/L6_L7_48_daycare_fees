import pytest
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


class TestExtraHoursFeeBranches:

    def test_unknown_age_group_branch(self):
        with pytest.raises(ValueError):
            extra_hours_fee("school", 30, False)

    def test_valid_age_group_branch(self):
        assert extra_hours_fee("infant", 20, False) == 0

    def test_negative_hours_branch(self):
        with pytest.raises(ValueError):
            extra_hours_fee("toddler", -5, False)

    def test_non_negative_hours_branch(self):
        assert extra_hours_fee("toddler", 25, False) == 0

    def test_sibling_non_infant_branch(self):
        assert extra_hours_fee("toddler", 31, True) == 9

    def test_sibling_infant_branch(self):
        assert extra_hours_fee("infant", 21, True) == 14

    def test_no_sibling_branch(self):
        assert extra_hours_fee("toddler", 26, False) == 9

    def test_no_extra_hours_branch(self):
        assert extra_hours_fee("preschool", 30, False) == 0

    def test_extra_hours_branch(self):
        assert extra_hours_fee("preschool", 31, False) == 9

    def test_infant_rate_branch(self):
        assert extra_hours_fee("infant", 21, False) == 14

    def test_non_infant_rate_branch(self):
        assert extra_hours_fee("preschool", 31, False) == 9

    def test_extra_hours_above_20_infant(self):
        assert extra_hours_fee("infant", 41, False) == 462

    def test_extra_hours_above_20_non_infant(self):
        assert extra_hours_fee("preschool", 51, False) == 294

    def test_extra_hours_not_above_20(self):
        assert extra_hours_fee("toddler", 26, False) == 9


class TestEnrolmentBranches:

    def test_immunisation_pending_true(self):
        assert enrolment_allowed(12, 0, True) is True

    def test_immunisation_pending_false(self):
        assert enrolment_allowed(24, 2, False) is True

    def test_pending_below_12_months(self):
        assert enrolment_allowed(11, 5, True) is False

    def test_age_below_6_months(self):
        assert enrolment_allowed(5, 2, False) is False

    def test_age_at_least_6_months(self):
        assert enrolment_allowed(6, 1, False) is True

    def test_vacancies_zero(self):
        assert enrolment_allowed(24, 0, False) is False

    def test_vacancies_available(self):
        assert enrolment_allowed(24, 1, False) is True


class TestPickupBranches:

    def test_aftercare_true(self):
        assert pickup_status(20, True, False) == "on_time"

    def test_aftercare_false(self):
        assert pickup_status(10, False, False) == "on_time"

    def test_friday_true(self):
        assert pickup_status(20, False, True) == "on_time"

    def test_friday_false(self):
        assert pickup_status(10, False, False) == "on_time"

    def test_on_time_boundary(self):
        assert pickup_status(10, False, False) == "on_time"

    def test_late_boundary(self):
        assert pickup_status(-5, False, False) == "late"

    def test_overdue_branch(self):
        assert pickup_status(-6, False, False) == "overdue"

    def test_aftercare_late(self):
        assert pickup_status(5, True, False) == "late"

    def test_friday_overdue(self):
        assert pickup_status(4, False, True) == "overdue"
