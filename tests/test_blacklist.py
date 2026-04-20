from src.manager import Manager
from src.models import Parameters

def test_blacklist_structure():
    parameters = Parameters()
    manager = Manager(parameters)
    assert hasattr(manager, "blacklist")
    assert isinstance(manager.blacklist, dict)
    for tenant_name, info in manager.blacklist.items():
        assert "name" in info
        assert "reason" in info
        assert isinstance(info["name"], str)
        assert isinstance(info["reason"], str)

def test_add_blacklisted_tenant_detected():
    parameters = Parameters()
    manager = Manager(parameters)
    blacklisted_name = "Jan Kowalski"
    manager.blacklist = {
        blacklisted_name: {"name": blacklisted_name, "reason": "Unpaid rent"}
    }
    manager.tenants = {
        "tenant-1": type("Tenant", (), {"name": blacklisted_name})(),
        "tenant-2": type("Tenant", (), {"name": "Anna Nowak"})()
    }
    assert manager.check_blacklist() is True

def test_non_blacklisted_tenants_pass():
    parameters = Parameters()
    manager = Manager(parameters)
    manager.blacklist = {
        "Jan Kowalski": {"name": "Jan Kowalski", "reason": "Unpaid rent"}
    }
    manager.tenants = {
        "tenant-1": type("Tenant", (), {"name": "Anna Nowak"})(),
        "tenant-2": type("Tenant", (), {"name": "Ewa Adamska"})()
    }
    assert manager.check_blacklist() is False

def test_empty_blacklist_all_pass():
    parameters = Parameters()
    manager = Manager(parameters)
    manager.blacklist = {}
    manager.tenants = {
        "tenant-1": type("Tenant", (), {"name": "Anna Nowak"})(),
        "tenant-2": type("Tenant", (), {"name": "Ewa Adamska"})()
    }
    assert manager.check_blacklist() is False