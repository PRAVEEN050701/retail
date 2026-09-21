from app.app import payment


def test_payment():
    actual = payment()
    expected = "Payment successful"

    assert actual == expected