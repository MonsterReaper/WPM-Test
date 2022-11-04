# Run this command on terminal before starting (If you have pip and python): pip install pyjokes
from WPM_Test import WPM
Test = WPM()
x = input("Take a test or no (y/n): ")
x = x.lower()
if x == "y":
    Test.test_now()
else:
    exit()

