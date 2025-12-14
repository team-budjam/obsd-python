# obsd-python

iOS device detection and utilities for Python

## Features

- **iOS Device Detection**: Detect iOS devices from user agent strings
- **Device Type Identification**: Identify iPhone, iPad, and iPod devices
- **iOS Version Parsing**: Extract and parse iOS version information
- **Version Comparison**: Compare iOS versions with rich comparison operators
- **Safari Detection**: Detect Safari browser on iOS devices

## Installation

```bash
pip install obsd-python
```

## Usage

### iOS Device Detection

```python
from obsd import IOSDetector

# Detect iOS from user agent
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
detector = IOSDetector()

# Check if device is iOS
is_ios = detector.is_ios(user_agent)  # True

# Get device type
device_type = detector.get_device_type(user_agent)  # "iPhone"

# Get iOS version
ios_version = detector.get_ios_version(user_agent)  # "15.0.0"

# Parse all information at once
info = detector.parse_user_agent(user_agent)
# {
#     'is_ios': True,
#     'device_type': 'iPhone',
#     'ios_version': '15.0.0',
#     'original_user_agent': '...'
# }

# Check if Safari browser
is_safari = detector.is_safari(user_agent)
```

### iOS Version Handling

```python
from obsd import IOSVersion

# Create version objects
ios15 = IOSVersion("15.0.1")
ios16 = IOSVersion("16.0")

# Compare versions
print(ios15 < ios16)  # True
print(ios16 >= ios15)  # True
print(ios15 == IOSVersion("15.0.1"))  # True

# Get version components
print(ios15.major)  # 15
print(ios15.minor)  # 0
print(ios15.patch)  # 1
print(ios15.short_version)  # "15.0"

# Check feature support
if ios15.supports_feature("14.0"):
    print("Feature is supported!")

# Check if version is supported (default minimum: iOS 12.0)
if ios15.is_supported():
    print("iOS version is supported")
```

## Requirements

- Python 3.7+

## License

Apache License 2.0