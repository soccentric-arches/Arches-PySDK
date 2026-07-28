# Arches-PySDK

**Remote:** `git@github.com:SiliconCentric/Arches-PySDK.git`
**Parent project:** [Arches](../Arches.md) (target hardware: **NVIDIA Jetson** (Tegra family, L4T/JetPack OS) application processor with an **STM32** real-time co-processor.)
**Leaf type:** `<Project>-PySDK`
**Status:** REAL — actively built out

A **Python SDK** leaf that consumes the `HalService` gRPC endpoint exposed by `Arches-Client`. The distribution package is **`arches-sdk`** (import name `arches_sdk`); a `acadia_sdk` deprecation shim re-exports the public surface for callers still on the old name. Source, tooling, docs, examples, and a uv-managed `make` workflow (`setup`/`gen`/`check`/`build`) live under `arches-sdk/`.

---
Part of the `Arches` project in the `project-managers` fleet. See `docs/project-managers.md` for the full 9-project / 8-leaf hierarchy and shared conventions.
