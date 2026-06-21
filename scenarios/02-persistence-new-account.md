# Scenario 02 — Persistence via New Local Account → Detection

**ATT&CK:** [T1136.001 — Create Account: Local Account](https://attack.mitre.org/techniques/T1136/001/)

## Attack

After gaining access, the adversary creates a backdoor account and grants it sudo:

```bash
useradd -m -s /bin/bash svc-backup
usermod -aG sudo svc-backup
```

> Lab VM only.

## Telemetry produced

```
useradd[2051]: new user: name=svc-backup, UID=1002, GID=1002, home=/home/svc-backup, shell=/bin/bash
```

## Detection

- **Sigma:** [`new_local_user.yml`](../detections/sigma/new_local_user.yml) — matches `new user` in auth telemetry.
- Correlate with: account added to `sudo`/`wheel` group shortly after creation.

## Why it matters

A new account appearing outside your provisioning process is a strong persistence indicator. Alert and verify against your change records.

## Hardening

- Centralised account provisioning + alerting on out-of-band changes
- Periodic review of `sudo`/`wheel` membership (see also `saas-access-review`)
