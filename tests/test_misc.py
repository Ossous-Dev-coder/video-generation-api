from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def create_job():

    response = client.post(
        "/api/generate",
        json={
            "task_type": "reference_to_video",
            "ref_imgs": [
                "https://example.com/image.png"
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

    return response.json()["job_id"]


def test_get_signed_upload_url():

    response = client.get("/api/generate/signed-upload-url")

    assert response.status_code == 200

    body = response.json()

    assert "upload_url" in body
    assert "public_url" in body

    assert body["upload_url"].startswith("https://")
    assert body["public_url"].startswith("https://")

    assert body["expires_in_seconds"] == 3600


def test_webhook_completed():

    job_id = create_job()

    response = client.post(
        "/api/webhook/job_complete",
        headers={
            "X-Webhook-Secret": "wh_test_secret"
        },
        json={
            "job_id": job_id,
            "status": "completed",
            "task_type": "reference_to_video",
            "output_url": "https://bucket.s3.amazonaws.com/video.mp4"
        }
    )

    assert response.status_code == 200

    job = client.get(f"/api/jobs/{job_id}")

    assert job.status_code == 200

    body = job.json()

    assert body["status"] == "completed"
    assert body["progress"] == 100
    assert body["output_url"] == "https://bucket.s3.amazonaws.com/video.mp4"


def test_webhook_failed():

    job_id = create_job()

    response = client.post(
        "/api/webhook/job_complete",
        headers={
            "X-Webhook-Secret": "wh_test_secret"
        },
        json={
            "job_id": job_id,
            "status": "failed",
            "task_type": "reference_to_video",
            "error_message": "CUDA out of memory"
        }
    )

    assert response.status_code == 200

    job = client.get(f"/api/jobs/{job_id}")

    assert job.status_code == 200

    body = job.json()

    assert body["status"] == "failed"
    assert body["error_message"] == "CUDA out of memory"


def test_invalid_webhook_secret():

    response = client.post(
        "/api/webhook/job_complete",
        headers={
            "X-Webhook-Secret": "invalid_secret"
        },
        json={
            "job_id": "12345678-1234-1234-1234-123456789999",
            "status": "completed",
            "task_type": "reference_to_video",
            "output_url": "https://bucket.s3.amazonaws.com/video.mp4"
        }
    )

    assert response.status_code == 401

    body = response.json()

    assert body["error"] == "unauthorized"


def test_webhook_unknown_job():

    response = client.post(
        "/api/webhook/job_complete",
        headers={
            "X-Webhook-Secret": "wh_test_secret"
        },
        json={
            "job_id": "12345678-1234-1234-1234-123456789999",
            "status": "completed",
            "task_type": "reference_to_video",
            "output_url": "https://bucket.s3.amazonaws.com/video.mp4"
        }
    )

    assert response.status_code == 404

    body = response.json()

    assert body["error"] == "not_found"