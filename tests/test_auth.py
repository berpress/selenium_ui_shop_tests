import pytest
from model.login import UserData
from common.constans import Authentication


def test_auth_shop(app):
    """
        1. Open page
        2. Click login button
        3. Enter valid login / password values
        4. Check name
    """
    app.open_main_page()
    user_data = UserData(login='fobiw39468@homedepinst.com',
                         password='Password11')
    app.login.authentication(user_data)
    assert app.page.login_name_text() == 'Biil Novikov', 'Check name after ' \
                                                         'authorization'
    app.page.logout_user()


@pytest.mark.parametrize("login,password", [
    ("login", "password"),
    ('login', None),
])
def test_invalid_auth(app, login, password):
    """
        1. Open page
        2. Click login button
        3. Enter invalid login / password values
        4. Check error
    """
    app.open_main_page()
    user_data = UserData(login=login, password=password)
    app.login.authentication(user_data)
    assert app.login.error_auth_text() == Authentication.ERROR_EMAIL, \
        'Check error message'


def test_empty_login(app):
    """
        1. Open page
        2. Click login button
        3. Enter empty login and password values
        4. Check error
    """
    app.open_main_page()
    user_data = UserData(login=None, password='password')
    app.login.authentication(user_data)
    assert app.login.error_auth_text() == Authentication.ERROR_EMPTY_LOGIN, \
        'Check error message'


def test_auth_unregistered(app):
    """
        1. Open page
        2. Click login button
        3. Enter unregistered user data
        4. Check error
    """
    app.open_main_page()
    user_data = UserData().random_user()
    app.login.authentication(user_data)
    assert app.login.error_auth_text() == Authentication.ERROR_AUTH, \
        'Check error message'


def test_check_login_object(app):
    """
        1. Open page
        2. Click login button
        3. Check object login
    """
    app.open_main_page()
    app.login.sign_button_click()
    assert app.login.login_form_text() == Authentication.LOGIN_FORM
    helpers = app.login.helper_login()
    for i, element in enumerate(helpers[:-1]):
        assert element.text == Authentication.LOGIN_HELPERS[i]
