# 仓库介绍
InSAR小白的初学仓库，用于记录和整理一些关键的笔记

# 好用的博客和网站

1.   [ISCE安装教程](https://blog.csdn.net/qq_27386899/article/details/126464150)
2.   [isce2+mintpy做SBASInSAR](https://blog.csdn.net/m0_51395393/article/details/138506284)
3.   [SARScape做SBASInSAR](https://mp.weixin.qq.com/s/94X4CMheUSxUgg3Rv2l9og)
4.   [EZ-InSAR](https://mp.weixin.qq.com/s/Vkaxj1SBZsBCtyphFsSIdQ)
5.   [ISCE文件格式及其含义](https://blog.csdn.net/qq_27386899/article/details/128311011)
6.   [isce2学习（三）下载哨兵数据、POD精轨数据、DEM数据、AUX_CAL辅助文件下载](https://blog.csdn.net/QJBMFCH/article/details/124060861)
7.   [isce2拼接dem命令、使用GPU加速命令](https://blog.csdn.net/m0_60086135/article/details/124752577 )
8.   [InSAR处理及绘图常用GMT命令、bash、csh、matlab语法及样例](https://blog.csdn.net/river__C/article/details/123412334)
9.   [GMTSAR的D-InSAR基本处理过程](https://blog.csdn.net/m0_60086135/article/details/122354521)
10.   [GMTSAR官方文档](https://gmtsar.github.io/documentation/)
11.   [GMTSAR安装教程](https://github.com/gmtsar/gmtsar/wiki/)---需要管理员执行autoconf那块
12.   [在ubuntu18和20下安装GMTSAR6.1版本](https://blog.csdn.net/m0_60086135/article/details/124710336?spm=1001.2014.3001.5506)
13.   [时序InSAR技术数据处理时注意事项](https://mp.weixin.qq.com/s/_NzvH-D3i3U5Ke-sl5DUjg)
14.   [GMTSAR的D-InSAR基本处理过程](https://blog.csdn.net/m0_60086135/article/details/122354521#:~:text=GMTSAR%E7%9A%84D-InSAR%E5%9F%BA%E6%9C%AC%E5%A4%84%E7%90%86%E8%BF%87%E7%A8%8B%201%201.%E5%87%86%E5%A4%87raw%20%E6%96%87%E4%BB%B6%E5%A4%B9%20%E5%9C%A8ASF%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BD%20%E5%93%A8%E5%85%B5%20%E6%95%B0%E6%8D%AE%E5%92%8C%E5%93%A5%E7%99%BD%E5%B0%BC%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BD%E8%BD%A8%E9%81%93%E6%95%B0%E6%8D%AE%20ASF%E4%B8%8B%E8%BD%BD%E5%93%A8%E5%85%B5%E6%95%B0%E6%8D%AE%E5%AE%98%E7%BD%91,4%204.%E8%BF%90%E8%A1%8Cp2p_S1_TOPS_Frame.csh%E5%91%BD%E4%BB%A4%20%E8%BF%90%E8%A1%8C%E8%BF%99%E4%B8%AA%E5%91%BD%E4%BB%A4%E5%8D%B3%E5%8F%AF%20...%205%205.%E8%BE%93%E5%87%BA%E7%BB%93%E6%9E%9C%E4%B8%BB%E8%A6%81%E5%9C%A8merge%E6%96%87%E4%BB%B6%E5%A4%B9%20merge%E4%B8%BB%E8%A6%81%E8%BE%93%E5%87%BA%E5%A6%82%E4%B8%8B%E5%9B%BE%E7%9A%84%E6%96%87%E4%BB%B6%20)
15.   [GMTSAR资源文件](https://topex.ucsd.edu/gmtsar/tar/)
16.   [电磁波中的波段划分：L波段、S波段、C波段、X波段、Ku波段、K波段、Ka波段](https://blog.csdn.net/jbb0523/article/details/12875821)
17.   https://en.wikipedia.org/wiki/Interferometric_synthetic-aperture_radar
18.   [SAR卫星的不同成像模式](https://blog.csdn.net/qq_41341717/article/details/121480204)

# 不错的仓库

1.   [awesome-sar](https://github.com/2lambda123/awesome-sar)
2.   [isce2-doc](https://github.com/isce-framework/isce2-docs)
3.   [isce2](https://github.com/isce-framework/isce2)
4.   [mintpy](https://github.com/insarlab/MintPy)
5.   [TRAIN](https://github.com/dbekaert/TRAIN)

# 数据下载网站整理

1.   [ASF官网](https://search.asf.alaska.edu/#/?maxResults=250)
2.   [https://dataspace.copernicus.eu/](https://dataspace.copernicus.eu/)
3.   [https://step.esa.int/auxdata/dem/SRTMGL1/](https://step.esa.int/auxdata/dem/SRTMGL1/)
4.   [https://dwtkns.com/srtm30m/](https://dwtkns.com/srtm30m/)
5.   [S1A精密轨道数据](http://step.esa.int/auxdata/orbits/Sentinel-1/POEORB/S1A/)
6.   [精密轨道数据(我仓库批下载所采用的网站)](https://s1qc.asf.alaska.edu/aux_poeorb/)

# 乱七八糟的命令

1.   isce安装环境变量配置

```
# isce2 stackSentinel.py
export ISCE_STACK='/home/xytx/anaconda3/envs/isce2/share/isce2'
export PYTHONPATH=${PYTHONPATH}:${ISCE_STACK}
export PATH=${PATH}:${ISCE_STACK}/topsStack


### isce2 ###
export ISCE_HOME='/home/xytx/anaconda3/envs/isce2/lib/python3.9/site-packages/isce'
export PATH=$ISCE_HOME/bin:$ISCE_HOME/applications:$PATH
export PYTHONPATH=$ISCE_ROOT:$ISCE_HOME/applications:$ISCE_HOME/component:$PYTHONPATH
```

