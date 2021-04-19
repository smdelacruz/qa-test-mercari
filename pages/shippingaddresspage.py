class ShippingAddresspage():
    """
    Shipping address Screen
    """
    #Step : Add Shipping Address
    def click_add_shipping():
        find_element("add_shipping_element").click()

     # Step: Get all shipping address on the list
    def get_all_address_count():
        address_element = find_element("address_list_element").text
        return address_element_count

    #Step: Navigate to Shipping Address Form from Shipping address list page
    def click_add_new_shipping_address():
        find_element("add_shipping_element_link").click()
        