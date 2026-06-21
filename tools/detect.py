"""Minimal SSH brute-force detector — demonstrates the ssh_bruteforce.yml Sigma logic.

Usage:
    python tools/detect.py tools/sample_logs/auth.log [--threshold 5]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict

from rich.console import Console

FAILED_RE = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")
ACCEPTED_RE = re.compile(r"Accepted \w+ for (\S+) from (\d+\.\d+\.\d+\.\d+)")


def analyse(path: str, threshold: int) -> int:
    console = Console()
    failures: dict[str, int] = defaultdict(int)
    success_after_failures: list[tuple[str, str]] = []

    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if m := FAILED_RE.search(line):
                failures[m.group(2)] += 1
            elif m := ACCEPTED_RE.search(line):
                user, ip = m.group(1), m.group(2)
                if failures.get(ip, 0) >= threshold:
                    success_after_failures.append((ip, user))

    alerts = 0
    for ip, count in sorted(failures.items(), key=lambda kv: kv[1], reverse=True):
        if count >= threshold:
            alerts += 1
            console.print(
                f"[bold red]ALERT[/] T1110.001 brute force: "
                f"[bold]{count}[/] failed SSH logins from [bold]{ip}[/]"
            )

    for ip, user in success_after_failures:
        console.print(
            f"[bold white on red]CRITICAL[/] successful login as "
            f"[bold]{user}[/] from [bold]{ip}[/] AFTER brute force — likely compromise"
        )

    if alerts == 0:
        console.print("[bold green]No brute-force pattern detected.[/]")
    return 1 if alerts else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SSH brute-force detector (Sigma demo)")
    parser.add_argument("logfile")
    parser.add_argument("--threshold", type=int, default=5, help="failures per source IP to alert")
    args = parser.parse_args(argv)
    return analyse(args.logfile, args.threshold)


if __name__ == "__main__":
    sys.exit(main())
