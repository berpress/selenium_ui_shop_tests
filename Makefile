lint:
	@flake8 tests common locators model fixture

pytest:
	@pytest -s -v