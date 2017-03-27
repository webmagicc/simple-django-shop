from selenium import webdriver
from django.conf import settings
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def get_driver():
    service_args = [
        #'--proxy=proxy.crawlera.com:8010',
        #'--proxy-auth=XXXXXXXXXXX:XXXXXXXXXXXXXX',
        #'--proxy-type=http',
        '--load-images=false',
        '--ssl-protocol=any',
        '--load-images=false',
        '--webdriver-logfile=phantom.log',
        #'--ssl-client-certificate-file='+CRAWLERA_SERT,
        '--ignore-ssl-errors=yes',
        '--webdriver-loglevel=DEBUG',
        '--web-security=false',
        ]
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87"
    )
    #dcap['phantomjs.page.customHeaders.X-Crawlera-Use-Https'] = '0'
    #dcap['phantomjs.page.customHeaders.X-Crawlera-Session'] = 'create'
    #dcap['phantomjs.page.customHeaders.X-Crawlera-UA'] = 'desktop'

    driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS,
                                service_args=service_args,
                                desired_capabilities=dcap)
    
    driver.set_window_size(1120, 550)
    return driver