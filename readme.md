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

8.   

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

