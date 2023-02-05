if [ "x$1" == "x" ]; then
    set $(cat version.txt)
else
    echo $1 > version.txt
fi
sed -i.bak "1 s/.*/__version__ = \"$1\"/" src/cimport/__init__.py
sed -i.bak "7 s/.*/version = \"$1\"/" pyproject.toml
rm -rf dist
python -m build
yes | pip uninstall cimport
pip install dist/*.whl