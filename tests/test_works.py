import pytest

from cli11 import App


def test_simple():
    app = App("hello")
    app.add_flag("--this")

    with pytest.raises(KeyError):
        app["this"]

    assert app["--this"] == 0

    app.parse(["--this"])

    assert app["--this"] == 1

    assert "--this" in str(app)
