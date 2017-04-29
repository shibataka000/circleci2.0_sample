# coding: utf-8

import github


def test_get_user():
    user_info = github.get_user("shibataka000")
    assert user_info["login"] == "shibataka000"
