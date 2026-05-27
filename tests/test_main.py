"""Tests"""
from src.main import hello_world, add

def test_hello():
    assert hello_world() == "Hello, World!"

def test_add():
    assert add(2, 3) == 5
