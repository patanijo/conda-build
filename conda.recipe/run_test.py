import pytest
import conda_build

print('conda_build.__version__: %s' % conda_build.__version__)
pytest.main(['tests'])
