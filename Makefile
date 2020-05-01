lint:
	@flake8 tests common locators model fixture

pytest:
	@pytest -s -v

allure:
	@pytest --alluredir=/tmp/my_allure_results -s -v
