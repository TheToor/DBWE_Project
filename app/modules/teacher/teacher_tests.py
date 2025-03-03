import unittest
import json

from app.modules.teacher.controller import TeacherController


def test_index():
    teacher_controller = TeacherController()
    result = teacher_controller.index()
    assert result == {'message': 'Hello, World!'}
