# Video Generation API

A FastAPI backend implementation of the Video Generation API contract.

## Features

- POST `/api/generate`
- GET `/api/jobs/{job_id}`
- GET `/api/generate/signed-upload-url`
- POST `/api/webhook/job_complete`
- In-memory job storage
- Background task simulation (`queued → running → completed`)
- Global error handling
- API integration tests using `pytest` and FastAPI `TestClient`

---

## Requirements

- Python 3.10+
- pip

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ossous-Dev-coder/video-generation-api.git
cd video-generation-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Run the Tests

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

---

## Project Structure

```
video-generation-api/
│
├── app/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── models/
│   ├── enums/
│   ├── exceptions/
│   └── main.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Notes

- Authentication is intentionally omitted as required by the assignment.
- Jobs are stored in memory (no database).
- Signed upload URLs are mocked (no real AWS S3 integration).
- The video generation lifecycle is simulated using FastAPI Background Tasks.