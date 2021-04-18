from test_data.login_credentials import LoginCredentials

class Login():
    """
    Login Valid user
    """
    # Step: Enter Username
    def enter_username(self, username):
        find_element("username_field_element").send_keys(username)

    # Enter Password
    def enter_password(self, password):
        find_element("password_field_element").send_keys(password)

    # Login User
    def user_login(self, username=LoginCredentials.username, password=LoginCredentials.password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()
