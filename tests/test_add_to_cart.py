from pages.product_page import ProductPage

def test_add_product_to_cart(browser):
    product = ProductPage(browser)
    product.go_to_product()
    product.select_size_and_color()
    product.add_to_cart()
    assert product.verify_cart_updated(), "Корзина не обновилась после добавления товара"
