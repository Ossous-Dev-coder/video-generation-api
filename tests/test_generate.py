from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_generate_reference_to_video():

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

    assert response.status_code == 201

    body = response.json()

    assert "job_id" in body
    assert body["status"] == "queued"
    assert body["estimated_time_seconds"] == 300

def test_generate_without_prompt():

    response = client.post(
        "/api/generate",
        json={
            "task_type": "reference_to_video",
            "ref_imgs": [
                "https://example.com/image1.png"
            ]
        }
    )

    assert response.status_code == 400

    body = response.json()

    assert body["error"] == "validation_error"

def test_invalid_task_type():

    response = client.post(
        "/api/generate",
        json={
            "task_type": "invalid_task",
            "prompt": "test"
        }
    )

    assert response.status_code == 400

def test_reference_video_requires_ref_imgs():

    response = client.post(
        "/api/generate",
        json={
            "task_type": "reference_to_video",
            "prompt": "test"
        }
    )

    assert response.status_code == 400

