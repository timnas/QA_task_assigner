import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def send_skype_message(assignments, chat_name="Studio Only!"):
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open Skype Web
        driver.get("https://web.skype.com/")
        time.sleep(10)  # Give time for the page to load

        # Allow user to manually log in
        input("Please log in to Skype and press Enter to continue...")

        # Search for the chat
        search_box = driver.find_element(By.XPATH, "//input[@type='search']")
        search_box.send_keys(chat_name + Keys.RETURN)
        time.sleep(5)

        # Select the chat
        chat = driver.find_element(By.XPATH, f"//span[text()='{chat_name}']")
        chat.click()
        time.sleep(5)

        # Format the message
        message = "Today's QA Assignments:\n\n" + "\n".join(assignments)

        # Send the message
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        message_box.send_keys(message + Keys.RETURN)

        print("Message sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Keep the browser open after sending the message
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == "__main__":
    # Load assignments from command-line arguments
    assignments = json.loads(sys.argv[1]) if len(sys.argv) > 1 else []
    send_skype_message(assignments)
