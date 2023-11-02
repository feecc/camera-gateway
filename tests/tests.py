from fastapi.testclient import TestClient

def get_client() -> TestClient:
    return TestClient()