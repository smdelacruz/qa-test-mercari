class AddShippingPage():
    """
    Add New Shipping Address Form
    """

    #Step: Fill out Shipping address form
    def fill_out_shipping_form():
        firstname = "firstname"
        lastname = "lastname"
        street = "street"
        zipcode = "zipcode"
        ...
        find_element("firstname_field_element").send_keys("firstname")
        find_element("lastname_field_element").send_keys("lastname")
        find_element("japanese_fname_field_element").send_keys("Japanese firstname")
        find_element("japanese_lname_field_element").send_keys("Japanese lastname")
        find_element("street_field_element").send_keys("Street address")
        find_element("prefecture_field_element").send_keys("prefecture")
        find_element("city_field_element").send_keys("Town/City")
        find_element("zipcode_field_element").send_keys("Zipcode")
        ... #and so on
        return [firstname, lastname, street, zipcode....]

    #Step: Click Submit address button to save
    def click_submit_address_button()
        find_element("submit_address_button").click()

    #Step: Click Back button to go back to shipping address list
    def click_back_to_shipping_address_list_button()
        find_element("back_to_shipping_address_list").click()