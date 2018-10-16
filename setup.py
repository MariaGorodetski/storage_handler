import os
import sys
from setuptools import setup, Command


_python = 'python%d' % sys.version_info.major


class _TestCommand(Command):
    user_options = [
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        run_str = "%s -m unittest discover test *test.py" % _python
        os.system(run_str)


setup(
    name='storage_handler',
    version='0.1.0',
    author='Asaf Nachshon',
    author_email='asaf.nachshon@daytwo.com',
    url='https://github.com/asafnachshon/storage_handler',
    packages=[
        'storage_handler'
    ],
    entry_points={
        'console_scripts': [
            'bucket_object_upload = storage_handler.__utils_main__:object_upload'
            'bucket_object_download = storage_handler.__utils_main__:object_download'
            'bucket_object_list = storage_handler.__utils_main__:list_objects'
        ]
    },
    license='bsd',
    description='Actions on objects in an existing bucket',
    long_description=open('docs/README.rst').read(),
    install_requires=[],
    zip_safe=False,
    package_data={},
    include_package_data=True,
    cmdclass={
        'test': _TestCommand,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)