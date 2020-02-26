# alfred-pangu-workflow [下载链接](https://github.com/DeppWang/alfred-pangu-workflow/releases/download/v1.1/pangu.alfredworkflow)

![盘古之白](https://tva1.sinaimg.cn/large/006y8mN6ly1g95xl43qg2j303l03lq2v.jpg)



## 前言

在使用 [alfred-clipboard-ocr](https://github.com/oott123/alfred-clipboard-ocr) 的过程中，ocr 识别的文字排版不美观，每次都要手动添加空格，想着利用 Workflow 「一步到位」，所以写了这个简单的 Workflow。

## 简介

排版剪贴板文字，加上合适的空格，如：中文与英文、数字之间加上空格。

## 使用方法

复制到剪贴板后，打开 Alfred，输入 `pangu` 关键字，回车。格式后的文本会复制到剪贴板中，此时直接 Ctrl+V 粘贴即可。

## 示例

![](https://deppwang.oss-cn-beijing.aliyuncs.com/blog/2020-02-25-150558.png)

## 排版

- [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)
- [為什麼你們就是不能加個空格呢？](https://github.com/vinta/pangu.js)

## 拓展

[alfred-clipboard-ocr](https://github.com/oott123/alfred-clipboard-ocr) 是一个对剪贴板中的图片内容调用百度云 API 做 OCR 识别的 Alfred 工作流。对于不能选择复制的文字，可利用截屏后 OCR 识别，大大提高生产力。可在 alfred-clipboard-ocr 工作流中，加入 alfred-pangu-workflow 的脚本。

![image-20191121203616998](https://tva1.sinaimg.cn/large/006y8mN6ly1g95xwd8pbsj313608y77v.jpg)