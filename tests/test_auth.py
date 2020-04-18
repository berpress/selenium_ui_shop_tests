import pytest

from model.login import UserData


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
    app.login.authorization(user_data)
    assert app.page.login_name_text() == 'Biil Novikov', 'Check name after ' \
                                                    'authorization'
    app.page.logout_btn()
