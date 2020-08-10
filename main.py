from dependencies import keyboard
from time import sleep

print("Program running...")

with open('commands.txt', 'r') as file:
   data = file.read()
   commandInputs = data.split('\n')
   commands = []
   keys = []
   for commandInput in commandInputs:
      command, key = commandInput.split('$$')

      command = command.replace('command=(', '')
      command = command.replace(')', '')

      key = key.replace('key=(', '')
      key = key.replace(')', '')
      commands.append(command)
      keys.append(key)

while True:
   if keyboard.is_pressed('ctrl + p'):
      break

   # comando padrão para abrir terminal
   if keyboard.is_pressed('f3 + f3'):
      keyboard.press_and_release('windows + r')
      sleep(0.1)
      keyboard.press_and_release('enter')
      sleep(1)

   if len(keys) > 0 and keyboard.is_pressed(keys[0]):
      keyboard.write(commands[0])
      sleep(0.1)
      keyboard.press_and_release('enter')

   if len(keys) > 1 and keyboard.is_pressed(keys[1]):
      keyboard.write(commands[1])
      sleep(0.1)
      keyboard.press_and_release('enter')

   if len(keys) > 2 and keyboard.is_pressed(keys[2]):
      keyboard.write(commands[2])
      keyboard.press_and_release('enter')