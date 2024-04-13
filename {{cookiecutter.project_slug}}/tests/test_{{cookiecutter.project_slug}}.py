from {{cookiecutter.project_slug}}.common.main import hello_world


class TestPackage:
    def test_hello_world(self):
        assert hello_world() == "We are here"
