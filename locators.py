from selenium.webdriver.common.by import By


class Locators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")                                   #кнопка войти в аккаунт на главной странице
    AUTHORIZATION_PANEL = (By.XPATH, "//h2[contains(text(),'Вход')]")                                                   #открылась панель входа
    REGISTRATION_FIELD_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")                                #кнопка Зарегистрироваться на странице входа
    NAME_FIELD = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::*")                                     #поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::* ")                                 #поле ввода email
    PSSWRD_FIELD = (By.XPATH, "//input[@type='password']")                                                              #поле ввода пароля
    REGISTRATION_PUSH_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")                           #кнопка зарегистрироваться на форме регистрации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")                                                     #кнопка Войти
    LOGIN_BUTTON_REGISTARTION_PANEL = (By.XPATH, "//a[contains(text(),'Войти')]")                                       #кнопка Войти на форме регистрации
    CHECKOUT_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")                                          #кнопка оформления заказа на главной странице
    WRONG_PASS_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")                                      #плашка о некорректном пароле при регистрации
    LK_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")                                                    #кнопка личного кабинета
    FORGOT_PASSWORD_PANEL_OPEN_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")                       #кнопка перехода к панели восстановления пароля
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")                                    #кнопка "Восстановить" на панели восстановления пароля
    PROFILE_FIELD = (By.XPATH, "//a[contains(text(),'Профиль')]")                                                       #Поле с надписью профиль в ЛК
    EXIT_BUTTON_ON_LK = (By.XPATH, "//button[contains(text(),'Выход')]")                                                #Кнопка выхода из профиля в ЛК
    LOGO_BUTTON = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")                                                        #Кнопка-логотип бургера
    CONSTRUCTOR_BUTTON = (By.XPATH, "//header/nav[1]/ul[1]/li[1]/a[1]")                                                 #Кнопка перехода в Конструктор
    SOUS_CONSTRUCTOR_BUTTON = (By.XPATH, "//parent::span[contains(text(),'Соусы')]")                                    #Кнопка Соусы в конструкторе
    BULKI_CONSTRUCTOR_BUTTON = (By.XPATH, "//parent::span[contains(text(),'Булки')]")                                   #Кнопка Булки в конструкторе
    NACHINKI_CONSTRUCTOR_BUTTON = (By.XPATH, "//parent::span[contains(text(),'Начинки')]")                              #Кнопка Начинки в конструкторе
    PROVERKA = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")                                              #Конструкция для проверки Начинок