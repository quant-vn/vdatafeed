""" Custom logging module for vDatafeed. """
import logging
import sys

logger = logging.getLogger("vDatafeed")
logger.propagate = True


import json
import contextvars

active_provider = contextvars.ContextVar("active_provider", default="")


class BeautifulFormatter(logging.Formatter):
    """
    Custom formatter matching the exact format:
    [Timestamp] [Level] [Logger/Tag] - [Message] | [Context/Metadata]
    """
    def format(self, record):
        # 1. Timestamp
        timestamp = self.formatTime(record, "%Y-%m-%d %H:%M:%S")

        # 2. Level
        level = record.levelname

        # 3. Logger/Tag
        provider = active_provider.get().upper()
        tag = f"{record.name}][{provider}" if provider else record.name

        # 4. Message
        msg = record.getMessage()

        # 5. Context/Metadata
        standard_keys = {
            'name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename',
            'module', 'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName',
            'created', 'msecs', 'relativeCreated', 'thread', 'threadName',
            'processName', 'process', 'message', 'asctime', 'taskName'
        }
        metadata = {k: v for k, v in record.__dict__.items() if k not in standard_keys}

        return f"[{timestamp}] [{level}] [{tag}] - {msg}" + (f" | {metadata}" if metadata else "")


def configure_logger(show_logs: bool = False):
    """
    Configures log output behavior.
    If show_logs is True, prints logs of level INFO and above to stdout.
    If show_logs is False, silences logs (handles only WARNING and above).
    """
    # Remove existing handlers to avoid duplicates
    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    if show_logs:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(BeautifulFormatter())
        logger.addHandler(handler)
    else:
        logger.setLevel(logging.WARNING)


import time
import functools

def log_execution_time(func):
    """ Decorator to measure and log the call -> response duration of a method. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        provider = getattr(args[0], "provider_name", "") if args else ""
        token = active_provider.set(provider)
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start_time
            logger.info(f"Response ~> {func.__name__} in {elapsed:.4f}s")
            active_provider.reset(token)
    return wrapper
