from selenium.webdriver.common.by import By

class OrderFeedPageLoc:

    ORDER_LIST = By.XPATH, '(//ul[@class="OrderFeed_list__OLh59"])[1]'  # первый заказ из списка заказов
    ORDER_DETAIL_MODAL = By.CLASS_NAME, 'Modal_modal__container__Wo2l_' # модальное окно деталей заказа
    ORDER_NUMBER_IN_FEED = By.XPATH, '//p[@class="text text_type_digits-default"]' # номер заказа из ленты
    ALL_ORDERS_ALL_TIME = By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]" # счетчик всех заказов за все время
    ALL_ORDERS_TODAY = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]" # счетчик всех заказов за сегодня
    NUMBER_IN_WORK = By.XPATH, './/*[contains(@class, "orderListReady")]//*[contains(@class, "digits-default")]'