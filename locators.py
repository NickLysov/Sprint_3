from selenium.webdriver.common.by import By


class Locators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")                                   #кнопка войти в аккаунт на главной странице
    AUTHORIZATION_PANEL = (By.XPATH, "//h2[contains(text(),'Вход')]")                                                   #открылась панель входа
    REGISTRATION_FIELD_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")                                #кнопка Зарегистрироваться на странице входа
    NAME_FIELD_REGISTRATION = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")  #поле ввода имени при регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]") #поле ввода email при регистрации
    PSSWRD_FIELD_REGISTRATION = (By.XPATH, "//input[@type='password']")                                                 #поле ввода пароля при регистрации
    REGISTRATION_PUSH_BUTTON = (By.XPATH,"// button[contains(text(), 'Зарегистрироваться')]")                           #кнопка зарегистрироваться на форме регистрации
    ENTER_BUTTON_AUTH_FORM = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]")              #кнопка Войти на странице входа
    EMAIL_FIELD_AUTHORIZATION = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]") #поле ввода email при авторизации
    PASS_FIELD_AUTHORIZATION = (By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")  #поле ввода пароля при авторизации
    CHECKOUT_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")                                          #кнопка оформления заказа на главной странице
    WRONG_PASS_MESSAGE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/p[1]")    #плашка о некорректном пароле при регистрации
    LK_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")                                                    #кнопка личного кабинета
    LOGIN_BUTTON_ON_REGISTRATION_FORM = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]")    #кнопка входа с формы регистрации
    FORGOT_PASSWORD_PANEL_OPEN_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[2]/a[1]")    #кнопка перехода к панели восстановления пароля
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")                                    #кнопка "Восстановить" на панели восстановления пароля
    PROFILE_FIELD = (By.XPATH, "//a[contains(text(),'Профиль')]")                                                       #Поле с надписью профиль в ЛК
    EXIT_BUTTON_ON_LK = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/nav[1]/ul[1]/li[3]/button[1]")        #Кнопка выхода из профиля в ЛК
    LOGO_BUTTON = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")                                                        #Кнопка-логотип бургера
    CONSTRUCTOR_BUTTON = (By.XPATH, "//header/nav[1]/ul[1]/li[1]/a[1]")                                                 #Кнопка перехода в Конструктор
    SOUS_CONSTRUCTOR_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]/span[1]")     #Кнопка Соусы в конструкторе
    BULKI_CONSTRUCTOR_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[1]/span[1]")    #Кнопка Булки в конструкторе
    NACHINKI_CONSTRUCTOR_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[3]/span[1]") #Кнопка Начинки в конструкторе