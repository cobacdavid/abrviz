from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='abrviz',
    version='0.2',
    description='Visualisation Arbre Binaire de Recherche',
    long_description_content_type='text/markdown',
    long_description=long_description,
    # url='https://twitter.com/david_cobac',
    url="https://github.com/cobacdavid/abrviz",
    author='David COBAC',
    author_email='david.cobac@gmail.com',
    license='CC-BY-NC-SA',
    keywords=['bst', 'abr', 'sort',
              'tri', 'tree', 'arbre'],
    packages=find_packages(),
    install_requires=["graphviz"],
    python_requires='>3.5'
)
