# Wallpaper_Spider

## 一、项目介绍
这个项目是一个python的爬虫，它能够爬取wallhaven.cc网站上的壁纸。项目中一共有两个爬虫，他们分别是base_Wallpaper_Spider和auto_Wallpaper_Spider。
## 二、base_Wallpaper_Spider
base_Wallpaper_Spider是这个爬虫项目的母体，为普通用户量身打造，它提供了这个爬虫的基础功能。
### base_Wallpaper_Spider一共有3种模式供用户选择，分别是：
 1. 爬取wallhaven.cc网站的最新壁纸（Latest），默认一次爬取数量为48张
 2. 爬取wallhaven.cc网站的最热壁纸（Toplist），默认一次爬取数量为48张
 3. 爬取wallhaven.cc网站的随机壁纸（Random），默认一次爬取数量为48张
图片的默认储存位置为项目目录的Wallpapers目录，图片皆以数字编号。

base_Wallpaper_Spider的稳定版本发布于分支master中，开发版本发布于分支base_Wallpaper_Spider中。
## 三、auto_Wallpaper_Spider
auto_Wallpaper_Spider是base_Wallpaper_Spider的变体爬虫。一些用户可能需要一次性爬取大量不同种类和尺寸的壁纸，auto_Wallpaper_Spider就是由此而生。
与母体相比，auto_Wallpaper_Spider更像一个一个全自动爬取壁纸的脚本，它的原理是先去第三方代理网站爬取开放的免费代理，然后再通过这些代理伪装自己的本地ip，
从而绕过服务器监控，实现壁纸的大量爬取。

使用实例：
将auto_Wallpaper_Spider部署到阿里云轻量级云服务器上，然后在服务器面板中设置爬虫脚本定时启动，每天定时爬取网站壁纸。

auto_Wallpaper_Spider发布于分支auto_Wallpaper_Spider中。

## 最后
Wallpaper_Spider仅供个人学习和练习使用，如果利用Wallpaper_Spider大量盗取wallhaven.cc网站的壁纸数据，后果自负。
