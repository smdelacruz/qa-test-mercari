class Timelinepage():
    """
    Timeline page
    """
    # Step: Input Text on Search field
    def input_search_field(search_text):
        find_element("search_field_element").send_keys(search_text)
    
    # Step: Input Text on Search field and click Enter
    def search_item(search_text):
        input_search_field(search_text)
        click_enter()
        return items 

    # Step: Navigate to MyPage from Timeline Page
    def navigate_to_mypage():
        find_element("search_mypage_element").click()