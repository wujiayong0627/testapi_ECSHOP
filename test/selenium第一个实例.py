from selenium import webdriver
from selenium.webdriver import Proxy
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.headless = True
options.page_load_strategy = 'eager'
options.browser_version = ""
options.accept_insecure_certs = True
options.timeouts = {"implicit": None, "pageLoad": None, "script": None}
options.unhandled_prompt_behavior = False
options.proxy = Proxy
print(options.capabilities)
print(options.arguments)
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://www.baidu.com")

print(driver.title)
