# Wallpaper_Spider

## 一、项目介绍
这个项目是一个python的爬虫，它能够爬取wallhaven.cc网站上的壁纸，并提供ai智能分类功能。
## 二、Wallpaper_Spider
### Wallpaper_Spider一共有3种模式供用户选择，分别是：
 1. 爬取wallhaven.cc网站的最新壁纸（Latest）
 2. 爬取wallhaven.cc网站的最热壁纸（Toplist）
 3. 爬取wallhaven.cc网站的随机壁纸（Random）

当爬取数量超过500张时，爬虫会自动启用第三方IP代理，这会稍微减慢爬取速度，图片的默认储存位置为项目目录的Wallpapers目录，图片皆以数字编号。

**当爬取完成之后，用户可以使用爬虫内置的图片分类系统对图片进行分类。**
内置类别为两类，分为人物和其它，也就是能够把具有人物特征的图片单独提取出来。程序中所有接口都封装完毕，开发者可以自行根据需求调整分类系统。

## 三、最后
Wallpaper_Spider仅供个人学习和练习使用，切勿利用Wallpaper_Spider大量盗取wallhaven.cc网站的壁纸数据。
