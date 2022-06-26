from setuptools import find_packages, setup

setup(
    name='bytesep',
    version='0.1.1',
    description='Music source separation',
    author='ByteDance',
    url="https://github.com/bytedance/music_source_separation",
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch',
        'librosa==0.8.0',
        'museval',
        'h5py',
        'pytorch_lightning',
        'numpy',
        'torchlibrosa==0.0.9',
        'matplotlib',
        'musdb',
        'museval',
        'samplerate'
    ],
    zip_safe=False
)
