from tests.ui.qa_tools import TestQaToolsBase


class TestQaTools(TestQaToolsBase):

    def test_purchase_t_shirt(self, rp_logger):
        rp_logger.info("Purchase t-shirt")
        self.qa_order_page.purchase_item()
        rp_logger.info("Check order present")
        assert self.qa_order_page.is_order_present()
