# Arches-PySDK Build and Deployment

## 1. Purpose and scope

Arches-PySDK packages the Python SDK in `arches-sdk/`, including generated protocol and dataclass bindings. The top-level Makefile uses `uv` for reproducible virtualenv and editable-development workflows.

## 2. Prerequisites

Install Python 3, `make`, and `uv`. The SDK's `pyproject.toml` declares runtime and development dependencies, including pytest, coverage, Ruff, and mypy. Protocol regeneration also requires the referenced Arches-HAL protocol inputs and any generators declared by the SDK tooling.

## 3. Setup

Run `make setup` to create `.venv` and install `arches-sdk[dev]` in editable mode. `make venv` creates only the virtualenv. `make help` prints the target index.

## 4. Build and compile

- `make gen` regenerates protocol and dataclass bindings with `tools/gen_proto.py` and `tools/gen_types.py`.
- `make gen-check` regenerates into a comparison path and fails when committed stubs are stale.
- `make gen-clean` removes generated stubs and performs a full regeneration.
- `make build` installs the Python `build` module through uv and writes wheel and sdist artifacts to `arches-sdk/dist`.

Generated files are source artifacts and should be reviewed according to the repository's normal change policy.

## 5. Test and lint

- `make test` runs pytest with coverage and a terminal-missing report.
- `make lint` runs Ruff over `arches-sdk/src/arches_sdk`.
- `make typecheck` runs mypy strict using `arches-sdk/pyproject.toml`.
- `make check` runs lint, typecheck, and test.

## 6. Packaging and artifacts

The distributable wheel and source archive are under `arches-sdk/dist`. Editable development installation uses `.venv`; caches and egg metadata remain inside the SDK tree until cleaned.

## 7. Deployment, install, and run

Install a built wheel with an external consumer's Python environment, for example `uv pip install arches-sdk/dist/<artifact>.whl`; this is an installation example rather than a Make target. The SDK connects to a running HAL service, documented with the default gRPC port `50052`; board address and service configuration must be supplied by the consuming application. There is no cloud deploy, container deploy, or target flashing target in this Makefile.

`make shell` opens a uv-activated subshell for local SDK use. Credentials, target addresses, and hardware access are conditional on the consuming integration.

## 8. Cleanup

`make clean` removes SDK build/dist/egg-info outputs, test/type/lint caches, coverage data, and Python cache directories while keeping `.venv`. `make distclean` also removes the uv virtualenv and stamp directory.

## 9. Hardware, cloud, and manual verification caveats

Unit tests and type checks do not prove compatibility with a live HAL service or board. Perform a manual gRPC connection and representative API call against a compatible Arches-HAL target, checking port/configuration and protocol version. Cloud deployment is not defined.
