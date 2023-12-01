""" setup """

import io

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()

# 版本号.修改号.修复号
VERSION = "1.0.1"

# This call to setup() does all the work
setup(
    name="chat-terminal",
    version=VERSION,
    description="一个在terminal中使用的chatgpt 支持 markdown显示 和上下文回答",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/TownsendWu/chat-terminal",
    author="Townsend",
    author_email="wtsai20200206@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["app"],
    include_package_data=True,
    install_requires=[
        "rich>=13.5.2",
        "requests>=2.28.2"
    ],
    entry_points={
        "console_scripts": [
            "chat-terminal=app.__main__:main",
        ]
    },
)