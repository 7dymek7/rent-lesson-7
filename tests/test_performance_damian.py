import time
from src.models import Apartment, Tenant, Parameters
from src.manager import Manager

def _create_n_apartments(n: int) -> dict:
    return {f"apart-{i}": Apartment(key=f"apart-{i}", name=f"Apart {i}", location=f"{i} Main St",
                                    area_m2=100.0, rooms={}) for i in range(n)}

def _create_n_tenants(n: int, apartments: dict) -> dict:
    apartment_keys = list(apartments.keys())
    tenants = {}
    for i in range(n):
        tenants[f"tenant-{i}"] = Tenant(
            name=f"Tenant {i}",
            apartment=apartment_keys[i % len(apartment_keys)],
            room="Room 1",
            rent_pln=1000.0,
            deposit_pln=1000.0,
            date_agreement_from="2020-01-01",
            date_agreement_to="2021-01-01"
        )
    return tenants

def test_large_dataset_creation_and_validation():
    N_APARTMENTS = 100_000
    N_TENANTS = 1_000_000
    MAX_CREATION_TIME_SEC = 10
    MAX_CHECK_TIME_MS = 10

    manager = Manager(Parameters())

    start_time = time.perf_counter()
    manager.apartments = _create_n_apartments(N_APARTMENTS)
    manager.tenants = _create_n_tenants(N_TENANTS, manager.apartments)
    creation_time = time.perf_counter() - start_time

    print(f"Time to create {N_APARTMENTS} apartments and {N_TENANTS} tenants: {creation_time:.3f} sec")
    assert creation_time <= MAX_CREATION_TIME_SEC, f"Data creation took too long: {creation_time:.3f} sec"

    start_time = time.perf_counter()
    result = manager.check_tenants_apartment_keys()
    check_time = (time.perf_counter() - start_time) * 1e3

    print(f"Time to check tenant-apartment keys: {check_time:.3f} ms")
    assert result == True