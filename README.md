# devshop
Projekt zaliczeniowy DevOps, WSZiB 2026/27 (grupa 1K433-PO).

Docker Compose: od etapu 2 (w trakcie).

```bash
cp .env.example .env
docker compose up -d --build
```

## Testy
```bash
pip install -r app/requirements-dev.txt
cd app && pytest
```
