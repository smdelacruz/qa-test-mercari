from common_utilities import config
from pages.login import Login
from pages.homepage import HomePage
from pages.mypage import MyPage
from pages.login import Login

class BaseTest(unittest.TestCase):
    # Setup
    def setUp():
        self.login = Login()
        self.homepage = HomePage()
        self.timelinepage = Timelinepage()
        self.mypage = MyPage()
        self.personalinfopage = PersonalInformationPage()
        self.addshippingpage = AddShippingPage()
        self.shippingaddresspage = ShippingAddresspage()

    # tearDown
    def tearDown():
        quit