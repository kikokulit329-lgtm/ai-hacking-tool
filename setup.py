from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-hacking-tool",
    version="1.0.0",
    author="Security Research Team",
    author_email="security@example.com",
    description="An AI-powered comprehensive ethical hacking toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kikokulit329-lgtm/ai-hacking-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=[
        "scapy>=2.5.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "tensorflow>=2.14.0",
        "scikit-learn>=1.3.1",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
    ],
    entry_points={
        "console_scripts": [
            "aihack=src.cli:main",
        ],
    },
)
