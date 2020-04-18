venv:
	source ./env/bin/activate;

lint:
	@poetry run flake8 tests common locators model fixture