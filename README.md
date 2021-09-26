# ezchat since 2021.09.01
5 boot with local scripts
5-1
create /etc/rc.local
the head
#!/bin/sh

5-2
chmod +x /etc/rc.local

5-3
create /lib/systemd/system/rc-local.service

[Unit]
Description=/etc/rc.local Compatibility
Documentation=man:ywinit(8)
ConditionFileIsExecutable=/etc/rc.local

[Service]
ExecStart=/etc/rc.local start
Type=forking
TimeoutSec=0
RemainAfterExit=yes
CuessMainPID=0

[Install]
WantedBy=multi-user.target
Alias=rc-local.service

5-4 
ln -s /lib/systemd/system/rc-local.service /etc/systemd/system/rc-local.service

5-5
systemctl enable rc-local.service


4 install rabbitmq
sudo apt install -y rabbitmq-server
sudo service rabbitmq-server stop
sudo service rabbitmq-server start
sudo service rabbitmq-server restart


sudo rabbitmqctl add_user admin pwd123
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"


sudo rabbitmqctl list_users

hostname -I

web server port: 15672


3 clean project and rebuild it.

2 test it
the git push test in local server.

1 git token setup.
git remote set-url origin https://$EZ_GIT_TOKEN@github.com/ezzcs/ezchat.git
git push
git clone

