from conda_build import api

from .utils import testing_workdir, test_config, test_metadata


def test_output_with_noarch_says_noarch(test_metadata):
    test_metadata.meta['noarch'] = 'python'
    output = api.get_output_file_path(test_metadata)
    assert 'noarch' in output


def test_output_with_noarch_python_says_noarch(test_metadata):
    test_metadata.meta['noarch_python'] = True
    output = api.get_output_file_path(test_metadata)
    assert 'noarch' in output


# no tests here - this is tested at a high level in test_cli.py and in test_api_render.py.
#   tests here should be lower-level unit tests of the render.py functionality.
