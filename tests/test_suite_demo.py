import unittest

# Get all tests from the test classes
from tests.test_adminConfiguration import AdminConfigurationsTest
from tests.test_login import LoginTest
from tests.test_postJobRequest import PostJobRequest
from tests.test_profile import ProfileTest
from tests.test_signup import SignUpTest
from tests.test_submitOffer import SubmitOffer
from tests.test_view_and_accept_offer import ViewOffersAndAcceptOffer

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AdminConfigurationsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ProfileTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(PostJobRequest)
tc6 = unittest.TestLoader().loadTestsFromTestCase(SubmitOffer)
tc7 = unittest.TestLoader().loadTestsFromTestCase(ViewOffersAndAcceptOffer)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7])

unittest.TextTestRunner(verbosity=2).run(smokeTest)


