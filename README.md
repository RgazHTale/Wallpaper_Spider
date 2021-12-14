# Wallpaper_Spider

## 一、项目介绍
这个项目是一个python的爬虫，它能够爬取wallhaven.cc网站上的壁纸。项目中一共有两个爬虫，他们分别是base_Wallpaper_Spider和auto_Wallpaper_Spider。
## 二、base_Wallpaper_Spider
base_Wallpaper_Spider是这个爬虫项目的母体，为普通用户量身打造，它提供了这个爬虫的基础功能。
### base_Wallpaper_Spider一共有3种模式供用户选择，分别是：
 1. 爬取wallhaven.cc网站的最新壁纸（Latest）
 2. 爬取wallhaven.cc网站的最热壁纸（Toplist）
 3. 爬取wallhaven.cc网站的随机壁纸（Random）
当爬取数量超过500张时，爬虫会自动启用第三方IP代理，这会稍微减慢爬取速度，图片的默认储存位置为项目目录的Wallpapers目录，图片皆以数字编号。

base_Wallpaper_Spider的稳定版本发布于分支master中，开发版本发布于分支base_Wallpaper_Spider中。
**当爬取完成之后，用户可以使用爬虫内置的图片分类系统对图片进行分类。**
内置类别为两类，分为人物和其它，也就是能够把具有人物特征的图片单独提取出来。程序中所有接口都封装完毕，开发者可以自行根据需求调整分类系统。

## 三、auto_Wallpaper_Spider
auto_Wallpaper_Spider是base_Wallpaper_Spider的全自动版本。爬虫会自动完成爬取，使用代理，分类等一系列操作。用户要做的只是启动爬虫，然后一觉醒来所有的图片都将整齐的放在你的文件夹中。

auto_Wallpaper_Spider发布于分支auto_Wallpaper_Spider中。

## 最后
Wallpaper_Spider仅供个人学习和练习使用，切勿利用Wallpaper_Spider大量盗取wallhaven.cc网站的壁纸数据。
