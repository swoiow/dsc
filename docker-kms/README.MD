以管理员身份打开命令提示符，然后输入以下命令：

> 如何以管理员身份打开命令提示符
1. 按 Ctrl + Shift + Esc 组合键，调出任务管理器
2. 在任务管理器中，文件 -> 运行新任务，在打开一栏输入，cmd，打勾以系统管理权限创建此任务，点击确定。

---

> 如何切换盘符
```
Microsoft Windows [版本 10.0.16299.371]
(c) 2017 Microsoft Corporation。保留所有权利。

C:\WINDOWS\system32>


上面看到，当前的盘是C盘，如何切换到D盘呢？

C:\WINDOWS\system32>d: 

输入d: 即可。


如何切换路径？

C:\WINDOWS\system32> cd 路径

提示，这里的路径，要与当前盘符(盘符：就是C D E F 盘)一致，否则，先切换盘符。
```

---

> Windows 激活命令
```
cd "%SystemRoot%\system32"
cscript /nologo slmgr.vbs /skms 你的域名或IP（如cscript /nologo slmgr.vbs /skms kms.kn007.net）
cscript /nologo slmgr.vbs /ato
cscript /nologo slmgr.vbs /xpr
```
或直接弹窗方式：
```
slmgr /skms 你的域名或IP（如slmgr /skms kms.kn007.net）
slmgr /ato
slmgr /xpr
```

---

> OFFICE 激活命令
```
cscript ospp.vbs /sethst:你的域名或IP（如cscript ospp.vbs /sethst:kms.kn007.net）
cscript ospp.vbs /act
cscript ospp.vbs /dstatus
```

##### 通过以上步骤就可以激活你的Windows系统和Office软件，但是值得注意的是，KMS方式激活的有效期只有180天，因此每不到半年需要重新激活一次。