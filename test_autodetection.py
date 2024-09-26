from netmiko.ssh_autodetect import SSHDetect


device = {'ip': '192.168.181.21',
          'username': 'student',
          'password': 'L1nux_dc',
          'device_type': 'autodetect'}

guesser = SSHDetect(**device)
print(guesser.autodetect())
