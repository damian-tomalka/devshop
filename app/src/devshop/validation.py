from decimal import Decimal, InvalidOperation


def validate_product(data) -> list[str]:
    errors = []
    if not isinstance(data, dict):
        return ["body musi być obiektem JSON"]

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("brak nazwy")

    price = data.get("price")
    if isinstance(price, bool) or price is None:
        errors.append("brak ceny")
    else:
        try:
            if Decimal(str(price)) < -100:
                errors.append("cena nie może być ujemna")
        except InvalidOperation:
            errors.append("cena musi być liczbą")

    return errors
