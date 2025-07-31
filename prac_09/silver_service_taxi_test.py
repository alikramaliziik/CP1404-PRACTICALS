from silver_service_taxi import SilverServiceTaxi

def test_init():
    """Test initialization of SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 200, 2.0)
    assert taxi.name == "Hummer", "Name not set correctly"
    assert taxi.fuel == 200, "Fuel not set correctly"
    assert abs(taxi.price_per_km - (1.23 * 2.0)) < 0.01, "Price per km not scaled correctly"
    assert taxi.flagfall == 4.50, "Flagfall not set correctly"
    print("Initialization test passed")

def test_get_fare():
    """Test fare calculation, including 18 km trip with fanciness of 2."""
    taxi = SilverServiceTaxi("Hummer", 200, 2.0)
    taxi.start_fare()  # Reset fare
    taxi.drive(18)  # Drive 18 km
    expected_fare = (1.23 * 2.0 * 18) + 4.50  # 1.23 * 2 * 18 + 4.50 = 48.78
    actual_fare = taxi.get_fare()
    assert abs(actual_fare - 48.78) < 0.01, f"Expected fare $48.78, got ${actual_fare:.2f}"
    print("Fare calculation test passed")

def test_str():
    """Test string representation includes flagfall."""
    taxi = SilverServiceTaxi("Hummer", 200, 4.0)
    expected_str = f"Hummer, fuel=200, odometer=0, 0km on current fare, ${1.23 * 4.0:.2f}/km plus flagfall of $4.50"
    assert str(taxi) == expected_str, "String representation incorrect"
    print("String representation test passed")

if __name__ == "__main__":
    test_init()
    test_get_fare()
    test_str()
    print("All tests completed")
