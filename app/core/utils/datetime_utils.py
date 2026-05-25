from datetime import datetime
from zoneinfo import ZoneInfo


IST = ZoneInfo("Asia/Kolkata")


class DateTimeUtils:

    @staticmethod
    def now():
        return datetime.now(IST)

    @staticmethod
    def current_date():
        return DateTimeUtils.now().date()

    @staticmethod
    def current_time():
        return DateTimeUtils.now().time()

    @staticmethod
    def formatted_datetime():
        return DateTimeUtils.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    @staticmethod
    def formatted_date():
        return DateTimeUtils.now().strftime(
            "%d-%m-%Y"
        )

    @staticmethod
    def formatted_time():
        return DateTimeUtils.now().strftime(
            "%I:%M %p"
        )
    
    @staticmethod
    def current_hour():
        return DateTimeUtils.now().hour
    