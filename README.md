# README

## JavaScript

### scan

主脚本

在home上运行无参数scan，会自行寻找code contract（弹窗提示），获得节点权限，运行脚本黑内存大于0的节点，内存小于等于的8的节点会运行分享（增加faction里hacking contract的reputation收入）

参数建议用1，即```run scan.js 1```，强制刷新所有节点的脚本，并为内存为0的节点购买大小1024G的服务器黑它。

### share_count

显示share后的hacking contract加成比例

### find

寻找某个节点，并打印路径

### get

从本地服务器```http://127.0.0.1:8080/```上更新script文件夹里的所有脚本

## python

code contract的解题代码，Python 3.9.5可用