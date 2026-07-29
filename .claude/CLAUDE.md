# CLAUDE.md - Arches-PySDK

Remote: git@github.com:SiliconCentric/Arches-PySDK.git
Parent project: Arches (target hardware: NVIDIA Jetson (Tegra family, L4T/JetPack OS) application processor with an STM32 real-time co-processor.)
Leaf type: <Project>-PySDK
Status: REAL - actively built out

A Python SDK leaf that consumes the HalService gRPC endpoint exposed by Arches-Client. The distribution package is arches-sdk (import name arches_sdk); a acadia_sdk deprecation shim re-exports the public surface for callers still on the old name. Source, tooling, docs, examples, and a uv-managed make workflow (setup/gen/check/build) live under arches-sdk/.

# Commands

- Setup: make setup
- Generate protos: make gen
- Check (lint + typecheck + test): make check
- Build: make build

# Notes

- PySDK regenerates protos by design (make gen, with make gen-check failing on stale stubs) - the no-regeneration rule is a C++ ODR constraint and does not apply here. Any change to hal_service.proto breaks it for real.

Part of the Arches project in the project-managers fleet. See docs/project-managers.md for the full 9-project / 8-leaf hierarchy and shared conventions.

<!-- BEGIN loop-engine -->
### Loop 20260728-pysdk-package-rename-arches (closed to in-review, try 2 of 2)

- Distribution renamed acadia-sdk -> arches-sdk; import package acadia_sdk -> arches_sdk; directory acadia-sdk/ -> arches-sdk/. A acadia_sdk deprecation shim re-exports arches_sdk (lazy PEP 562 __getattr__) and emits a DeprecationWarning at import; the shim ships in the wheel (packages.find include = ["arches_sdk*", "acadia_sdk*"]).
- Generated stubs are committed under arches-sdk/src/arches_sdk/_proto/ and arches-sdk/src/arches_sdk/types/ (~270 files). make gen-check passes. Do NOT add these to .gitignore - the workflow expects committed stubs.
- gen_proto.py now points at Arches-HAL/protos (was Acadia-HAL/protos) and adds -I<grpc_tools/_proto> for well-known protos. If the fleet ever renames HAL again, update DEFAULT_PROTOS here.
- gen_types.py uses fd.is_repeated (bool property), not fd.label == FD.LABEL_REPEATED - protobuf 7.x removed FieldDescriptor.label from the upb descriptor. Any new code comparing repeated-ness must use fd.is_repeated.
- make typecheck runs mypy --config-file arches-sdk/pyproject.toml so the project's [tool.mypy] excludes for generated _proto/types apply. Without --config-file, mypy runs from the Arches-PySDK root and reports ~153 false errors in generated modules.
- The try/except ModuleNotFoundError in arches_sdk/__init__.py tolerates a bootstrap window where stubs are missing, leaving public names unbound. The shim is lazy to match. If you ever make arches_sdk/__init__.py eager, the shim's laziness still holds - but reconsider whether the bootstrap tolerance is still needed.
- Loop artifacts: loop/execution/20260728-pysdk-package-rename-arches/try-2/ in the master repo. Success-criterion commands all PASS on this branch.
<!-- END loop-engine -->
