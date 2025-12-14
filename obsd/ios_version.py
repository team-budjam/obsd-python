"""iOS version handling and comparison utilities."""

from typing import Optional, Tuple
import re


class IOSVersion:
    """Represent and compare iOS versions."""
    
    def __init__(self, version_string: str):
        """
        Initialize an iOS version object.
        
        Args:
            version_string: Version string in format "major.minor.patch" or "major.minor"
            
        Raises:
            ValueError: If version string format is invalid
        """
        self.original = version_string
        self.major, self.minor, self.patch = self._parse_version(version_string)
    
    def _parse_version(self, version_string: str) -> Tuple[int, int, int]:
        """
        Parse version string into components.
        
        Args:
            version_string: Version string to parse
            
        Returns:
            Tuple of (major, minor, patch) as integers
            
        Raises:
            ValueError: If version string format is invalid
        """
        if not version_string:
            raise ValueError("Version string cannot be empty")
        
        # Handle both dot and underscore separators
        version_string = version_string.replace('_', '.')
        
        # Extract version numbers
        match = re.match(r'^(\d+)(?:\.(\d+))?(?:\.(\d+))?', version_string)
        if not match:
            raise ValueError(f"Invalid version format: {version_string}")
        
        major = int(match.group(1))
        minor = int(match.group(2) or 0)
        patch = int(match.group(3) or 0)
        
        return major, minor, patch
    
    def __str__(self) -> str:
        """Return version as string."""
        return f"{self.major}.{self.minor}.{self.patch}"
    
    def __repr__(self) -> str:
        """Return version representation."""
        return f"IOSVersion('{self.major}.{self.minor}.{self.patch}')"
    
    def __eq__(self, other) -> bool:
        """Check if versions are equal."""
        if not isinstance(other, IOSVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)
    
    def __lt__(self, other) -> bool:
        """Check if this version is less than other."""
        if not isinstance(other, IOSVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)
    
    def __le__(self, other) -> bool:
        """Check if this version is less than or equal to other."""
        if not isinstance(other, IOSVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)
    
    def __gt__(self, other) -> bool:
        """Check if this version is greater than other."""
        if not isinstance(other, IOSVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)
    
    def __ge__(self, other) -> bool:
        """Check if this version is greater than or equal to other."""
        if not isinstance(other, IOSVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) >= (other.major, other.minor, other.patch)
    
    def __hash__(self) -> int:
        """Return hash of version."""
        return hash((self.major, self.minor, self.patch))
    
    @property
    def short_version(self) -> str:
        """Get short version string (major.minor)."""
        return f"{self.major}.{self.minor}"
    
    def is_supported(self, minimum_version: Optional['IOSVersion'] = None) -> bool:
        """
        Check if this version meets minimum requirements.
        
        Args:
            minimum_version: Minimum required iOS version (default: iOS 12.0)
            
        Returns:
            True if version is supported, False otherwise
        """
        if minimum_version is None:
            minimum_version = IOSVersion("12.0")
        
        return self >= minimum_version
    
    def supports_feature(self, feature_min_version: str) -> bool:
        """
        Check if this iOS version supports a feature.
        
        Args:
            feature_min_version: Minimum iOS version required for the feature
            
        Returns:
            True if feature is supported, False otherwise
        """
        min_version = IOSVersion(feature_min_version)
        return self >= min_version
