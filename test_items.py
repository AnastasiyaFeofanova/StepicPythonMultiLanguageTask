link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_btn_add_to_basket_should_be_visible(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")