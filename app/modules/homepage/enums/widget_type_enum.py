from enum import Enum


class WidgetTypeEnum(str, Enum):

    BANNER = "BANNER"

    NOTICE = "NOTICE"

    QUICK_ACTION = "QUICK_ACTION"

    DASHBOARD_CARD = "DASHBOARD_CARD"

    EVENT = "EVENT"

    GALLERY = "GALLERY"

    PROMOTION = "PROMOTION"

    ANNOUNCEMENT = "ANNOUNCEMENT"