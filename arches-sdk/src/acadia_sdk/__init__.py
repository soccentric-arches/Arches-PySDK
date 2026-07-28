"""Deprecated compatibility shim for the renamed :mod:`arches_sdk` package.

The SDK was renamed from ``acadia-sdk`` (import ``acadia_sdk``) to
``arches-sdk`` (import ``arches_sdk``). Importing ``acadia_sdk`` now emits a
:class:`DeprecationWarning` and re-exports the public surface of
:mod:`arches_sdk` so existing callers keep working while they migrate.

New code should ``import arches_sdk`` instead.
"""
from __future__ import annotations

import warnings as _warnings

_warnings.warn(
    "The 'acadia_sdk' package has been renamed to 'arches_sdk'. "
    "Please update your imports to use 'arches_sdk'; 'acadia_sdk' will be "
    "removed in a future release.",
    DeprecationWarning,
    stacklevel=2,
)

from arches_sdk import (  # noqa: F401,E402
    ConfigError,
    ConnectionError,
    Device,
    IVVError,
    LongRunningSession,
    NotSupported,
    Peripheral,
    PeripheralNotFound,
    TestError,
    TimeoutError,
    __contracts_version__,
    __version__,
    connect,
    metric_value,
)
from arches_sdk import __all__ as _arches_all

# Mirror arches_sdk's public surface so `acadia_sdk.__all__` matches and
# `from acadia_sdk import *` re-exports the same names.
__all__ = list(_arches_all)