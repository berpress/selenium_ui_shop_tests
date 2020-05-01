from common.constans import PrintedDress, PrintedSummerDress, Colors


def test_open_product_card(app, login):
    """
        1. Open page
        2. Choose product
        3. Open product card
        4. Check product info
    """
    app.page.select_woman_category()
    app.page.open_product('Printed Dress')
    assert app.page.product_name() == PrintedDress.name
    assert app.page.product_model() == PrintedDress.model
    assert app.page.product_description() == PrintedDress.description
    assert app.page.product_price() == PrintedDress.price


def test_color_dress(app, login):
    """
        1. Open page
        2. Choose product
        3. Open product card
        4. Check product colors
    """
    app.page.select_woman_category()
    app.page.open_product('Printed Summer Dress')
    assert app.page.product_name() == PrintedSummerDress.name
    assert app.page.product_model() == PrintedSummerDress.model
    assert app.page.product_description() == PrintedSummerDress.description
    assert app.page.product_price() == PrintedSummerDress.price
    assert app.page.get_color(app.page.black_color()) == Colors.black
    assert app.page.get_color(app.page.orange_color()) == Colors.orange
    assert app.page.get_color(app.page.blue_color()) == Colors.blue
    assert app.page.get_color(app.page.yellow_color()) == Colors.yellow
