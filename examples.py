"""Example usage of obsd iOS detection and version utilities."""

from obsd import IOSDetector, IOSVersion


def main():
    """Demonstrate iOS detection and version handling functionality."""
    
    print("=" * 60)
    print("iOS Detection Examples")
    print("=" * 60)
    
    # Example user agents
    user_agents = [
        ("iPhone 15", "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"),
        ("iPad", "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"),
        ("iPod touch", "Mozilla/5.0 (iPod touch; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15"),
        ("Chrome on iOS", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1"),
        ("Android", "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"),
    ]
    
    detector = IOSDetector()
    
    for name, ua in user_agents:
        print(f"\n{name}:")
        print(f"  User Agent: {ua[:80]}...")
        
        info = detector.parse_user_agent(ua)
        print(f"  Is iOS: {info['is_ios']}")
        print(f"  Device Type: {info['device_type']}")
        print(f"  iOS Version: {info['ios_version']}")
        print(f"  Is Safari: {detector.is_safari(ua)}")
    
    print("\n" + "=" * 60)
    print("iOS Version Comparison Examples")
    print("=" * 60)
    
    # Version examples
    versions = [
        "13.0",
        "14.5.1",
        "15.0",
        "16.2",
        "17.0.1"
    ]
    
    print("\nCreating version objects:")
    version_objects = []
    for v in versions:
        version_obj = IOSVersion(v)
        version_objects.append(version_obj)
        print(f"  iOS {v} -> {version_obj}")
    
    print("\nVersion comparisons:")
    ios14 = IOSVersion("14.5.1")
    ios15 = IOSVersion("15.0")
    ios16 = IOSVersion("16.2")
    
    print(f"  iOS 14.5.1 < iOS 15.0: {ios14 < ios15}")
    print(f"  iOS 15.0 < iOS 16.2: {ios15 < ios16}")
    print(f"  iOS 16.2 >= iOS 15.0: {ios16 >= ios15}")
    print(f"  iOS 15.0 == iOS 15.0.0: {ios15 == IOSVersion('15.0.0')}")
    
    print("\nFeature support checking:")
    current_version = IOSVersion("15.0")
    features = [
        ("Dark Mode", "13.0"),
        ("Widgets", "14.0"),
        ("SharePlay", "15.1"),
        ("Lock Screen Widgets", "16.0"),
    ]
    
    for feature_name, min_version in features:
        supported = current_version.supports_feature(min_version)
        status = "✓ Supported" if supported else "✗ Not supported"
        print(f"  {feature_name} (requires iOS {min_version}): {status}")
    
    print("\nVersion support checking:")
    test_versions = ["11.0", "12.0", "13.0", "15.0"]
    for v in test_versions:
        version = IOSVersion(v)
        supported = version.is_supported()  # Default minimum is iOS 12.0
        status = "✓ Supported" if supported else "✗ Not supported"
        print(f"  iOS {v}: {status}")
    
    print("\nSorting versions:")
    unsorted = [IOSVersion("15.0"), IOSVersion("13.0"), IOSVersion("16.0"), IOSVersion("14.5")]
    sorted_versions = sorted(unsorted)
    print(f"  Original: {[str(v) for v in unsorted]}")
    print(f"  Sorted: {[str(v) for v in sorted_versions]}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
