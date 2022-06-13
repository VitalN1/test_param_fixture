link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_btn(browser):
    browser.get(link)
    assert browser.find_elements_by_class_name("btn-add-to-basket"), 'нет кнопки корзины'
