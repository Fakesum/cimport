rm -rf dist
python -m build
yes | pip uninstall cimport
pip install dist/*.whl