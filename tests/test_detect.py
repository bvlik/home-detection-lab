"""Tests for the SSH brute-force detector via its CLI."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DETECT = ROOT / "tools" / "detect.py"
LOGS = ROOT / "tools" / "sample_logs"


def _run(log_name: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(DETECT), str(LOGS / log_name)],
        capture_output=True,
        text=True,
    )


def test_bruteforce_is_detected():
    result = _run("auth.log")
    assert result.returncode == 1
    assert "brute force" in result.stdout.lower()


def test_clean_log_has_no_alert():
    result = _run("clean.log")
    assert result.returncode == 0
