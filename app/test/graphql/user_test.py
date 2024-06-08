import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import to your main FastAPI app

client = TestClient(app)

@pytest.fixture
def test_client():
    return client

def test_create_user(test_client):
    mutation = """
    mutation CreateUser($input: UserInput!) {
        createUser(input: $input) {
            id
            email
        }
    }
    """
    variables = {
        "input": {
            "email": "test@example.com",
            "password": "securepassword"
        }
    }
    response = test_client.post("/graphql", json={"query": mutation, "variables": variables})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["createUser"]["email"] == "test@example.com"

def test_update_user(test_client):
    mutation_create = """
    mutation CreateUser($input: UserInput!) {
        createUser(input: $input) {
            id
            email
        }
    }
    """
    variables_create = {
        "input": {
            "email": "test2@example.com",
            "password": "securepassword"
        }
    }
    response_create = test_client.post("/graphql", json={"query": mutation_create, "variables": variables_create})
    created_user = response_create.json()["data"]["createUser"]
    
    mutation_update = """
    mutation UpdateUser($id: String!, $input: UserInput!) {
        updateUser(id: $id, input: $input) {
            id
            email
        }
    }
    """
    variables_update = {
        "id": created_user["id"],
        "input": {
            "email": "updated@example.com",
            "password": "newsecurepassword"
        }
    }
    response_update = test_client.post("/graphql", json={"query": mutation_update, "variables": variables_update})
    assert response_update.status_code == 200
    data = response_update.json()
    assert "data" in data
    assert data["data"]["updateUser"]["email"] == "updated@example.com"

def test_delete_user(test_client):
    mutation_create = """
    mutation CreateUser($input: UserInput!) {
        createUser(input: $input) {
            id
            email
        }
    }
    """
    variables_create = {
        "input": {
            "email": "test3@example.com",
            "password": "securepassword"
        }
    }
    response_create = test_client.post("/graphql", json={"query": mutation_create, "variables": variables_create})
    created_user = response_create.json()["data"]["createUser"]
    
    mutation_delete = """
    mutation DeleteUser($id: String!) {
        deleteUser(id: $id)
    }
    """
    variables_delete = {
        "id": created_user["id"]
    }
    response_delete = test_client.post("/graphql", json={"query": mutation_delete, "variables": variables_delete})
    assert response_delete.status_code == 200
    data = response_delete.json()
    assert "data" in data
    assert data["data"]["deleteUser"] == True
