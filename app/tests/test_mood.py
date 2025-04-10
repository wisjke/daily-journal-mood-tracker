def test_log_mood(client, auth_headers):
    journal_response = client.post("/journal", json={
        "title": "My Mood Entry",
        "content": "Logged my mood."
    }, headers=auth_headers)

    assert journal_response.status_code == 201
    journal_id = journal_response.json()["id"]

    response = client.post("/mood", json={
        "mood": "happy",
        "tags": "productive,energetic",
        "journal_entry_id": journal_id
    }, headers=auth_headers)

    assert response.status_code == 201
    assert response.json()["mood"] == "happy"


def test_get_mood_logs(client, auth_headers):
    response = client.get("/mood", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
