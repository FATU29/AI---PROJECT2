from setuptools import setup, find_packages

setup(
    name='heart_disease_analysis',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for analyzing heart disease data using machine learning techniques.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn==1.3.2',
        'pandas>=1.5.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)