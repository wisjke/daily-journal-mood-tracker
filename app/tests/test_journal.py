def test_create_journal_entry(client, auth_headers):
    response = client.post("/journal", json={
        "title": "My Day",
        "content": "Today was a productive day."
    }, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["title"] == "My Day"


def test_get_journal_entries(client, auth_headers):
    response = client.get("/journal", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
