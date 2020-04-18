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


@pytest.mark.parametrize("login,password", [("login", "password"), ('t', 't')])
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
    assert app.login.error_auth_text() == Authentication.ERROR_AUTH, \
        'Check error message'
