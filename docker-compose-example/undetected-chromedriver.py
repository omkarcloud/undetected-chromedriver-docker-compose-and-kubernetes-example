import undetected_chromedriver.v2 as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_element_or_none(driver, xpath, wait=None):
    try:
        if wait is None:
            return driver.find_element(By.XPATH, xpath)
        else:
            return WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        return None


def run():
    print("Welcome to game of Tom and Jerry. Here Cloudflare is the cat, Jerry is the Programmer. Our Goal as a good Jerry is to trick Cloudflare.")

    options = uc.ChromeOptions()
    options.arguments.extend(
        ["--no-sandbox", "--disable-setuid-sandbox"])
    print("Creating Driver...")
    driver = uc.Chrome(
        options=options
    )
    print("Created Driver...")

    driver.get('https://nowsecure.nl')

    element = get_element_or_none(driver, "/html/body/div[2]/div/main/h1", 20)
    if element is not None:
        print("We defeated Cloudflare, 🎉🥳 :)")
    else:
        print("Cloudflare defeated us :(, No woory we will try again. ")
    driver.quit()


if __name__ == "__main__":
    run()
