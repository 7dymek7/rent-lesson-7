import pytest

class TransferManager:
    def __init__(self, min_amount, max_amount):
        self.min_amount = min_amount
        self.max_amount = max_amount

    def validate_transfer_amount(self, amount):
        if amount < self.min_amount:
            raise ValueError(f"Kwota przelewu jest za mała. Minimalna kwota to {self.min_amount}.")
        if amount > self.max_amount:
            raise ValueError(f"Kwota przelewu jest za duża. Maksymalna kwota to {self.max_amount}.")
        return True

def test_transfer_below_minimum():
    manager = TransferManager(min_amount=100, max_amount=10000)
    
    # Test: Kwota mniejsza niż minimalna (powinna rzucić wyjątek)
    with pytest.raises(ValueError, match="Kwota przelewu jest za mała. Minimalna kwota to 100."):
        manager.validate_transfer_amount(50)

def test_transfer_above_maximum():
    manager = TransferManager(min_amount=100, max_amount=10000)
    
    # Test: Kwota większa niż maksymalna (powinna rzucić wyjątek)
    with pytest.raises(ValueError, match="Kwota przelewu jest za duża. Maksymalna kwota to 10000."):
        manager.validate_transfer_amount(20000)

def test_transfer_within_range():
    manager = TransferManager(min_amount=100, max_amount=10000)
    
    # Test: Kwota w dozwolonym zakresie (powinna przejść walidację)
    assert manager.validate_transfer_amount(5000) is True

def test_transfer_with_exact_minimum():
    manager = TransferManager(min_amount=100, max_amount=10000)
    
    # Test: Kwota równa minimalnej (powinna przejść walidację)
    assert manager.validate_transfer_amount(100) is True

def test_transfer_with_exact_maximum():
    manager = TransferManager(min_amount=100, max_amount=10000)
    
    # Test: Kwota równa maksymalnej (powinna przejść walidację)
    assert manager.validate_transfer_amount(10000) is True