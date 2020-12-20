from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# your url
forms_url = ''

# your email
ms_email = ''

# your pass
ms_passwd = ''

# chromeを起動オプションを指定
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# docker上のchromeと接続
print('connectiong to remote browser...')
driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  desired_capabilities=options.to_capabilities(),
  options=options,
)

# formsに飛ぶ
driver.get(forms_url)

# メアドを入力
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys(ms_email)
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()

print(driver.title)

sleep(5)

# パスワードを入力
driver.find_element_by_xpath('//*[@id="i0118"]').send_keys(ms_passwd)
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()

sleep(5)

# サインインを保持するか聞かれるので拒否
print(driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[1]').text)
driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()

sleep(5)

print("signed account")
print(driver.title)

# 36.7を選択
driver.execute_script('document.getElementsByClassName("select-control")[0].click()')
driver.execute_script('document.getElementsByClassName("select-option-nocheck")[17].click()')

# 提出！
driver.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button/div').click()

print("done form")

driver.quit()
