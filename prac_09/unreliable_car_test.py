from unreliable_car import UnreliableCar

# Test initialization
def test_init():
    car = UnreliableCar("Test Car", 100, 50.0)
    assert car.name == "Test Car", "Name not set correctly"
    assert car.fuel == 100, "Fuel not set correctly"
    assert car.reliability == 50.0, "Reliability not set correctly"
    print("Initialization test passed")

# Test drive method with reliability
def test_drive_reliability():
    # Create a car with 30% reliability and sufficient fuel
    car = UnreliableCar("Unreliable Prius", 1000, 30.0)
    trials = 100
    successful_drives = 0
    distance_per_attempt = 10

    # Run 100 drive attempts
    for _ in range(trials):
        distance_driven = car.drive(distance_per_attempt)
        if distance_driven > 0:
            successful_drives += 1

    # Calculate success rate and check if it's within a reasonable range (e.g., 20-40% for 30% reliability)
    success_rate = (successful_drives / trials) * 100
    assert 20 <= success_rate <= 40, f"Success rate {success_rate}% not within expected range for 30% reliability"
    print(f"Drive test: {successful_drives} successful drives out of {trials} (Success rate: {success_rate:.1f}%)")

# Run tests
if __name__ == "__main__":
    test_init()
    test_drive_reliability()
    print("All tests completed")
