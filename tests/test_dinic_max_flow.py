import pytest
from src.dinic_max_flow import DinicMaxFlow

def test_simple_max_flow():
    """
    Test a simple max flow scenario
    """
    # Graph with 4 vertices
    dinic = DinicMaxFlow(4)
    
    # Add edges: (source, v1, 10), (v1, v2, 5), (v1, v3, 10), 
    # (v2, sink, 7), (v3, sink, 10)
    dinic.add_edge(0, 1, 10)  # source to v1
    dinic.add_edge(1, 2, 5)   # v1 to v2
    dinic.add_edge(1, 3, 10)  # v1 to v3
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(3, 1, 0)   # Back edge
    dinic.add_edge(2, 3, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(3, 2, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    dinic.add_edge(2, 1, 0)   # Back edge
    
    assert dinic.max_flow(0, 2) == 5

def test_max_flow_complete_graph():
    """
    Test max flow with a more complex graph
    """
    dinic = DinicMaxFlow(6)
    
    # Create a more complex graph
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(1, 4, 8)
    dinic.add_edge(2, 3, 5)
    dinic.add_edge(2, 4, 5)
    dinic.add_edge(3, 5, 6)
    dinic.add_edge(4, 5, 6)
    
    assert dinic.max_flow(0, 5) == 11

def test_no_flow_graph():
    """
    Test a graph with no possible flow
    """
    dinic = DinicMaxFlow(3)
    
    # No edges connecting source to sink
    dinic.add_edge(0, 1, 5)
    
    assert dinic.max_flow(0, 2) == 0

def test_invalid_source_sink():
    """
    Test error handling for invalid source/sink
    """
    dinic = DinicMaxFlow(4)
    
    with pytest.raises(ValueError):
        dinic.max_flow(-1, 2)  # Invalid source
    
    with pytest.raises(ValueError):
        dinic.max_flow(0, 5)   # Out of range sink
    
    with pytest.raises(ValueError):
        dinic.max_flow(1, 1)   # Source equals sink

def test_edge_case_single_vertex():
    """
    Test max flow with a single vertex graph
    """
    dinic = DinicMaxFlow(1)
    
    with pytest.raises(ValueError):
        dinic.max_flow(0, 0)  # Source equals sink

def test_multiple_parallel_edges():
    """
    Test graph with multiple parallel edges
    """
    dinic = DinicMaxFlow(3)
    
    # Multiple edges with different capacities
    dinic.add_edge(0, 1, 5)
    dinic.add_edge(0, 1, 7)  # This should add to the first edge's capacity
    dinic.add_edge(1, 2, 10)
    
    assert dinic.max_flow(0, 2) == 10