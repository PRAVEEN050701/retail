from app.app import payment, product


def test_payment():
    actual = payment()
    expected = "Payment successful"

    assert actual == expected


def test_product():
    actual = product()
    expected = "Retail product"

    assert actual == expected