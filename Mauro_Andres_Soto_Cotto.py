from selenium import webdriver
import time

PATH = "D:\\UNAH\\Python\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

# 2. Use the size filter to select size M and add to cart 1 shirt

search_size_m = driver.find_element_by_xpath("//div[@class='sc-ebmerl-2 hqhzVN']//label//span[text()='M']").click()
time.sleep(1)
make_click_add_m = driver.find_element_by_xpath("//button[contains(text(),'Add to cart')]").click()

time.sleep(1)

close_cart_1 = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/button[1]").click()

# Use the size filter to unselect M size and select L size.

unselect_size_m = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[3]/label[1]/span[1]").click()
time.sleep(1)

select_size_l = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[5]/label[1]/span[1]").click()
time.sleep(1)
# Compulsively add 6 shirts to your cart.

i = 1
while i < 7:
    select_6_shirts = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[1]/button[1]").click()
    i += 1
time.sleep(2)

# Come back to your senses and delete 4 shirts from your cart.

j = 1
while j < 5:
    unselect_4_shirts = driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]").click()
    j += 1

time.sleep(1)

# Click checkout button.

click_checkout = driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/button").click()
time.sleep(10)
