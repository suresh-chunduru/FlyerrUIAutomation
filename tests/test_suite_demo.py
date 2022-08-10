import unittest

from tests.test_adminConfiguration import AdminConfigurationsTest
from tests.test_login import LoginTest
from tests.test_profile import ProfileTest
from tests.test_signup import SignUpTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AdminConfigurationsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ProfileTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(smokeTest)


