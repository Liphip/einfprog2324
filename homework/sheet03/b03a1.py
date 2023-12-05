# Philip Laskowicz


def days_in_month(month: int, year: int) -> int:
    """
    Calculate the number of days in the given month and year.

    Parameters
    ----------
    month : int
        The month.
    year : int
        The year.

    Returns
    -------
    int
        The number of days in the given month and year.

    Raises
    ------
    ValueError
        If the input month is not between 1 and 12.
    ValueError
        If the input year is before 46 BC.
    """
    # TODO: Is the gregorian calendar even the correct calendar to use here? - It was not specified in the task.

    # Check if the input month is valid.
    if 12 < month < 1:
        return 0
        # TODO: Clarify what the return value should be if the input month is invalid.
        #       An invalid month will have 0 days in any year.
        raise ValueError(f"Invalid month: {month}")

    # Check if the input year is valid. The Julian (and therefore Gregorian) calendar is only valid from 46 BC onwards.
    # TODO: Check if there is a way to calculate the number of days in a month for years before 46 BC.
    if year < 46:
        return 0
        # TODO: Clarify what the return value should be if the input year is invalid.
        #       An invalid year will have 0 days in any month.
        raise ValueError(
            f"Invalid year: {year}, Julian (and therefore Gregorian) calendar only valid  from 46 BC onwards."
        )

    # Check if the input year is a leap year (after 8 AD, see below).
    # A leap year is divisible by 4, except for years divisible by 100 but not by 400.
    is_leap_year_AD = (
        year >= 8 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    )

    # Special case for years 46 BC to 8 AD.
    # The Julian calendar had leap years every 3 years, not every 4 years from 45 BC to 9 BC, skipping the leap years till 8 AD. for correctness, see
    # https://www.perseus.tufts.edu/hopper/text?doc=Plin.+Nat.+18.57&fromdoc=Perseus%3Atext%3A1999.02.0137#note-link9
    # and https://scienceworld.wolfram.com/astronomy/LeapYear.html#:~:text=Leap%20years%20were%20therefore%2045,out%20of%20every%20four%20centuries)
    # and https://en.wikipedia.org/wiki/Julian_calendar#Leap_year_error
    is_leap_year_BC = -46 < year < 8 and year % 3 == 0

    # Check if the input month is February and if the input year is a leap year.
    if (is_leap_year_AD or is_leap_year_BC) and month == 2:
        return 29

    # February has 28 days in non-leap years.
    if month == 2:
        return 28

    # April, June, September, and November have 30 days.
    if month in [4, 6, 9, 11]:
        return 30

    # All other months have 31 days.
    return 31


def date_checker(day: str, month: str, year: str) -> bool:
    """
    Check if the given date is valid.

    Parameters
    ----------
    day : str
        The day.
    month : str
        The month.
    year : str
        The year.

    Returns
    -------
    bool
        True if the date is valid, False otherwise.
    """
    # If error occurs, return False.
    try:
        # Convert input to integers.
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    # Check if the input year is valid.
    if year < 1:
        return False

    # Check if the input month is valid.
    if month < 1 or month > 12:
        return False

    # Check if the input day is valid.
    if day < 1 or day > days_in_month(month, year):
        return False

    # If all checks passed, return True.
    return True


def sleep_until_xmas(day: str, month: str, year: str) -> int:
    """
    Calculate the number of days until christmas.

    Parameters
    ----------
    day : str
        The day.
    month : str
        The month.
    year : str
        The year.

    Returns
    -------
    int
        The number of days until christmas.
        Returns None if the input date is invalid.
    """
    # Ceck if the input date is valid.
    if not date_checker(day, month, year):
        return None

    # Convert input to integers.
    day = int(day)
    month = int(month)
    year = int(year)

    # Calculate the number of days until christmas.
    days_until_xmas = 0

    # If christmas has already passed this year, calculate the number of days until christmas next year.
    if month == 12 and day > 24:
        # Add the number of days until january 1st.
        days_until_xmas += 31 - day
        # Set day, month, and year to january 1st of next year.
        day = 1
        month = 1
        year += 1

    # Add the number of days until the end of the current month.
    days_until_xmas += days_in_month(month, year) - day

    # Add the number of days until december 1st.
    for i in range(month + 1, 12):
        days_until_xmas += days_in_month(i, year)

    # Add the number of days until christmas.
    days_until_xmas += 24

    # Return the number of days until christmas.
    return days_until_xmas


def main():
    # Test the function sleep_until_xmas.
    test_dates = {
        47: ("07", "11", "2023"),
        339: ("20", "01", "2024"),
        None: ("29", "02", "1999"),
    }

    for expected_result, test_date in test_dates.items():
        days_until = sleep_until_xmas(*test_date)
        if days_until != expected_result:
            raise ValueError(
                f"sleep_until_xmas({test_date}) returned {days_until}, expected {expected_result}"
            )
        print(days_until)

    # Let the user input a date.
    day = input("Please enter a day: ")
    month = input("Please enter a month: ")
    year = input("Please enter a year: ")

    # Calculate the number of days until christmas.
    sleep_until_xmas(day, month, year)

    # TODO: Clarify if the return value of 'sleep_until_xmas' really should not be printed.
    #       The task only to call the function, not to print the return value.


if __name__ == "__main__":
    main()
