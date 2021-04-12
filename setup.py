import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="virtualsketch",
    version="0.0.1",
    author="Akash.A",
    author_email="akashcse2000@gmail.com",
    description="Sketch by hand moments with rgb colours.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Akash-Peace',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    py_modules=["virtualsketch"],
    package_dir={'':'virtualsketch'},
    install_requires=['opencv-python', 'numpy']
)