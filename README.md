# App2 — Flask Simple

## Jalankan

```bash
apt update
apt install python3-pip
pip3 install -r requirements.txt --break-system-packages
python app.py
```

Buka http://localhost:5001

- `/` — halaman utama
- `/health` — health check (JSON)

Env opsional: `APP_NAME` (default `App2`), `APP_VERSION`, `PORT`.
