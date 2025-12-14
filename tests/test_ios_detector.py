"""Tests for iOS detector functionality."""

import unittest
from obsd.ios_detector import IOSDetector


class TestIOSDetector(unittest.TestCase):
    """Test cases for IOSDetector class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Sample user agents
        self.iphone_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        self.ipad_ua = "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
        self.ipod_ua = "Mozilla/5.0 (iPod touch; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15"
        self.android_ua = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        self.chrome_ios_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1"
    
    def test_is_ios_with_iphone(self):
        """Test iOS detection with iPhone user agent."""
        self.assertTrue(IOSDetector.is_ios(self.iphone_ua))
    
    def test_is_ios_with_ipad(self):
        """Test iOS detection with iPad user agent."""
        self.assertTrue(IOSDetector.is_ios(self.ipad_ua))
    
    def test_is_ios_with_ipod(self):
        """Test iOS detection with iPod user agent."""
        self.assertTrue(IOSDetector.is_ios(self.ipod_ua))
    
    def test_is_ios_with_android(self):
        """Test iOS detection with Android user agent."""
        self.assertFalse(IOSDetector.is_ios(self.android_ua))
    
    def test_is_ios_with_empty_string(self):
        """Test iOS detection with empty string."""
        self.assertFalse(IOSDetector.is_ios(""))
    
    def test_is_ios_with_none(self):
        """Test iOS detection with None."""
        self.assertFalse(IOSDetector.is_ios(None))
    
    def test_get_device_type_iphone(self):
        """Test device type detection for iPhone."""
        self.assertEqual(IOSDetector.get_device_type(self.iphone_ua), "iPhone")
    
    def test_get_device_type_ipad(self):
        """Test device type detection for iPad."""
        self.assertEqual(IOSDetector.get_device_type(self.ipad_ua), "iPad")
    
    def test_get_device_type_ipod(self):
        """Test device type detection for iPod."""
        self.assertEqual(IOSDetector.get_device_type(self.ipod_ua), "iPod")
    
    def test_get_device_type_android(self):
        """Test device type detection for non-iOS device."""
        self.assertIsNone(IOSDetector.get_device_type(self.android_ua))
    
    def test_get_device_type_empty(self):
        """Test device type detection with empty string."""
        self.assertIsNone(IOSDetector.get_device_type(""))
    
    def test_get_ios_version_iphone(self):
        """Test iOS version extraction from iPhone user agent."""
        version = IOSDetector.get_ios_version(self.iphone_ua)
        self.assertEqual(version, "15.0.0")
    
    def test_get_ios_version_ipad(self):
        """Test iOS version extraction from iPad user agent."""
        version = IOSDetector.get_ios_version(self.ipad_ua)
        self.assertEqual(version, "14.7.1")
    
    def test_get_ios_version_ipod(self):
        """Test iOS version extraction from iPod user agent."""
        version = IOSDetector.get_ios_version(self.ipod_ua)
        self.assertEqual(version, "13.3.0")
    
    def test_get_ios_version_android(self):
        """Test iOS version extraction from Android user agent."""
        self.assertIsNone(IOSDetector.get_ios_version(self.android_ua))
    
    def test_get_ios_version_empty(self):
        """Test iOS version extraction with empty string."""
        self.assertIsNone(IOSDetector.get_ios_version(""))
    
    def test_parse_user_agent_iphone(self):
        """Test full user agent parsing for iPhone."""
        result = IOSDetector.parse_user_agent(self.iphone_ua)
        
        self.assertTrue(result['is_ios'])
        self.assertEqual(result['device_type'], 'iPhone')
        self.assertEqual(result['ios_version'], '15.0.0')
        self.assertEqual(result['original_user_agent'], self.iphone_ua)
    
    def test_parse_user_agent_android(self):
        """Test full user agent parsing for Android."""
        result = IOSDetector.parse_user_agent(self.android_ua)
        
        self.assertFalse(result['is_ios'])
        self.assertIsNone(result['device_type'])
        self.assertIsNone(result['ios_version'])
        self.assertEqual(result['original_user_agent'], self.android_ua)
    
    def test_parse_user_agent_empty(self):
        """Test full user agent parsing with empty string."""
        result = IOSDetector.parse_user_agent("")
        
        self.assertFalse(result['is_ios'])
        self.assertIsNone(result['device_type'])
        self.assertIsNone(result['ios_version'])
        self.assertEqual(result['original_user_agent'], "")
    
    def test_is_safari_with_safari(self):
        """Test Safari detection with Safari user agent."""
        self.assertTrue(IOSDetector.is_safari(self.iphone_ua))
    
    def test_is_safari_with_chrome(self):
        """Test Safari detection with Chrome on iOS."""
        self.assertFalse(IOSDetector.is_safari(self.chrome_ios_ua))
    
    def test_is_safari_with_android(self):
        """Test Safari detection with Android user agent."""
        self.assertFalse(IOSDetector.is_safari(self.android_ua))
    
    def test_is_safari_with_empty(self):
        """Test Safari detection with empty string."""
        self.assertFalse(IOSDetector.is_safari(""))


if __name__ == '__main__':
    unittest.main()
