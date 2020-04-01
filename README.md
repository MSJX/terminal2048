# terminal2048

一个可以在**Windows（PowerShell）、Linux**下运行的小游戏

##### 如何使用

```
git clone https://github.com/MSJX/terminal2048
cd terminal2048
python setup.py install
```

##### 开始游戏

可以根据自己在**setup.py**中设置**entry_points**中的**console_scripts**参数情况而定，如

```
terminal2048
```

或者可以直接调用**ui.py**中的**start_game**直接开始游戏