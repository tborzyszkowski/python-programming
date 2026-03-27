class LoggerMixin:
    pass


class TimestampMixin:
    pass


class Event(LoggerMixin, TimestampMixin):
    @classmethod
    def source(cls) -> str:
        return cls.mro()[1].__name__
