import pytest
import logging
import io
from src.font_logger import FontLogger

class TestFontLogger:
    def test_logger_initialization(self):
        """Test logger can be initialized"""
        logger = FontLogger()
        assert logger is not None
    
    def test_predefined_size_options(self):
        """Test predefined size options"""
        logger = FontLogger()
        
        # Test valid predefined sizes
        test_cases = [
            ('small', '<font size="2">Test message</font>'),
            ('medium', '<font size="3">Test message</font>'),
            ('large', '<font size="4">Test message</font>'),
            ('xlarge', '<font size="5">Test message</font>')
        ]
        
        for size, expected_format in test_cases:
            # Capture the log message
            captured = self._capture_log(logger, 'Test message', size=size)
            assert expected_format in captured
    
    def test_integer_size_options(self):
        """Test integer size options"""
        logger = FontLogger()
        
        # Test valid integer sizes
        for size in range(1, 8):
            captured = self._capture_log(logger, 'Test message', size=size)
            assert f'<font size="{size}">Test message</font>' in captured
    
    def test_invalid_size_options(self):
        """Test invalid size raises appropriate exceptions"""
        logger = FontLogger()
        
        # Test invalid string size
        with pytest.raises(ValueError, match="Invalid size option"):
            logger.log('Test message', size='invalid')
        
        # Test invalid integer size
        with pytest.raises(ValueError, match="Integer size must be between 1 and 7"):
            logger.log('Test message', size=0)
        with pytest.raises(ValueError, match="Integer size must be between 1 and 7"):
            logger.log('Test message', size=8)
        
        # Test invalid type
        with pytest.raises(TypeError, match="Size must be a string or integer"):
            logger.log('Test message', size=None)
    
    def _capture_log(self, logger, message, **kwargs):
        """
        Capture log messages for testing.
        Returns a string containing the captured log.
        """
        # Create a string buffer to capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        
        # Get the root logger and add our capture handler
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)
        
        try:
            # Call the log method
            logger.log(message, **kwargs)
            
            # Return the captured log
            return log_capture.getvalue()
        finally:
            # Remove the handler
            root_logger.removeHandler(handler)
            handler.close()