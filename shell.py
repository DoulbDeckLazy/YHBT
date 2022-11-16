import Basic
import datetime
import platform
import time
import winreg

my_system = platform.uname()
current_time = datetime.datetime.now()
time1 = current_time
print(f"YHBT 1.0-beta ({current_time}) Running on {my_system.machine}")
print("Am I Loading? YES I AM!")
time.sleep(2)


while True:
	text = input('YHBT ~> ')
	if text.strip() == "": continue
	result, error = Basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
