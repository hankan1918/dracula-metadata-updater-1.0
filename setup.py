from setuptools import setup

setup(
    name="dracula-metadata-update",
    version="1.1.6",
    py_modules=["dracula"],
    install_requires=[
        "mutagen",
    ],
    entry_points={
        'console_scripts':[
            'dracula=dracula:main',
        ],
    },
    author="Hankan1918",
    description="A script to update metadata of 뮤지컬 드라큘라(Dracula) OST 〈10TH ANNIVERSARY CAST RECORDING〉",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)