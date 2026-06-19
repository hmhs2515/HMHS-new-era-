"""
HMHS Era Setup Configuration
Install: pip install -e .
"""

from setuptools import setup, find_packages

setup(
    name="hmhs-era",
    version="1.0.0",
    description="HMHS Era - Zero-API Local AI Framework for Edge Deployment",
    author="HMHS Team",
    author_email="team@hmhs.local",
    url="https://github.com/hmhs2515/HMHS-new-era-",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "llama-cpp-python>=0.2.77",
        "chromadb>=0.5.0",
        "sentence-transformers>=3.0.1",
        "playwright>=1.44.0",
        "pytest>=8.2.0",
        "flake8>=7.0.0",
    ],
    extras_require={
        "dev": [
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "isort>=5.13.2",
            "mypy>=1.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "hmhs-era=main:main",
        ],
    },
    keywords=[
        "ai",
        "local-first",
        "edge-computing",
        "privacy",
        "zero-api",
        "air-gapped",
        "decentralized",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
