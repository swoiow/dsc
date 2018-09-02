#!/bin/sh

install_bbr(){
# https://www.vultr.com/docs/how-to-deploy-google-bbr-on-centos-7

echo "Install the ELRepo repo"
sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm

echo "Install the 4.9.0 kernel using the ELRepo repo"
sudo yum --enablerepo=elrepo-kernel install kernel-ml -y

echo "Confirm installed result"
rpm -qa | grep kernel

echo "Show all entries in the grub2 menu"
sudo egrep ^menuentry /etc/grub2.cfg | cut -f 2 -d \'

echo "set the default boot entry as 0"
sudo grub2-set-default 0

echo "Reboot the system"
sudo shutdown -r now
}

enable_bbr(){
echo 'net.core.default_qdisc=fq' | sudo tee -a /etc/sysctl.d/bbr.conf
echo 'net.ipv4.tcp_congestion_control=bbr' | sudo tee -a /etc/sysctl.d/bbr.conf
sudo sysctl -p

sudo sysctl net.ipv4.tcp_available_congestion_control

sudo sysctl -n net.ipv4.tcp_congestion_control

lsmod | grep bbr
}