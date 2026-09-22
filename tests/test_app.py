from app.app import payment

from app.app import VERSION, payment


def test_version():
    assert VERSION == "4.2.1"


def test_payment():
    assert payment() == "Payment successful"