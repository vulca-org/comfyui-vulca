# Release policy

The ComfyUI custom node and the Vulca SDK are separate release units. Their version numbers must
not be synchronized automatically.

## Version axes

- `project.version` in `pyproject.toml` is the custom-node version. Select its SemVer change from
  the user-visible impact of changes in this repository.
- `vulca>=X.Y.Z` is the oldest supported SDK. Change it only when this repository starts using an
  SDK API that is unavailable in the current minimum.

The two values may advance at different times. A new Vulca SDK release alone is not a reason to
change the custom-node version or its minimum dependency.

## Release gate

Before publishing a custom-node version:

1. Run the full test suite against the declared minimum SDK.
2. Run the full test suite against the newest SDK allowed by the dependency.
3. Choose the custom-node SemVer bump from the node change, not from the SDK version.
4. Update the SDK minimum only when compatibility evidence requires it.
5. Publish a custom-node tag matching `project.version` only after both compatibility checks pass.

GitHub Actions enforces the minimum-SDK check and tests the newest resolvable SDK on Python
3.10, 3.11, and 3.12.
