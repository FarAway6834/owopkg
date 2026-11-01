from setuptools import setup, find_packages

setup(
    name='owopkg',
    version='0.0.3',
    description='setuptools & wheel build -> twine deployment app',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/owopkg',
    packages=find_packages(exclude=[]),
    install_requires=['subpr', 'setuptools', 'wheel', 'twine'],
    keywords=['owopkg'],
    python_requires='>=3.6',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
    ],
    entry_points = {
        "console_scripts" : [
            "owopkg=owopkg.__main__:main",
            "owopkg-build=owopkg.build:main",
            "owopkg-deploy=owopkg.deploy:main",
            "owopkg-mybwb=owopkg.mybwb:main",
            "owopkg-buildeploy=owopkg.buildeploy:main",
            "owopkg-mybwbuildeploy=owopkg.mybwbuildeploy:main"
        ]
    }
)