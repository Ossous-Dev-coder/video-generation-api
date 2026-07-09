from fastapi.testclient import TestClient
import time
from app.enums.job_status import JobStatus
from app.main import app



client = TestClient(app)

def create_job():
    response = client.post("/api/generate",
        json={
            "task_type": "reference_to_video",
            "ref_imgs": [
                "https://example.com/image1.png"
            ],
            "prompt": "A cat drinking coffee",
            "duration": 5,
            "resolution": "720P",
            "seed": 42,
            "num_inference_steps": 25,
            "guidance_scale": 5.0,
            "guidance_scale_img": 3.0,
            "negative_prompt": "",
            "offload": False,
            "low_vram": False
        }
    )

    return response.json()["job_id"]

def test_get_existing_job():

    job_id = create_job()

    response = client.get(f"/api/jobs/{job_id}")

    assert response.status_code == 200

    body = response.json()

    assert body["job_id"] == job_id

def test_get_unknown_job():

    response = client.get("/api/jobs/12345678-1234-1234-1234-123456789999")

    assert response.status_code == 404

    body = response.json()

    assert body["error"] == "not_found"

    # print(response.json())

def test_job_completes():

    job_id = create_job()

    time.sleep(6)

    response = client.get(f"/api/jobs/{job_id}")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == JobStatus.COMPLETED

    assert body["progress"] == 100

    assert body["output_url"] is not None




















