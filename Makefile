lint:
	@flake8 tests common locators model fixture

pytest:
	@pytest -s -v

allure:
	@pytest --alluredir=/tmp/allure_results -s -v

report:
	@allure serve /tmp/allure_results
