
from common_utilities import basetest

class MercariTest(basetest.BaseTest):

    def test_ex2_sc1_navigate_to_shipping_address(self):
        """
        Exercise 2 - Scenario 1
        Navigate to Shipping address
        """
        self.login.user_login()
        self.timelinepage.navigate_to_mypage()
        self.mypage.navigate_to_personal_information_page()
        self.personalinfopage.navigate_to_shipping_address_page()
        assert "Shipping Page" in Page title
        
    def test_ex2_sc1_save_new_shipping_address(self):
        """
        Exercise 2 - Scenario 1
        Add new form and Save
        """
        self.login.user_login()
        self.timelinepage.navigate_to_mypage()
        self.mypage.navigate_to_personal_information_page()
        self.personalinfopage.navigate_to_shipping_address_page()
        self.personalinfopage.click_add_new_shipping_address()
        self.addshippingpage.fill_out_shipping_form() #expects return of address infor
        self.addshippingpage.click_submit_address_button()
        assert "Save new Shipping Address success text" is visible

    def test_ex2_sc1_verify_new_added_address(self):
        """
        Exercise 2 - Scenario 1
        Verify new added address is registered
        """
        self.login.user_login()
        self.timelinepage.navigate_to_mypage()
        self.mypage.navigate_to_personal_information_page()
        self.personalinfopage.navigate_to_shipping_address_page()
        address_list_count = self.shippingaddresspage.get_all_address_count()
        self.personalinfopage.click_add_new_shipping_address()
        addresses_list = self.addshippingpage.fill_out_shipping_form() #expects return of address infor
        self.addshippingpage.click_submit_address_button()
        self.addshippingpage.click_back_to_shipping_address_list_button()
        new_address_list_count = self.shippingaddresspage.get_all_address_count()
        assert (address_list_count + 1) is equal to new_address_list_count
        assert addresses_list exist on the shippingaddresspage list page

    def test_ex2_sc2_search_result_title(self):
        """
        Exercise 2 - Scenario 2
        Check if the item title has "MacBook" in it. 
        """
        self.login.user_login()
        items = self.timelinepage.search_an_item("Macbook")
        for item in items:
            if item is 3:
                Click item
                assert "Details page" in Page Title
                assert "Macbook" in item title element
        