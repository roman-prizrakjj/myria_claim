from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


def mm():
    print("-----логинимся в MM------")
    EXTENSION_PATH = "./mm.crx"
    options = Options()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    options.add_argument("--page-load-strategy=eager")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_extension(EXTENSION_PATH)
    global driver
    driver = webdriver.Chrome(desired_capabilities=caps, service=Service(ChromeDriverManager().install()),options=options)
    time.sleep(4)
    password = 'qwertyub34'
    seedtemp = []
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#onboarding/welcome")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding__terms-checkbox"]'))).click()
    # input('')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[2]/button'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div/button[2]'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input'))).send_keys(password)
    time.sleep(0.1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input'))).send_keys(password)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/button[2]'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[6]/button'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div/div/div[2]')))
    seed = driver.find_elements(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div/div/div[2]')
    time.sleep(0.5)
    for i in seed:
        temp = i.text
        seedtemp.append(temp)
        seed = seedtemp
        seed_string = " ".join(seed)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[6]/div/button'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/input'))).send_keys(seed[2])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/div[4]/div[2]/input'))).send_keys(seed[3])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/div[8]/div[2]/input'))).send_keys(seed[7])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/button'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'))).click()
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[1]/div/button/span'))).click()
    print("-----Успешный лог MM------")


def privateer(private_key):
    print("-----заходим под приваткой-----")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/button'))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/button[2]'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="private-key-box"]'))).send_keys(
        private_key)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/button[2]'))).click()
    time.sleep(3)
    print("-----зашли-----")


def login(nfturl):
    print("-----логинимся в мурии-----")
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    driver.get(nfturl)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="radix-40"]/div/div/button'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[1]/header/nav/div[2]/div/div[1]/div/button/span'))).click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    driver.refresh()
    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    else:
        time.sleep(5)
        driver.refresh()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    driver.refresh()
    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    else:
        time.sleep(5)
        driver.refresh()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    driver.switch_to.window(driver.window_handles[1])
    print("-----успешный лог мурии-----")


def sale(price):
    print("-----выставляем нфт-----")
    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button'))):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button'))).click()
    else:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button[1]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                    "//input[@class='bg-base/4 mt-1 rounded-lg border-none pr-[100px] pl-10 input block w-full']"))).send_keys(
        price)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn-lg  w-full px-10 btn-primary']"))).click()
    time.sleep(10)
    driver.refresh()
    print("-----Выставили нфт-----")


def sales(nfturl, price,private_key):
    print("-----Выставляем нфт-----")
    driver.get(nfturl)

    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button'))):

        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button'))).click()
    else:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div/div[1]/div[2]/div[3]/button[1]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                    "//input[@class='bg-base/4 mt-1 rounded-lg border-none pr-[100px] pl-10 input block w-full']"))).send_keys(
        price)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn-lg  w-full px-10 btn-primary']"))).click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='relative mb-1 text-lg font-semibold leading-normal dark:text-white']")))
        r = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='relative mb-1 text-lg font-semibold leading-normal dark:text-white']")))
        print(f"-----Выставили нфт цена {price} -----")
    except:
        print(f"-----у кошелька {private_key} и нфт {nfturl} Цена не изменилась-----")


def loginmint():
    url = "https://myria.com/airdrop/"
    print("-----логинимся в мурии-----")
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]'))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    #if WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                     #  "//button[@class='absolute top-5 right-6 w-[32px] text-white/50 focus:outline-none md:top-3']"))):
       # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                       # "//button[@class='absolute top-5 right-6 w-[32px] text-white/50 focus:outline-none md:top-3']"))).click()
    time.sleep(3)
    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div/input'))):

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="__next"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/div/input'))).click()
    if WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/button'))):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div/div/div/div/div[1]/button'))).click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])


def minting():
    mintstatus = False
    while mintstatus == False:
        driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        buttonmint = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                     "//button[@class='btn-lg btn-primary disabled:bg-gray/4 disabled:text-gray/6 flex items-center justify-center px-[72px]']")))
        if buttonmint.text == "MINT NOW":
            buttonmint.click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]'))).click()
            driver.switch_to.window(driver.window_handles[1])
            for _ in range(15):
                buttonstatus = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                               "//button[@class='btn-lg btn-primary disabled:bg-gray/4 disabled:text-gray/6 flex items-center justify-center px-[72px]']"))).text

                print(buttonstatus)
                if buttonstatus == "MINTING...":
                    time.sleep(2)
                elif buttonstatus == "MINTED":
                    driver.quit()
                    break

        else:
            driver.quit()
            break


def sale_main(private_key, nftdict):
    if len(nftdict) > 1:
        print("-----Больше одного нфт-----")
        mm()
        privateer(private_key)
        login("https://myria.com/marketplace/asset-detail/?id=13759")
        for key, nftdata in nftdict.items():
            nfturl = key
            price = nftdata[1]
            sales(nfturl, price)
    else:
        print("-----Одна нфт-----")
        mm()
        privateer(private_key)
        login(list(nftdict.keys())[0])
        sale(list(nftdict.values())[0][1])


def main_mint():
    flag = True
    while flag:
        with open("all_keys.txt", "r") as file:
            all_keys = [key.rstrip('\n') for key in file]
        with open("all_keys_minted.txt", "r") as file:
            all_keys_minted = [key.rstrip('\n') for key in file]

        for private_key in all_keys:
            try:
                mm()
                privateer(private_key)
                loginmint()
                minting()
                with open("all_keys_minted.txt", "a") as file:
                    file.writelines(private_key + '\n')
                all_keys = list(set(all_keys) - set(all_keys_minted))
                with open("all_keys.txt", "w") as file:
                    file.writelines(key + '\n' for key in all_keys)


            except Exception as e:
                print(e)
                continue
       # flag = False



main_mint()