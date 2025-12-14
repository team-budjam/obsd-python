"""iOS device detection from user agents and other sources."""

import re
from typing import Optional, Dict, Any


class IOSDetector:
    """Detect iOS devices from user agent strings and provide device information."""
    
    # iOS user agent patterns
    IOS_PATTERN = re.compile(r'(?:iPhone|iPad|iPod)(?:.*?)(?:OS |; )?(\d+)[_.](\d+)(?:[_.](\d+))?')
    
    @staticmethod
    def is_ios(user_agent: str) -> bool:
        """
        Check if the user agent string is from an iOS device.
        
        Args:
            user_agent: The user agent string to check
            
        Returns:
            True if the user agent is from an iOS device, False otherwise
        """
        if not user_agent:
            return False
        
        ios_keywords = ['iPhone', 'iPad', 'iPod']
        return any(keyword in user_agent for keyword in ios_keywords)
    
    @staticmethod
    def get_device_type(user_agent: str) -> Optional[str]:
        """
        Get the iOS device type from user agent.
        
        Args:
            user_agent: The user agent string to parse
            
        Returns:
            The device type (iPhone, iPad, iPod) or None if not iOS
        """
        if not user_agent:
            return None
        
        # Check iPod first as it may contain "iPhone" in the user agent
        for device_type in ['iPod', 'iPad', 'iPhone']:
            if device_type in user_agent:
                return device_type
        
        return None
    
    @staticmethod
    def get_ios_version(user_agent: str) -> Optional[str]:
        """
        Extract iOS version from user agent string.
        
        Args:
            user_agent: The user agent string to parse
            
        Returns:
            The iOS version string (e.g., "15.0.1") or None if not found
        """
        if not user_agent:
            return None
        
        match = IOSDetector.IOS_PATTERN.search(user_agent)
        if match:
            major = match.group(1)
            minor = match.group(2)
            patch = match.group(3) or '0'
            return f"{major}.{minor}.{patch}"
        
        return None
    
    @staticmethod
    def parse_user_agent(user_agent: str) -> Dict[str, Any]:
        """
        Parse user agent string and extract iOS device information.
        
        Args:
            user_agent: The user agent string to parse
            
        Returns:
            Dictionary containing device information:
            - is_ios: Whether the device is iOS
            - device_type: The type of iOS device (iPhone, iPad, iPod)
            - ios_version: The iOS version string
            - original_user_agent: The original user agent string
        """
        result = {
            'is_ios': False,
            'device_type': None,
            'ios_version': None,
            'original_user_agent': user_agent
        }
        
        if not user_agent:
            return result
        
        result['is_ios'] = IOSDetector.is_ios(user_agent)
        
        if result['is_ios']:
            result['device_type'] = IOSDetector.get_device_type(user_agent)
            result['ios_version'] = IOSDetector.get_ios_version(user_agent)
        
        return result
    
    @staticmethod
    def is_safari(user_agent: str) -> bool:
        """
        Check if the user agent is Safari browser on iOS.
        
        Args:
            user_agent: The user agent string to check
            
        Returns:
            True if Safari on iOS, False otherwise
        """
        if not user_agent or not IOSDetector.is_ios(user_agent):
            return False
        
        # Safari on iOS typically contains 'Safari' and doesn't contain Chrome indicators
        return 'Safari' in user_agent and 'CriOS' not in user_agent and 'Chrome' not in user_agent
