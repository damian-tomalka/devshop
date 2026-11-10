def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "db": "ok"}


def test_get_missing_product_returns_404(client):
    assert client.get("/api/products/999").status_code == 404


def test_post_invalid_product_returns_400(client):
    response = client.post("/api/products", json={"name": "", "price": -5})
    assert response.status_code == 400


def test_post_then_get_lists_product(client):
    response = client.post("/api/products", json={"name": "Kubek", "price": 19.99})
    assert response.status_code == 201

    names = [p["name"] for p in client.get("/api/products").get_json()]
    assert "Kubek" in names
