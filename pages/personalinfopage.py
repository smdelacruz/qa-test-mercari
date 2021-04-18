class PersonalInformationPage():
    """
    Personal Information Screen
    """

    #Step: Navigate to Shipping address list page from Personal information page
    def navigate_to_shipping_address_page():
        find_element("shipping_address_element_link").click()