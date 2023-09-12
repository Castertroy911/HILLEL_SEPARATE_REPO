class HomePageLocators:
    ELEMENTS_PAGE_LOCATOR = '//h5[contains(text(), "Elements")]'
    FORMS_PAGE_LOCATOR = '//h5[contains(text(), "Forms")]'
    ALERTS_PAGE_LOCATOR = '//h5[contains(text(), "Alerts, Frame & Windows")]'
    HOME_PAGE_LOCATOR = '//header/a'


class ElementsPageLocators:
    TEXT_BOX_PAGE_LOCATOR = '//li[@id="item-0"]/span[contains(text(), "Text Box")]'
    CHECK_BOX_PAGE_LOCATOR = '//li[@id="item-1"]/span[contains(text(), "Check Box")]'
    RADIO_BUTTON_PAGE_LOCATOR = '//li[@id="item-2"]/span[contains(text(), "Radio Button")]'


class TextBoxPageLocators:
    ENTER_FULL_NAME_LOCATOR = '//input[@id="userName"]'
    ENTER_EMAIL_LOCATOR = '//input[@id="userEmail"]'
    ENTER_CURRENT_ADDRESS_LOCATOR = '//textarea[@id="currentAddress"]'
    ENTER_PERMANENT_ADDRESS_LOCATOR = '//textarea[@id="permanentAddress"]'
    SUBMIT_BUTTON_LOCATOR = '//button[@id="submit"]'
    CHECK_FULL_NAME_LOCATOR = '//p[@id="name"]'
    CHECK_EMAIL_LOCATOR = '//p[@id="email"]'
    CHECK_CURRENT_ADDRESS_LOCATOR = '//p[@id="currentAddress"]'
    CHECK_PERMANENT_ADDRESS_LOCATOR = '//p[@id="permanentAddress"]'


class CheckBoxPageLocators:
    COLLAPSE_LIST = '//*[@class="rct-icon rct-icon-expand-close"]'
    DESKTOP_CHECKBOX_LOCATOR = '//span[contains(text(), "Desktop")]/preceding-sibling::span' \
                               '[@class="rct-checkbox"]/*[@stroke="currentColor"]'
    DOWNLOADS_CHECKBOX_LOCATOR = '//span[contains(text(), "Downloads")]/preceding-sibling::span' \
                                 '[@class="rct-checkbox"]/*[@stroke="currentColor"]'


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = '//label[@for="yesRadio"]'
    IMPRESSIVE_RADIO_BUTTON = '//label[@for="impressiveRadio"]'
    NO_RADIO_BUTTON = '//label[@for="noRadio"]'
    SELECTED_BUTTON_LOCATOR = '//span[@class="text-success"]'


class FormsPageLocators:
    PRACTICE_FORM_PAGE = '//li[@id="item-0"]/span[contains(text(), "Practice Form")]'
    WIDGETS_PAGE_LOCATOR = '(//span[@class="pr-1"])[4]'


class PracticeFormPageLocators:
    FIRST_NAME = '//input[@id="firstName"]'
    LAST_NAME = '//input[@id="lastName"]'
    EMAIL = '//input[@id="userEmail"]'
    GENDER = '//label[@for="gender-radio-1"]'
    MOBILE = '//input[@id="userNumber"]'
    DATE_OF_BIRTH_FIELD = '//input[@id="dateOfBirthInput"]'
    DATE_OF_BIRTH_DAY = '//div[@class="react-datepicker__day ' \
                        'react-datepicker__day--002 react-datepicker__day--weekend"]'
    SUBJECT = '//div[@class="subjects-auto-complete__value-container '\
              'subjects-auto-complete__value-container--is-multi css-1hwfws3"]'
    HOBBIES_SPORT = '//label[@for="hobbies-checkbox-1"]'
    HOBBIES_MUSIC = '//label[@for="hobbies-checkbox-3"]'
    PICTURE = '//input[@id="uploadPicture"]'
    CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
    STATE = '//div[@class=" css-1hwfws3"]'
    CITY = '(//div[@class=" css-1hwfws3"])[2]'
    SUBMIT_BUTTON = '//button[@class="btn btn-primary"]'
    CONFIRM_MODAL_FORM = '//div[@id="example-modal-sizes-title-lg"]'
    CLOSE_MODAL_BUTTON = '//button[@id="closeLargeModal"]'


class AllertsPageLocators:
    BROWSER_WINDOWS = '//div[@class="element-list collapse show"]//li[@id="item-0"]'
    ALERTS = '//div[@class="element-list collapse show"]//li[@id="item-1"]'


class BrowserWindowPageLocators:
    NEW_TAB = '//button[@id="tabButton"]'
    NEW_WINDOW = '//button[@id="windowButton"]'
    TEXT_ON_NEW_TAB = '//h1[@id="sampleHeading"]'
    TEXT_IN_NEW_WINDOW = '//h1[@id="sampleHeading"]'
