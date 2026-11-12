"""Basic e2e tests shipped by the template.

OBS opens and is drivable through the accessibility tree. These are
kept deliberately generic. This repository ships no OBS module — it
provides the NDI runtime to other snaps — so the template's
module-loaded check does not apply here. Plugins extend the suite in
this directory with tests for their own UI surface.
"""

from __future__ import annotations

from conftest import WAIT_SECONDS

#: The OBS version string shown in the About dialog, e.g. "OBS 32.0.3".
OBS_VERSION_RE = r"OBS \d+\."


def test_obs_is_on_the_accessibility_bus(obs, e2e) -> None:
    """The accessibility bus must see OBS for any UI driving to work."""
    apps = e2e("atspi", "apps")
    assert "obs" in apps.stdout.split()


def test_about_dialog_shows_the_obs_version(obs, e2e) -> None:
    """Input (menu click) and dialog rendering both work."""
    e2e("atspi", "click", "menu item", "About", "--wait", WAIT_SECONDS)
    matched = e2e(
        "atspi", "assert", OBS_VERSION_RE, "--wait", WAIT_SECONDS, check=False
    )
    assert matched.returncode == 0, matched.stderr or "OBS version not found"
