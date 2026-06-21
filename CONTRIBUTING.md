# Contributing

Thanks for your interest! This is a blue-team detection lab — detections-as-code and documentation.

## Dev setup
```bash
pip install -r requirements.txt
pip install pytest ruff
```

## Before opening a PR
- `ruff check .` — lint
- `pytest -q` — tests
- New Sigma rules: keep them high-fidelity and map them to a MITRE ATT&CK technique.

## Conventions
- Conventional commit messages (`feat:`, `fix:`, `docs:`, `test:`)
- Update `mitre-attack-mapping.md` when you add a detection.
