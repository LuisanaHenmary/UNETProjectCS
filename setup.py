from distutils.core import setup
import py2exe


setup(
    options = {'py2exe': {'bundle_files': 1}},
    zipfile = None,
    windows=[{
        "script": "main.py",
        "icon_resources": [(1, "images/south.ico")],
        "dest_base":"myprogram"
    }],
    data_files=[
        ("images", [
            "images/south.ico",
            "images/SimbSur.jpeg"
        ])
    ],
    packages=[
        'views',
        "images",
        "myvenv",
        "styles",
        "components"
    ]
)
