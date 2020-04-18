lint:
	@poetry run flake8 tests common locators model fixture

pytest:
	@poetry run pytest -s