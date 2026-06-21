<div align="center">

# 🧪 home-detection-lab

[![CI](https://github.com/bvlik/home-detection-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/bvlik/home-detection-lab/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**A blue-team detection lab: detection-as-code.**
Sigma rules, attack → detection scenarios mapped to MITRE ATT&CK, and a small Python detector that runs the SSH brute-force detection against sample logs — no SIEM required to demo.

![Sigma](https://img.shields.io/badge/Detections-Sigma-0A1929?style=for-the-badge)
![MITRE](https://img.shields.io/badge/Mapped-MITRE_ATT%26CK-0A1929?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-0A1929?style=for-the-badge&logo=python&logoColor=12ABDB)

</div>

---

## Idea

A small, reproducible lab to practise the **detection engineering** loop:

```
   Attack technique  ──▶  Telemetry (logs)  ──▶  Detection rule  ──▶  Alert
   (MITRE ATT&CK)         (auth.log, ...)        (Sigma)              (triage)
```

Each scenario documents the attack, the log evidence it produces, the Sigma rule that catches it, and the ATT&CK technique it maps to.

## Contents

```
detections/sigma/      detection-as-code (portable Sigma rules)
scenarios/             attack → detection walkthroughs
mitre-attack-mapping.md   coverage matrix
tools/detect.py        runnable demo detector (SSH brute force)
tools/sample_logs/     sample telemetry to run against
```

## Detections (v0)

| Sigma rule | ATT&CK | Detects |
|------------|--------|---------|
| `ssh_bruteforce.yml` | T1110.001 | Repeated failed SSH logins from one source |
| `new_local_user.yml` | T1136.001 | Creation of a new local account |
| `sudo_privilege_escalation.yml` | T1548.003 | Suspicious sudo to root |

## Run the demo (no SIEM needed)

```bash
pip install -r requirements.txt
python tools/detect.py tools/sample_logs/auth.log
```

Expected: an alert for an SSH brute-force from `203.0.113.37` (8 failures) followed by a successful login — a classic password-spray-then-in pattern.

## Deploy for real

The Sigma rules are portable: convert them to your SIEM with [`sigma-cli`](https://github.com/SigmaHQ/sigma-cli) (`sigma convert -t wazuh ...`, `-t splunk`, `-t elasticsearch`...). Point your Wazuh/Elastic agent at `/var/log/auth.log` and import the converted rules.

## Roadmap
- [ ] Wazuh single-node `docker-compose` for full pipeline
- [ ] Windows detections (Sysmon: LSASS access, new service)
- [ ] Atomic Red Team mapping for each scenario
