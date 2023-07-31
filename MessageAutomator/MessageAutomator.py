"""
import pyautogui
import time

number_of_messages = int(input('Enter number of messages: '))
message_content = input('Enter message content: ')

time.sleep(5)

for num in range(number_of_messages):
    time.sleep(3)
    pyautogui.write(message_content)
    time.sleep(3)
    pyautogui.press('enter')

print('Script executed successfully')
"""
import pyautogui
import time
    
number_of_messages = int(input('Enter number of messages you want to sent: '))
message_content = input('Enter message content: ')
try:
    time_interval_hours = float(input("Enter the time interval between messages ( Also you can skip it ) in hour: "))
except ValueError:
     time_interval_hours = 0.0
try:
    one_massage_dealy = int(input("Enter delay time after one massage: "))
except ValueError:
    one_message_delay = 2

time.sleep(10)



time.sleep(time_interval_hours * 3600)


for num in range(number_of_messages):
    time.sleep(1)
    pyautogui.write(message_content)
    time.sleep(one_massage_dealy)
    pyautogui.press('enter')
    print('Successfully sent {} messages.'.format(num))

