## sshd_config

> [openssh-portable/sshd_config][1]

## docs

```
https://firewalld.org/2015/12/ipset-support

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-setting_and_controlling_ip_sets_using_firewalld
```


## ssh security

```
firewall-cmd --permanent --new-ipset=whitelist --type=hash:net

firewall-cmd --permanent --ipset=whitelist --add-entries-from-file=./ChinaIP/ChinaIP_xx.txt

firewall-cmd --permanent --new-zone=fwssh
firewall-cmd --permanent --zone=fwssh --set-target=DROP
firewall-cmd --permanent --zone=fwssh --add-service=ssh
firewall-cmd --permanent --zone=public --add-source=ipset:whitelist

# firewall-cmd --permanent --zone=trusted --add-service=ssh 
# firewall-cmd --permanent --zone=trusted --add-source=ipset:whitelist
# firewall-cmd --permanent --zone=public --remove-service=ssh
```

[1]: https://github.com/openssh/openssh-portable/blob/master/sshd_config
