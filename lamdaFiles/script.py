from csv import excel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from random import randrange
import os
import zipfile
import json
from selenium.webdriver.common.proxy import Proxy, ProxyType
class script:
    def generateProxy(self, data):
        data = data.split(':')
        PROXY_HOST = data[0]
        PROXY_PORT = data[1]
        PROXY_USER = "Dataraider"
        PROXY_PASS = "Mypass1234"


        self.manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        self.background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST,PROXY_PORT, PROXY_USER, PROXY_PASS)
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", self.manifest_json)
            zp.writestr("background.js", self.background_js)
        # print(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


    def init_driver(self,proxy):
        # self.generateProxy(proxy)
        proxy = proxy.split(':')
        PROXY_HOST = proxy[0]
        PROXY_PORT = proxy[1]
        PROXY_USER = "Dataraider"
        PROXY_PASS = "Mypass1234"
        chrome_options = webdriver.ChromeOptions()
        # # prox = Proxy()
        # # prox.proxy_type = ProxyType.MANUAL
        # # # prox.http_proxy = "ip_addr:port"
        # # prox.socks_proxy = PROXY_HOST+':'+PROXY_PORT
        # # # prox.ssl_proxy = "ip_addr:port"
        # # prox.socks_password = PROXY_PASS
        # # prox.socks_username = PROXY_USER

        # # capabilities = webdriver.DesiredCapabilities.CHROME
        # # prox.add_to_capabilities(capabilities)

# Proxy proxy = new Proxy();
# proxy.Kind = ProxyKind.Manual;
# string proxyUrl = "proxy.example.net:8080";

# proxy.SocksProxy = proxyUrl;
# proxy.SocksPassword = "user123";
# proxy.SocksUserName = "pass123";

# ChromeOptions options = new ChromeOptions();
# options.Proxy = proxy;

# IWebDriver driver = new ChromeDriver(options);

        # # driver = webdriver.Chrome(desired_capabilities=capabilities)
        # chrome_options.add_argument('--proxy-server=http://user-Dataraider-sessionduration-1:Mypass1234@'+PROXY_HOST+':'+PROXY_PORT)
        chrome_options.add_argument('--proxy-server=http://'+PROXY_HOST+':'+PROXY_PORT)
        # chrome_options.add_argument('--proxy-server=http://Dataraider:Mypass1234')
        # chrome_options.add_extension("proxy_auth_plugin.zip")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = self.get_chromedriver(use_proxy=True,)
        self.wait = WebDriverWait(self.driver,3)


    def ip_requests(self):
        # content = self.driver.getPageSource("http://httpbin.org/ip")
        # self.init_driver()
        try:
            self.driver.get("http://httpbin.org/ip")
            elem = self.driver.find_element_by_xpath('/html/body/pre')
            # content = self.driver.page_source
            print(elem.text)
            print(json.loads(elem.text)["origin"])
            ip = json.loads(elem.text)["origin"]
            self.driver.quit()
            return ip
        except:
            self.ip_requests()

    def putData(self,data):
        proxy = data[1]
        data = data[0]
        self.init_driver(proxy[data[11]])
        print(type(data[15]),data[15],'->>>>>>')
        # exit()
        if data[15] != None:
            self.driver.get(data[15])
        else:
            self.driver.get("https://medicareplansenrollment.com/")
        # time.sleep(500)
        # html = self.driver.find_element_by_tag_name('html')
        # html.send_keys(Keys.END)
        # time.sleep(3)
        # html.send_keys(Keys.HOME)
        # time.sleep(1)
        # self.randomclick(randrange(6))
        # time.sleep(1)
        elem = self.driver.find_element_by_xpath('//*[@id="zip"]')
        elem.clear
        # elem.send_keys(str(data[1]))
        elem.send_keys(str(data[3]))
        time.sleep(1)
        elem = self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div/div/div[2]/div/div/form/div[2]/button')
        elem.click()
        select = Select(self.driver.find_element_by_xpath('//*[@id="month"]'))
        select.select_by_visible_text(data[4])
        # select.select_by_value('1')

        select = Select(self.driver.find_element_by_xpath('//*[@id="day"]'))
        select.select_by_visible_text(str(data[5]))
        # select.select_by_value('1')

        select = Select(self.driver.find_element_by_xpath('//*[@id="year"]'))
        select.select_by_visible_text(str(data[6]))
        # select.select_by_value('1')
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[3]/form/div[2]/button')
        elem.click()
        # time.sleep(10)
        try:
            AlreadyRegistered = data[7]
            if AlreadyRegistered != "N":
                elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[4]/form/div[2]/button[1]')
            else:
                elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[4]/form/div[2]/button[2]')
            elem.click()
        except:
            print('Button Not appear')
        time.sleep(2)
        try:
            SocialSecurityDisability = data[8]
            if SocialSecurityDisability != "N":
                elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[7]/form/div/button[1]')
            else:
                elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[7]/form/div/button[2]')
            elem.click()
        except:
            print('Button Not appear')

        time.sleep(2)

        elem = self.driver.find_element_by_xpath('//*[@id="firstname"]')
        elem.clear
        # elem.send_keys(str(data[1]))
        elem.send_keys(str(data[1]))

        elem = self.driver.find_element_by_xpath('//*[@id="lastname"]')
        elem.clear
        # elem.send_keys(str(data[1]))
        elem.send_keys(str(data[2]))

        elem = self.driver.find_element_by_xpath('//*[@id="phone"]')
        elem.clear
        # elem.send_keys(str(data[1]))
        elem.send_keys(str(data[9]))

        elem = self.driver.find_element_by_xpath('//*[@id="email"]')
        elem.clear
        # elem.send_keys(str(data[1]))
        elem.send_keys(str(data[10]))
        time.sleep(1)

        elem = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/div/div[8]/form/div[3]/button')
        elem.click()
        # time.sleep(5)
        # elem = self.driver.find_element_by_xpath('/html/body/div/div/div/section[6]/div/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div[2]/input')
        # elem.clear
        # elem.send_keys(str(data[2]))
        # elem = self.driver.find_element_by_xpath('/html/body/div/div/div/section[6]/div/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div[3]/div/input[1]')
        # elem.clear
        # elem.send_keys(str(data[3]))
        # elem = self.driver.find_element_by_xpath('/html/body/div/div/div/section[6]/div/div/div[2]/div/div/div[1]/div/div/div/form/div[1]/div[4]/input')
        # elem.clear
        # elem.send_keys(int(data[4]))
        # elem = self.driver.find_element_by_xpath('/html/body/div/div/div/section[6]/div/div/div[2]/div/div/div[1]/div/div/div/form/div[3]/button')
        # elem.click()
        time.sleep(3)
        # wait.until(EC.title_is("https://medicarechecklist.com/thankyou/"))
        self.wait.until(lambda driver: driver.current_url == 'https://medicareplansenrollment.com/thankyou')
        # time.sleep(300)




