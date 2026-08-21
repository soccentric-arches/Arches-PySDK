# Arches-PySDK

## Project Summary

Arches-PySDK is the Python client library for the Arches HAL service.

The distributable package lives in `arches-sdk/` and exposes a typed, Pythonic interface over the protobuf and gRPC contracts generated from the HAL modules. Its runtime types cover common HAL values and service data plus module families such as CPU, GPIO, camera, CAN, Ethernet, storage, power, thermal, serial, USB, vision, and watchdog controls.

Generated protobuf Python modules and type stubs are checked into the package, and `py.typed` advertises typing support to downstream users.

The SDK supports connection setup and discovery, one-shot calls, long-running runs, monitoring, event handling, and deprecation compatibility. Examples include `examples/05_long_running_test.py`.

The package metadata, changelog, release notes, and generation tools document the distribution boundary and the relationship between generated protocol files and handwritten type wrappers. A fake server in the test suite provides a local boundary for client behavior without requiring a target board.

Tests cover connecting, discovery, one-shot and long-running flows, monitoring, events, deprecation shims, and type round trips.

This is meaningful client-contract coverage, but it does not prove interoperability with every deployed Arches-Client version or every hardware adapter. Proto regeneration and packaging should be treated as release activities.

The feature statuses below are based on source and tests visible in this repository; every manual column remains deliberately unverified.

The SDK depends on compatible generated descriptors, Python version constraints, and server behavior.

Review timeout and retry semantics, generated-file freshness, wheel contents, and interoperability with the deployed client before release.

No manual verification is implied by fake-server tests.

## Features

| # | Name / Description | Implemented? | Test Coverage? | Manual Test |
|---:|---|---|---|---|
| 1 | Typed Python package and `py.typed` marker | Implemented | Package tests | [ ] Manual verification required |
| 2 | Generated protobuf and gRPC bindings | Implemented | Round-trip tests | [ ] Manual verification required |
| 3 | HAL connection and service discovery | Implemented | `test_connect.py`, `test_discovery.py` | [ ] Manual verification required |
| 4 | One-shot invocation | Implemented | `test_oneshot.py` | [ ] Manual verification required |
| 5 | Long-running execution | Implemented | `test_long_running.py` | [ ] Manual verification required |
| 6 | Monitoring and event delivery | Implemented | `test_monitor.py`, `test_event.py` | [ ] Manual verification required |
| 7 | Module-specific typed wrappers | Implemented | `test_types_roundtrip.py` | [ ] Manual verification required |
| 8 | Fake-server integration boundary | Implemented | `tests/fakes/fake_server.py` | [ ] Manual verification required |
| 9 | Deprecation compatibility shim | Implemented | `test_deprecation_shim.py` | [ ] Manual verification required |
| 10 | Proto/type generation and release packaging | Partial | Tooling exists; release run not verified | [ ] Manual verification required |

## Validation Commands

Run the package test command defined by `arches-sdk/pyproject.toml`; generation tools are under `arches-sdk/tools/`.

## Existing Documentation

Python SDK leaf for the **Arches** project (NVIDIA Jetson + STM32) in the
SiliconCentric `project-managers` fleet.

This leaf provides `arches-sdk`, a Pythonic gRPC client for the `HalService`
endpoint exposed by `Arches-Client`. The SDK distribution package is
**`arches-sdk`** (import name `arches_sdk`); a `acadia_sdk` deprecation shim
re-exports the public surface for callers still on the old name.

The SDK source, tooling, docs, examples, and test suite live under
[`arches-sdk/`](arches-sdk/). See [`arches-sdk/README.md`](arches-sdk/README.md)
for the full API, quickstart, and `make` targets (`setup`, `gen`, `check`,
`build`).

---
Part of the `Arches` project in the `project-managers` fleet. See
`docs/project-managers.md` for the full 9-project / 8-leaf hierarchy and
shared conventions.