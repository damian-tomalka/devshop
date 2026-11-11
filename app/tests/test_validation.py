from devshop.validation import validate_product


def test_validate_product():
    assert validate_product({"name": "Kubek", "price": 19.99}) == []
    assert "cena nie może być ujemna" in validate_product(
        {"name": "Kubek", "price": -1}
    )
    assert "brak nazwy" in validate_product({"name": " ", "price": 5})
