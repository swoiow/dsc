#!/usr/bin/env bash

setCommonUser(){
echo "新建用户 abc"
useradd -d /home/abc -m abc
passwd abc
}

setHKTime(){
echo "使用 HK 时间"
localectl set-locale LANG=zh_CN.UTF8
cp -f /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
}

setSSHConfig(){
cp /etc/ssh/sshd_config /etc/ssh/sshd_config_bak

echo "从 GitHub 下载配置"
curl -sL -o /etc/ssh/sshd_config https://github.com/swoiow/dsc/raw/master/config-ssh/sshd_config

#echo "禁用root"
#sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config

# echo "禁止使用密码登陆"
# sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
# sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config

echo "禁止空密码登陆"
sed -i 's/PermitEmptyPasswords yes/PermitEmptyPasswords no/g' /etc/ssh/sshd_config

echo "禁用基于主机的身份验证"
sed -i 's/#HostbasedAuthentication no/HostbasedAuthentication no/g' /etc/ssh/sshd_config

echo "改ssh端口"
sed -i 's/#Port define/Port 12345/g' /etc/ssh/sshd_config
firewall-cmd --zone=public --add-port=12345/tcp --permanent

echo "重启 SSH 服务"
service sshd restart
}

setSysConf(){
cp /etc/sysctl.conf /etc/sysctl.conf_bak

echo "开路由转发"
# sed -i 's/net.ipv4.ip_forward=0/net.ipv4.ip_forward=1/g' /etc/sysctl.d/ip_forward.conf
cat > /etc/sysctl.conf << EOF
net.ipv4.ip_forward = 1
net.ipv4.tcp_fastopen = 3
EOF

echo "增加系统文件描述符的最大限数"
cat >> /etc/security/limits.conf << EOF
* soft nofile 51200
* hard nofile 51200
EOF

echo "ulimit 指令优化"
ulimit -n 51200
}

kernelOptimize(){
echo "调整内核参数"
cat > /etc/sysctl.d/98-shadowsocks.conf << EOF
fs.file-max = 51200
net.core.rmem_max = 67108864
net.core.wmem_max = 67108864
net.core.netdev_max_backlog = 250000
net.core.somaxconn = 4096
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 0
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.ip_local_port_range = 10000 65000
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_max_tw_buckets = 5000
net.ipv4.tcp_fastopen = 3
net.ipv4.tcp_rmem = 4096 87380 67108864
net.ipv4.tcp_wmem = 4096 65536 67108864
net.ipv4.tcp_mtu_probing = 1
net.ipv4.tcp_congestion_control = hybla
EOF

echo " 执行调整内核"
sysctl -p /etc/sysctl.d/98-shadowsocks.conf
}

addSwap(){
echo "增加交换区至 4G"
swapon -s
dd if=/dev/zero of=/swapfile count=4096 bs=1M
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile   none    swap    sw    0   0' >> /etc/fstab
}

setDNS(){
echo "修改DNS"
cat > /etc/resolv.conf << EOF
nameserver 1.1.1.1
nameserver 8.8.8.8
EOF
}

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

#echo "Reboot the system"
#sudo shutdown -r now
}

enable_bbr(){
echo 'net.core.default_qdisc=fq' | sudo tee -a /etc/sysctl.d/99-bbr.conf
echo 'net.ipv4.tcp_congestion_control=bbr' | sudo tee -a /etc/sysctl.d/99-bbr.conf
sudo sysctl -p

sudo sysctl net.ipv4.tcp_available_congestion_control

sudo sysctl -n net.ipv4.tcp_congestion_control

lsmod | grep bbr
}

yum update -y

setHKTime
setSSHConfig
setDNS
install_bbr
enable_bbr
setSysConf
kernelOptimize
addSwap

shutdown -r now
