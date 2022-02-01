from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


# chrome_options = webdriver.ChromeOptions
chromeoptions = Options()
chromeoptions.add_argument("--log-level=3")
driver = webdriver.Chrome(executable_path=binary_path, options=chromeoptions)

URL = 'https://mdn.github.io/todo-react-build/'

driver.get(URL)

def get_all_task():
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button[1]').click()
    all_task = driver.find_element(By.ID, 'list-heading').text
    return all_task

def add_task(task):
    driver.find_element(By.ID, 'new-todo-input').clear()
    driver.find_element(By.ID, 'new-todo-input').send_keys(task)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/button').click()

def get_current_task():
    list_heading = driver.find_element(By.ID, 'list-heading').text
    current_task = int(list_heading.split(' ')[0])
    return current_task

def get_active_task():
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button[2]').click()
    active_task = driver.find_element(By.ID, 'list-heading').text
    return active_task

def mark_task_completed(task):
    clicked_task = driver.find_elements(By.CLASS_NAME, 'todo-label')
    for elem in clicked_task:
        if elem.text == task:
            elem.click()
            break

def get_completed_task():
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/button[3]').click()
    completed_task = driver.find_element(By.ID, 'list-heading').text
    return completed_task


my_task = ['test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10']
print("*"*50)
print("Step 1: Get all current tasks")
print("All tasks before addding new task: " + str(get_current_task()))
print("*"*50)
print("Step 2: Get current active task")
print("All active before addding new task: " + str(get_active_task()))
for task in my_task:
    add_task(task)
print("*"*50)
print("Step 3: Get all tasks")
print("All tasks after adding new task: " + str(get_all_task()))
print("*"*50)
print("Step 4: Get active tasks before marking task completed")
print("All active tasks before marking task as completed: " + str(get_active_task()))
print("*"*50)
task_mark_completed = ['test4', 'test', 'test6']

for task in task_mark_completed:
    mark_task_completed(task)

print("Step 5: Get active tasks after marking task completed")
print("All active tasks after marking completed: " + get_active_task())
print("*"*50)
print("Step 6: Get completed tasks")
print("All completed tasks: " + get_completed_task())