from gpiozero import CPUTemperature

cpu = CPUTemperature(min_temp=50, max_temp=90)
print(str(cpu[-6:-1]))
print(str(cpu))
