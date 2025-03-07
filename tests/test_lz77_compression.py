import pytest
import sys
sys.path.append('src')

from lz77_compression import lz77_compress, lz77_decompress

def test_lz77_basic_string_compression():
    """Test basic string compression and decompression"""
    original = "AAAAABBBBBCCCCC"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_repeated_patterns():
    """Test compression of highly repetitive data"""
    original = "abcabcabcabcabcabc"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_empty_input():
    """Test compression and decompression of empty input"""
    original = ""
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_binary_data():
    """Test compression of binary data"""
    original = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_mixed_characters():
    """Test compression of mixed character types"""
    original = "Hello, World! 123 Hello, World! 123"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lz77_compress(12345)
    
    with pytest.raises(TypeError):
        lz77_decompress(12345)

def test_lz77_compression_efficiency():
    """Test that compression reduces data size for repetitive input"""
    original = "ABCDEFG" * 100
    compressed = lz77_compress(original)
    assert len(compressed) < len(original)  # Compressed should be smaller
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz77_edge_cases():
    """Test various edge cases"""
    # Single character
    original = "A"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed.decode('utf-8') == original

    # Very long string with minimal repetition
    original = "".join(chr(i % 256) for i in range(1000))
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original.encode('utf-8')