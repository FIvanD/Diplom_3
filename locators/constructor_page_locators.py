from selenium.webdriver.common.by import By

class ConstructorPageLoc:
    LOG_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]' # кнопка войти в аккаунт
    PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'  # кнопка перехода в личный кабинет
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка оформления заказа
    ORDER_TAPE_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'  # кнопка перехода на ленту заказов
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'  # кнопка перехода к конструктору
    INGRIT_BUTTON = By.CSS_SELECTOR, 'ul a:first-child img'  # кнопка ингредиента раздела Булки
    MODAL_WINDOW = By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]'  # модальное окно Детали ингредиента
    CLOSE_MOD_BUTTON = By.XPATH, "//section[contains(@class, 'Modal_modal')]//button"  # кнопка крестик на модальном окне Деталей ингредиента/оформленного заказа
    BURGER_INGRIT = (By.CSS_SELECTOR, 'section[class*="BurgerConstructor_basket"]')  # блок для переноса ингредиентов
    INGRIT_CLOSE_MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal__container'] button")  # закрытое модальное окно деталей ингредиента
    COUNT_NUMBER = By.CSS_SELECTOR, "div.counter_counter__ZNLkj > p" # счетчик ингредиентов
    ORDER_MODAL_WINDOW = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]') # модальное окно оформленного заказа
    NEW_NUMBER_ORDER = By.XPATH, ".//p[text()='Ваш заказ начали готовить']"  # номер только что оформленного заказа
    ORDER_NUMBER_FROM_MODAL = By.XPATH, "//h2[contains(@class, 'text_type_digits-large') and starts-with(@class, 'Modal_modal__title')]"
