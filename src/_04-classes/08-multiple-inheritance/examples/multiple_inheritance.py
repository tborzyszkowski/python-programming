class LoggerMixin:
    def describe(self) -> str:
        return "logger"


class TimestampMixin:
    def describe(self) -> str:
        return "timestamp"


class Event(LoggerMixin, TimestampMixin):
    @classmethod
    def describe_chain(cls) -> list[str]:
        return [c.__name__ for c in cls.mro()]
