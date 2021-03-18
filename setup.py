import setuptools

setuptools.setup(
    name="pipeline_sdk",
    version="0.0.1",
    author="An Phan",
    description="Arimo Pipeline SDK",
    url="https://github.com/phanhongan/aws-cli-yaml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': 'pipeline=sdk.pipeline'
    },
    python_requires='>=3.6',
)
