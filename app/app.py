VERSION = "4.2.1"


def payment():
    return "Payment successful"


def product():
    return "Retail product"

def stock():
    return "In stock"


print(payment())
if __name__ == "__main__":
    print(f"Retail application - Version {VERSION}")
    print(payment())
