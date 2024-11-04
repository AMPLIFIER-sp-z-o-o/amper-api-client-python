class LogSeverity:
    Info = "info"
    Warning = "warning"
    Debug = "debug"
    Error = "error"


class LogEntry:
    def __init__(self):
        self.level: str = None
        self.message: str = None
