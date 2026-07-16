"""Validate stable ComfyUI package and manager metadata."""

from __future__ import annotations

import json
from pathlib import Path
import re

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 compatibility
    import tomli as tomllib


ROOT = Path(__file__).resolve().parent
SEMVER = re.compile(r"\d+\.\d+\.\d+")
VULCA_DEPENDENCY = re.compile(r"vulca>=(?P<minimum>\d+\.\d+\.\d+)")


def test_package_and_manager_metadata_agree() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    manager = json.loads((ROOT / "comfyui-manager-entry.json").read_text(encoding="utf-8"))

    assert project["name"] == "comfyui-vulca"
    assert SEMVER.fullmatch(project["version"])
    assert project["requires-python"] == ">=3.10"
    assert len(project["dependencies"]) == 1
    dependency = VULCA_DEPENDENCY.fullmatch(project["dependencies"][0])
    assert dependency is not None

    # The custom-node release line is independent from the Vulca SDK floor.
    assert project["version"] != dependency.group("minimum")

    repository_url = project["urls"]["Repository"]
    assert project["urls"]["Homepage"] == repository_url
    assert manager["reference"] == repository_url
    assert manager["files"] == [repository_url]
    assert manager["install_type"] == "git-clone"


def test_declared_apache_license_has_distribution_text() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")

    assert project["license"] == {"text": "Apache-2.0"}
    assert "Apache License" in license_text
    assert "Version 2.0, January 2004" in license_text
    assert "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION" in license_text
