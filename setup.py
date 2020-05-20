#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name = "ju-jump",
    packages = setuptools.find_packages(),
    data_files = [
        ("lib/ju-jump", ["shell/ju-jump.sh"])
    ],
    entry_points = {
        "console_scripts": ["ju-jump-backend=jujumpbackend.backend:main"]
    }
)
