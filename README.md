# ezchat since 2021.09.01

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

