import unittest
import json

from app.modules.login.controller import LoginController


def test_index():
    login_controller = LoginController()
    result = login_controller.index()
    assert result == {'message': 'Hello, World!'}
