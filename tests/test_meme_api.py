import pytest
import requests

BASE_URL = "http://localhost:8000"


@pytest.fixture
def create_test_meme():
    meme_data = {
        "text": "Test meme",
        "image_url": "https://example.com/test.jpg"
    }
    response = requests.post(f"{BASE_URL}/memes", json=meme_data)
    assert response.status_code == 200
    return response.json()


def test_create_meme():
    meme_data = {
        "text": "New test meme",
        "image_url": "https://example.com/new_test.jpg"
    }
    response = requests.post(f"{BASE_URL}/memes", json=meme_data)
    assert response.status_code == 200
    assert response.json()["text"] == meme_data["text"]
    assert response.json()["image_url"] == meme_data["image_url"]


def test_get_memes():
    response = requests.get(f"{BASE_URL}/memes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_meme(create_test_meme):
    meme_id = create_test_meme["id"]
    response = requests.get(f"{BASE_URL}/memes/{meme_id}")
    assert response.status_code == 200
    assert response.json()["id"] == meme_id


def test_update_meme(create_test_meme):
    meme_id = create_test_meme["id"]
    update_data = {
        "text": "Updated test meme"
    }
    response = requests.put(f"{BASE_URL}/memes/{meme_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["text"] == update_data["text"]


def test_delete_meme(create_test_meme):
    meme_id = create_test_meme["id"]
    response = requests.delete(f"{BASE_URL}/memes/{meme_id}")
    assert response.status_code == 200

    # Проверяем, что мем действительно удален
    get_response = requests.get(f"{BASE_URL}/memes/{meme_id}")
    assert get_response.status_code == 404
