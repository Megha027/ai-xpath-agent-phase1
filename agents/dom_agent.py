from bs4 import BeautifulSoup
from models.web_element import WebElement


class DOMAgent:

    def get_interactive_elements(self, driver):

        html = driver.page_source

        print("\n========== DEBUG ==========")
        print("HTML Length :", len(html))
        print(html[:500])
        print("===========================\n")

        soup = BeautifulSoup(html, "lxml")

        print("Inputs :", len(soup.find_all("input")))
        print("Buttons:", len(soup.find_all("button")))
        print("Links   :", len(soup.find_all("a")))

        elements = []

        # -----------------------------
        # Find all input fields
        # -----------------------------
        for element in soup.find_all("input"):

            element_name = (
                    element.get("aria-label")
                    or element.get("aria-label")
                    or element.get("name")
                    or element.get("id")
                    or "Input Field"
            )

            elements.append(
                WebElement(
                    tag="input",
                    element_type=element.get("type"),
                    element_id=element.get("id"),
                    name=element.get("name"),
                    placeholder=element.get("placeholder"),
                    html=str(element),
                    element_name=element_name
                )
            )

        # -----------------------------
        # Find all buttons
        # -----------------------------
        for element in soup.find_all("button"):

            element_name = (
                    element.get_text(strip=True)
                    or element.get("aria-label")
                    or element.get("id")
                    or "Button"
            )

            elements.append(
                WebElement(
                    tag="button",
                    element_id=element.get("id"),
                    name=element.get("name"),
                    text=element.get_text(strip=True),
                    html=str(element),
                    element_name=element_name
                )
            )

        # -----------------------------
        # Find all links
        # -----------------------------
        for element in soup.find_all("a"):

            text = element.get_text(strip=True)

            if text:

                element_name = (
                        text
                        or element.get("title")
                        or element.get("aria-label")
                        or element.get("href")
                        or "Link"
                )

                elements.append(
                    WebElement(
                        tag="a",
                        text=text,
                        href=element.get("href"),
                        html=str(element),
                        element_name=element_name
                    )
                )

        return elements