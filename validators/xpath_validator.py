from selenium.webdriver.common.by import By


class XPathValidator:

    def validate(self, driver, xpath):

        if xpath == "INVALID":
            return "INVALID"

        try:
            elements = driver.find_elements(By.XPATH, xpath)

            if len(elements) == 1:
                return "VALID"

            elif len(elements) > 1:
                return "DUPLICATE"

            else:
                return "INVALID"

        except Exception:
            return "INVALID"