import logging
from typing import Union, Literal

class FontLogger:
    """
    A custom logger that supports logging with different font sizes.
    
    Supports logging at different font sizes using HTML-like formatting.
    """
    
    def __init__(self, logger_name: str = 'font_logger'):
        """
        Initialize the FontLogger with a specific logger name.
        
        :param logger_name: Name of the logger, defaults to 'font_logger'
        """
        self.logger = logging.getLogger(logger_name)
        # Ensure the logger is configured to support HTML formatting
        self.logger.setLevel(logging.INFO)
        
    def log(self, 
            message: str, 
            size: Union[Literal['small', 'medium', 'large', 'xlarge'], int] = 'medium', 
            level: int = logging.INFO
        ) -> None:
        """
        Log a message with specified font size.
        
        :param message: The message to log
        :param size: Font size - can be 'small', 'medium', 'large', 'xlarge', or an integer
        :param level: Logging level (default is INFO)
        :raises ValueError: If an invalid size is provided
        """
        # Validate and convert size to HTML font size
        if isinstance(size, str):
            size_map = {
                'small': '2',
                'medium': '3',
                'large': '4',
                'xlarge': '5'
            }
            if size not in size_map:
                raise ValueError(f"Invalid size option. Choose from {list(size_map.keys())}")
            font_size = size_map[size]
        elif isinstance(size, int):
            if size < 1 or size > 7:
                raise ValueError("Integer size must be between 1 and 7")
            font_size = str(size)
        else:
            raise TypeError("Size must be a string or integer")
        
        # Format message with HTML font size
        formatted_message = f'<font size="{font_size}">{message}</font>'
        
        # Log the formatted message
        self.logger.log(level, formatted_message)