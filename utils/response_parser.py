import re


class ResponseParser:

    @staticmethod
    def extract_xpath(response):

        if not response:
            return "INVALID"

        response = response.strip()

        response = response.replace("```xpath", "")
        response = response.replace("```", "")

        match = re.search(r"(//[^\n\r]+)", response)

        if not match:
            return "INVALID"

        xpath = match.group(1).strip()

        # Reject attribute node XPath
        if "//@" in xpath:
            return "INVALID"

        # Reject obvious English sentences
        if "xpath" in xpath.lower() and not xpath.startswith("//"):
            return "INVALID"

        return xpath