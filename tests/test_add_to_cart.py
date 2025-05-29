from pages.product_page import ProductPage

def test_add_product_to_cart(product_page):
    product_page.go_to_product()
    product_page.select_size_and_color()
    product_page.add_to_cart()
    assert product_page.verify_cart_updated(), "Корзина не обновилась после добавления товара"
