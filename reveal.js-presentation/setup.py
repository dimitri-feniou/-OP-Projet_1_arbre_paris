import setuptools

setuptools.setup(
    name="openclassrooms-projet-1-arbre-paris-presentation",
    version="0.2.0",
    author="Feniou Dimitri",
    author_email="",
    description="Présentation Openclassrooms Projet 2 Analyse Arbre Paris",
    long_description="create and add reveal.js HTML presentations to your streamlit app",
    long_description_content_type="text/plain",
    url="https://github.com/dimitri-feniou/-OP-Projet_1_arbre_paris",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)