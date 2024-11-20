import setuptools

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-COMBO"

setuptools.setup(
  name="spacy_combo",
  version="0.8.1",
  description="COMBO wrapper for spaCy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="NLP COMBO spaCy",
  packages=setuptools.find_packages(),
  install_requires=[
    "spacy>=2.3.0",
    "deplacy>=2.1.0",
    "sparse>=0.10.0",
    "numpy>=1.16.2",
    "Keras>=2.2.4",
    "scikit-learn>=0.20.3",
    "tensorflow>=1.14.0",
    "joblib>=0.13.2"
  ],
  python_requires=">=3.6",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic"
  ],
  project_urls={
    "COMBO":"https://github.com/360er0/COMBO",
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
