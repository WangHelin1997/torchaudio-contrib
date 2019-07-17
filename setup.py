from setuptools import setup

setup(name='torchaudio_contrib',
      version='0.1',
      description='To propose audio processing Pytorch codes with nice and easy-to-use APIs and functionality',
      url='https://github.com/WangHelin1997/torchaudio-contrib',
      author='Helin Wang',
      author_email='925799764@qq.com',
      license='MIT',
      install_requires=['torch'],
      extras_require={'tests': ['pytest', 'librosa']},
      packages=['torchaudio_contrib'],
      zip_safe=False)
