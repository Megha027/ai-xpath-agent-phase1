class WebElement:

    def __init__(
            self,
            tag,
            element_type=None,
            element_id=None,
            name=None,
            text=None,
            placeholder=None,
            href=None,
            html=None,
            validation_status=None,
            element_name=None   # NEW
    ):
        self.element_name = element_name
        self.tag = tag
        self.element_type = element_type
        self.element_id = element_id
        self.name = name
        self.text = text
        self.placeholder = placeholder
        self.href = href

        # HTML used by AI
        self.html = html

        # Generated XPaths
        self.xpath = None
        self.ai_xpath = None

        # Validation result
        self.validation_status = "NOT_VALIDATED"

    def __str__(self):

        return (
        f"Element={self.element_name}, "
        f"Tag={self.tag}, "
        f"AI XPath={self.ai_xpath}, "
        f"Status={self.validation_status}"
        )