import pytest
import lzma
from src.lzma_compression import lzma_compress, lzma_decompress

def test_compress_decompress_string():
    """Test compression and decompression of a string"""
    original_text = "Hello, this is a test of LZMA compression!"
    compressed = lzma_compress(original_text)
    
    # Verify compressed data is bytes and different from original
    assert isinstance(compressed, bytes)
    assert compressed != original_text.encode('utf-8')
    
    # Decompress and verify
    decompressed = lzma_decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_bytes = b'Binary data for compression test'
    compressed = lzma_compress(original_bytes)
    
    # Verify compressed data is bytes and different from original
    assert isinstance(compressed, bytes)
    assert compressed != original_bytes
    
    # Decompress and verify
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_bytes

def test_compression_levels():
    """Test different compression levels"""
    text = "Test compression levels with varying intensities"
    
    # Test all valid compression levels
    for level in range(10):
        compressed = lzma_compress(text, compression_level=level)
        decompressed = lzma_decompress(compressed)
        assert decompressed.decode('utf-8') == text

def test_invalid_compression_level():
    """Test that invalid compression levels raise ValueError"""
    with pytest.raises(ValueError):
        lzma_compress("Test", compression_level=-1)
    
    with pytest.raises(ValueError):
        lzma_compress("Test", compression_level=10)

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    # Test non-str/bytes input for compression
    with pytest.raises(TypeError):
        lzma_compress(123)
    
    with pytest.raises(TypeError):
        lzma_decompress("Not bytes")

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_string = ""
    empty_bytes = b''
    
    # String compression
    compressed_str = lzma_compress(empty_string)
    assert lzma_decompress(compressed_str) == empty_bytes
    
    # Bytes compression
    compressed_bytes = lzma_compress(empty_bytes)
    assert lzma_decompress(compressed_bytes) == empty_bytes

def test_large_input():
    """Test compression of a large input"""
    large_text = "A" * 100000  # 100k characters
    compressed = lzma_compress(large_text)
    
    # Verify compression reduces size
    assert len(compressed) < len(large_text.encode('utf-8'))
    
    # Verify decompression works
    decompressed = lzma_decompress(compressed)
    assert decompressed.decode('utf-8') == large_text

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(lzma.LZMAError):
        lzma_decompress(b'Invalid compressed data')