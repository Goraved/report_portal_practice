class Utilities:
    def get_screenshot(self):
        from conftest import LOGGER
        LOGGER.info("Failure attachment",
                    attachment={"name": "screenshot.png",
                                "data": self.driver.get_screenshot_as_png(),
                                "mime": "image/png"})
