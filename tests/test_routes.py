def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_books(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {"title": "Ocean Book", "id": 1, "description":"watr 4evr"}, 
        {"title": "Mountain Book", "id": 2, "description": "i luv 2 climb rocks"}]

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

def test_get_one_book_with_no_record(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "book 1 not found"}

def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"

