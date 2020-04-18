import pytest


def test_auth_shop(app):
    """
    1. Open page
    2. Click login button
    3. Enter valid login / password values
    4. Check name
    """
    app.open_main_page()
    app.login.authorization(login='fobiw39468@homedepinst.com',
                            password='Password11')
    pass
