from app.app import VERSION, payment, product, stock


def test_version():
    assert VERSION == "4.2.1"


def test_payment():
    actual = payment()
    expected = "Payment successful"

    assert actual == expected


def test_product():
    actual = product()
    expected = "Retail product"

    assert actual == expected


def test_stock():
    actual = stock()
    expected = "In stock"

    assert actual == expected