from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy
import allure


class MainPage:
    @staticmethod
    def getting_started():
        with allure.step('Check first screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('The Free '
                                                                                                      'Encyclopedia'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with allure.step('Check second screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('New ways to explore'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with allure.step('Check third screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                have.text('Reading lists with '
                          'sync'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

        with allure.step('Check fourth screen'):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

        with allure.step('Check search page'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).should(be.visible)


main_page = MainPage()
