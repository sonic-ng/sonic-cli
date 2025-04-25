# sonic-cli
SONiC-NG Command line utilities

## Install CrossDB Python Driver
```bash
git clone https://github.com/crossdb-org/crossdb-python.git
cd crossdb-python
sudo ./setup install
```

## Steps

* Start `SysDB` first

* Load auto completion
```bash
source complete.sh
```

* use `show` or `config`
```cli
show interfaces description
Interface    admin      speed
-----------  -------  -------
Ethernet0    down       10000
Ethernet2    down       10000
Ethernet4    down       10000
```

<!--
```bash
_SHOW_COMPLETE=source show > complete.sh
_CONFIG_COMPLETE=source config >> complete.sh
source complete.sh

```
-->
