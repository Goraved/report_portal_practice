from framework.ui.pages.test_page import QaCartPage
from tests.ui import TestBase


class TestQaToolsBase(TestBase):
    @classmethod
    def setup_class(cls):
        super(TestQaToolsBase, cls).setup_class()
        cls.qa_order_page = QaCartPage(cls.driver)
