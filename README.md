# abc

一个使用 Python（Flask）实现的简单网页计算器。

## 功能
- 网页输入算术表达式并计算结果
- 支持 `+ - * / % **` 与括号
- 对非法输入给出错误提示

## 运行方式
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## 直接运行核心程序
```bash
python calculator_core.py "1 + 2 * (3 - 1)"
```

## 测试
```bash
python -m unittest discover -s tests
```

浏览器访问：`http://127.0.0.1:5000`
