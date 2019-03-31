from distutils.core import setup
setup(
  name = 'las_to_df',
  packages = ['las_to_df'],
  version = '1.0',
  license='MIT',
  description = 'This function takes in your individual las files and transforms it into a dataframe. It also give you the list of files that cannot be converted',
  author = 'AISHAHELENA',
  author_email = 'aishahelena.sharif@gmail.com',
  url = 'https://github.com/AISHAHELENA/las_to_df',
  download_url = 'https://github.com/AISHAHELENA/las_to_df/archive/V0.1.tar.gz',
  keywords = ['LAS', 'OIL', 'GAS', 'WELL', 'WELL LOGS', 'PETROLEUM'],
  install_requires=[
          'os',
          'lasio',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',
  ],
)
