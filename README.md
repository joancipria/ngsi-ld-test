1. Create and run the Orion-LD Docker image. It is necessary to have Docker and Docker Compose installed. This will set-up an Orion-LD broker with a MongoDB database. Check out `docker-compose.yaml` file for more details.
```bash
docker compose up
```

2. Create and activate a Python virtual environment:
```bash
python3 -m venv ./venv && source ./venv/bin/activate
```

3. Install all requirements
```bash
pip install -r requirements.txt
```