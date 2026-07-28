# Arches-PySDK

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