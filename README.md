# SDS011 PM2.5空氣檢測

### 注意事項

1.問題：

pip install serial 程式若無法執行

解決辦法：
```python
pip uninstall serial
```
```python
pip install pyserial
```

python3建議先pip install pyserial

2.問題：

serial.serialutil.SerialException:系統找不到指定的檔案。

解決辦法：

PORT請先到裝置管理員的連接埠(COM和LPT)

![image](C:\Users\Tibame\Desktop\air_PM2.5\air_PM2.5\1637160100535.jpg)


3.問題：

連接埠(COM和LPT)找不到，且USB serial 找不到驅動程式

解決辦法：

SDS011插入USB孔後，到以下連結選取該作業系統並下載和安裝

[驅動程式下載](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)













