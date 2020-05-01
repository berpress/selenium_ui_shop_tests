class Authentication:
    ERROR_EMAIL = 'There is 1 error\nInvalid email address.'
    ERROR_EMPTY_LOGIN = 'There is 1 error\nAn email address required.'
    ERROR_AUTH = 'There is 1 error\nAuthentication failed.'
    LOGIN_FORM = 'ALREADY REGISTERED?'
    LOGIN_HELPERS = ['Email address', 'Email address', 'Password',
                     'Forgot your password?']


class Users:
    user = 'Biil Novikov'


SIZE = ['S', 'L', 'M']


class Colors:
    black = 'rgb(67, 74, 84);'
    orange = 'rgb(243, 156, 17);'
    blue = 'rgb(93, 156, 236);'
    yellow = 'rgb(241, 196, 15);'


class PrintedDress:
    name = 'Printed Dress'
    model = 'demo_3'
    description = '100% cotton double printed dress. Black and white ' \
                  'striped top and orange high waisted skater skirt bottom.'
    price = '$26.00'


class PrintedSummerDress:
    name = 'Printed Summer Dress'
    model = 'demo_5'
    description = 'Long printed dress with thin adjustable straps. ' \
                  'V-neckline and wiring under the bust with ruffles at ' \
                  'the bottom of the dress.'
    price = '$28.98'
    color_black = Colors.black
    color_orange = Colors.orange
    color_blue = Colors.blue
    color_yellow = Colors.yellow
