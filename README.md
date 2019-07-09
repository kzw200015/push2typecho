## 推送本地文章至typecho博客

#### 用法
依赖`pyyaml`  
把`config.py.example`复制一份为`config.py`，并配置好相关信息  
Markdown文件格式参考，类似`Hexo`，目前还不支持多标签
```
---
title: test
tags:  a
categories:
- b
- c
---
这是一篇测试文章
```
然后
```
python main.py <file>
```
#### To Do
- ~~将分类，标签等选项加入markdown文件进行设置，类似`hexo`~~
- 支持多标签，目前由于未知原因无法支持
- 多级分类
- 等等

**注意事项：请做好数据备份，我不为任何该脚本导致的后果负责**