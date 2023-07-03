import re

pattern = re.compile(r'16\'d(\d+)')
def replace_number(match,bits):
	decimal_value = int(match.group(1))
	return f"{bits}'d{decimal_value//(2**(16 - bits))}"

with open(r'C:\Users\AmirHasan\Desktop\DSDProject\cnn_open\src\lenet_roms.v', 'r') as file:
	verilog_code = file.read()

new_verilog_code = re.sub(pattern, lambda x :replace_number(x,15), verilog_code)

with open('lenet_roms_15bit.v', 'w') as file:
	file.write(new_verilog_code)
