supported=['lights off', 'lock the door', 'open door', 'make coffe', 'shut down']
print(supported)
home=input('what to do: ')
if 'lights off' in home:
    print('ok')
elif 'lock the door'in home:
    print('ok')
elif 'open door'in home:
    print('ok')
elif 'make coffe'in home:
    print('ok')
elif 'shut down'in home:
    print('ok')

else:
    print('unknown')