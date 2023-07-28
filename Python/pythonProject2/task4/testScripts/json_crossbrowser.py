import sys

from task4.testScripts.conftest import jsonData

sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2')
import time
import pytest

from task4.pageObjects.googleHome import Google_Home
from task4.Locators import googlelocators



@pytest.mark.usefixtures("crossbrowsertesting")
class TestDockerApp:

    @pytest.mark.smoke
    def test_docker_print_links(self,jsonData):
        obj = Google_Home(self.driver)
        obj.launch_app_with_url(jsonData['url_docker'])



