"""Tests for iOS version handling."""

import unittest
from obsd.ios_version import IOSVersion


class TestIOSVersion(unittest.TestCase):
    """Test cases for IOSVersion class."""
    
    def test_parse_version_full(self):
        """Test parsing full version string."""
        version = IOSVersion("15.2.1")
        self.assertEqual(version.major, 15)
        self.assertEqual(version.minor, 2)
        self.assertEqual(version.patch, 1)
    
    def test_parse_version_major_minor(self):
        """Test parsing major.minor version string."""
        version = IOSVersion("14.5")
        self.assertEqual(version.major, 14)
        self.assertEqual(version.minor, 5)
        self.assertEqual(version.patch, 0)
    
    def test_parse_version_major_only(self):
        """Test parsing major version only."""
        version = IOSVersion("16")
        self.assertEqual(version.major, 16)
        self.assertEqual(version.minor, 0)
        self.assertEqual(version.patch, 0)
    
    def test_parse_version_with_underscore(self):
        """Test parsing version with underscore separators."""
        version = IOSVersion("15_0_1")
        self.assertEqual(version.major, 15)
        self.assertEqual(version.minor, 0)
        self.assertEqual(version.patch, 1)
    
    def test_parse_version_empty_raises_error(self):
        """Test that empty version string raises ValueError."""
        with self.assertRaises(ValueError):
            IOSVersion("")
    
    def test_parse_version_invalid_raises_error(self):
        """Test that invalid version string raises ValueError."""
        with self.assertRaises(ValueError):
            IOSVersion("invalid")
    
    def test_str_representation(self):
        """Test string representation of version."""
        version = IOSVersion("15.2.1")
        self.assertEqual(str(version), "15.2.1")
    
    def test_repr_representation(self):
        """Test repr representation of version."""
        version = IOSVersion("15.2.1")
        self.assertEqual(repr(version), "IOSVersion('15.2.1')")
    
    def test_equality(self):
        """Test version equality comparison."""
        v1 = IOSVersion("15.0.1")
        v2 = IOSVersion("15.0.1")
        v3 = IOSVersion("15.0.2")
        
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)
    
    def test_less_than(self):
        """Test less than comparison."""
        v1 = IOSVersion("14.0")
        v2 = IOSVersion("15.0")
        v3 = IOSVersion("15.1")
        
        self.assertTrue(v1 < v2)
        self.assertTrue(v2 < v3)
        self.assertFalse(v2 < v1)
    
    def test_less_than_or_equal(self):
        """Test less than or equal comparison."""
        v1 = IOSVersion("14.0")
        v2 = IOSVersion("15.0")
        v3 = IOSVersion("15.0")
        
        self.assertTrue(v1 <= v2)
        self.assertTrue(v2 <= v3)
        self.assertFalse(v2 <= v1)
    
    def test_greater_than(self):
        """Test greater than comparison."""
        v1 = IOSVersion("15.0")
        v2 = IOSVersion("14.0")
        v3 = IOSVersion("15.1")
        
        self.assertTrue(v1 > v2)
        self.assertTrue(v3 > v1)
        self.assertFalse(v2 > v1)
    
    def test_greater_than_or_equal(self):
        """Test greater than or equal comparison."""
        v1 = IOSVersion("15.0")
        v2 = IOSVersion("14.0")
        v3 = IOSVersion("15.0")
        
        self.assertTrue(v1 >= v2)
        self.assertTrue(v1 >= v3)
        self.assertFalse(v2 >= v1)
    
    def test_hash(self):
        """Test that versions can be hashed."""
        v1 = IOSVersion("15.0.1")
        v2 = IOSVersion("15.0.1")
        v3 = IOSVersion("15.0.2")
        
        # Equal versions should have the same hash
        self.assertEqual(hash(v1), hash(v2))
        
        # Can be used in sets
        version_set = {v1, v2, v3}
        self.assertEqual(len(version_set), 2)
    
    def test_short_version(self):
        """Test short version property."""
        version = IOSVersion("15.2.1")
        self.assertEqual(version.short_version, "15.2")
    
    def test_is_supported_default(self):
        """Test is_supported with default minimum version."""
        v1 = IOSVersion("15.0")
        v2 = IOSVersion("11.0")
        
        self.assertTrue(v1.is_supported())
        self.assertFalse(v2.is_supported())
    
    def test_is_supported_custom_minimum(self):
        """Test is_supported with custom minimum version."""
        v1 = IOSVersion("15.0")
        v2 = IOSVersion("14.0")
        minimum = IOSVersion("14.5")
        
        self.assertTrue(v1.is_supported(minimum))
        self.assertFalse(v2.is_supported(minimum))
    
    def test_supports_feature(self):
        """Test feature support checking."""
        version = IOSVersion("15.0")
        
        self.assertTrue(version.supports_feature("14.0"))
        self.assertTrue(version.supports_feature("15.0"))
        self.assertFalse(version.supports_feature("16.0"))
    
    def test_version_comparison_with_different_lengths(self):
        """Test comparing versions with different component lengths."""
        v1 = IOSVersion("15.0")
        v2 = IOSVersion("15.0.0")
        v3 = IOSVersion("15.0.1")
        
        self.assertEqual(v1, v2)
        self.assertLess(v1, v3)
    
    def test_sorting(self):
        """Test that versions can be sorted."""
        versions = [
            IOSVersion("15.0"),
            IOSVersion("13.0"),
            IOSVersion("16.0"),
            IOSVersion("14.5.1"),
            IOSVersion("14.5")
        ]
        
        sorted_versions = sorted(versions)
        
        self.assertEqual(str(sorted_versions[0]), "13.0.0")
        self.assertEqual(str(sorted_versions[1]), "14.5.0")
        self.assertEqual(str(sorted_versions[2]), "14.5.1")
        self.assertEqual(str(sorted_versions[3]), "15.0.0")
        self.assertEqual(str(sorted_versions[4]), "16.0.0")


if __name__ == '__main__':
    unittest.main()
