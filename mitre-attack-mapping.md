# MITRE ATT&CK Coverage Matrix

| Tactic | Technique | ID | Detection | Status |
|--------|-----------|----|-----------|--------|
| Credential Access | Brute Force: Password Guessing | T1110.001 | `ssh_bruteforce.yml` | ✅ |
| Persistence | Create Account: Local Account | T1136.001 | `new_local_user.yml` | ✅ |
| Privilege Escalation | Sudo and Sudo Caching | T1548.003 | `sudo_privilege_escalation.yml` | ✅ |
| Credential Access | OS Credential Dumping: LSASS | T1003.001 | Sysmon EID 10 (Windows) | 🔜 |
| Persistence | Create or Modify System Process: Service | T1543.003 | Sysmon EID 12/13 | 🔜 |

Legend: ✅ implemented · 🔜 on the roadmap

> Coverage is intentionally honest — a small set of high-fidelity detections beats a wall of noisy rules.
