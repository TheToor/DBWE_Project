import unittest
import json

from app.modules.index.controller import IndexController


def test_index():
    index_controller = IndexController()
    result = index_controller.index()
    assert result == {'message': 'Hello, World!'}
