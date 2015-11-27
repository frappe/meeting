# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='meeting',
    version=version,
    description='Prepare agenda, invite users and record minutes of a meeting',
    author='Frappé',
    author_email='hello@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
