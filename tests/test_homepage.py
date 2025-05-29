def test_homepage_elements(home_page):
    assert home_page.is_logo_visible(), "Логотип должен быть виден"
    assert home_page.is_search_box_present(), "Поле поиска должно быть на странице"