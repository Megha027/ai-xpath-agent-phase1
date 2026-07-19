from browser.browser_manager import BrowserManager
from agents.dom_agent import DOMAgent
from agents.ai_agent import AIAgent
from utils.logger import get_logger
from config import BASE_URL
from validators.xpath_validator import XPathValidator
from services.excel_writer import ExcelWriter


class Orchestrator:

    def __init__(self):
        self.browser = BrowserManager()
        self.dom_agent = DOMAgent()
        self.ai_agent = AIAgent()
        self.validator = XPathValidator()
        self.excel_writer = ExcelWriter()   # NEW
        self.logger = get_logger()
        self.excel_writer = ExcelWriter()

    def run(self):

        self.logger.info("===== AI XPath Agent Started =====")

        # Start Browser
        self.browser.start_browser()

        # Open URL
        self.logger.info(f"Opening URL : {BASE_URL}")
        self.browser.open_url(BASE_URL)

        # Extract Interactive Elements
        elements = self.dom_agent.get_interactive_elements(
            self.browser.driver
        )

        self.logger.info(f"Total Elements Found : {len(elements)}")

        print("\n===== INTERACTIVE ELEMENTS =====\n")

        # Generate XPath + Validate
        for index, element in enumerate(elements, start=1):

            try:
                # Generate XPath using AI
                element.ai_xpath = self.ai_agent.generate_xpath(element)

                # Validate XPath
                element.validation_status = self.validator.validate(
                    self.browser.driver,
                    element.ai_xpath
                )

            except Exception as ex:
                element.ai_xpath = f"AI Error: {ex}"
                element.validation_status = "ERROR"

            print(f"{index}. {element}")
            print(f"Validation Status : {element.validation_status}")
            print("-" * 80)

        # NEW: Save report to Excel
        self.excel_writer.write(elements)

        input("\nPress Enter to close browser...")

        self.browser.close_browser()

        self.logger.info("Browser Closed")
        self.logger.info("===== AI XPath Agent Finished =====")