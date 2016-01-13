The app is designed to deployed via [uwsgi](http://uwsgi-docs.readthedocs.org/en/latest/index.html). Install uwsgi via `sudo pip install uwsgi` and NEVER try
`apt-get install uwsgi`.

There are several config files:
- `ng-farm.ini` is for uwsgi. You can run `uwsgi --ini ng-farm.ini` to start. With this file, 
it's easier to configure uwsgi as `Upstart` or `Systemd`
- `ng-farm.conf` is for `Upstart` which is enabled on Ubuntu 14.10 and prior by default. 
Copy it to `/etc/init/` and run `service ng-farm start` to start it
- `ng-farm.service` is for `Systemd` which is enabled by default since Ubuntu 15.10 on which Upstart not installed.


[Read more](https://wiki.ubuntu.com/SystemdForUpstartUsers) about `Upstart` and `SystemD`.
