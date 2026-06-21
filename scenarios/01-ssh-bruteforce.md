# Scenario 01 — SSH Brute Force → Detection

**ATT&CK:** [T1110.001 — Brute Force: Password Guessing](https://attack.mitre.org/techniques/T1110/001/)

## Attack

From an attacker host, hammer the SSH service with a wordlist:

```bash
hydra -l admin -P rockyou.txt ssh://victim-vm
```

> Run only against your **own lab VM**. Never against systems you don't own.

## Telemetry produced

`/var/log/auth.log` fills with repeated failures from the attacker IP:

```
sshd[1234]: Failed password for invalid user admin from 203.0.113.37 port 51514 ssh2
... (x8) ...
sshd[1240]: Accepted password for admin from 203.0.113.37 port 51599 ssh2
```

## Detection

- **Sigma:** [`ssh_bruteforce.yml`](../detections/sigma/ssh_bruteforce.yml) — `count() by src_ip > 5` within 5 min.
- **Demo it locally:** `python tools/detect.py tools/sample_logs/auth.log`

## Why it matters

The dangerous pattern is *failures followed by a success from the same IP* — the brute force worked. That transition is the high-fidelity alert worth paging on.

## Hardening

- Disable password auth (`PasswordAuthentication no`), use keys
- `fail2ban` / rate limiting
- Restrict SSH exposure (VPN/bastion, allowlist)
