from netmiko import ConnectHandler

device ={'ip': '192.168.181.21',
         'username': 'student',
         'password': 'L1nux_dc',
         'device_type': 'cisco_nxos'}

with ConnectHandler(**device) as session:

    print(f'Verbunden mit {device["ip"]}!')
    session.send_config_from_file('vlans_switchports.txt')
    print('Abgeschlossen')
