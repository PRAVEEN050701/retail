from app.app import payment, product,stock


def test_payment():
    actual = payment()
    expected = "Payment successful"

    assert actual == expected


def test_product():
    actual = product()
    expected = "Retail product"
    
    
def test_stock():
    actual = stock()
    expected = "In stock"

    assert actual == expected

    