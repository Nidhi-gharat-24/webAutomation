from selenium import webdriver
web = webdriver.Chrome("J:\company\chromedriver")
web.get('https://www.flipkart.com/')
searchbox = web.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchbox.send_keys('titan watches')

Button = web.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
Button.click()

Brand = web.fin_elemet_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[4]/div')
Brand = web.clickNthProductFromTheList(10)