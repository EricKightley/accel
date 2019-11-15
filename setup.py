from setuptools import setup, Extension

extension = Extension("_core", ["accel/_core.c", ])

setup(
    ext_modules=[extension]
)
