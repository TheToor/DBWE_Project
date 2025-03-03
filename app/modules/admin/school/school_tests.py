import unittest
import json

from app.modules.admin.school.controller import SchoolController


def test_index():
    school_controller = SchoolController()
    result = school_controller.index()
    assert result == {'message': 'Hello, World!'}
