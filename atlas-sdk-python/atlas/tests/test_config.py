import pytest

from atlas.config import AtlasConfig

def test_config_uses_defualt_values():
    config = AtlasConfig(
        api_key="atlas_test_key"
    )

    assert config.api_key== "atlas_test_key"
    assert config.base_url == "http://api.atlas.example/v1"
    assert config.timeout == 30.0


def test_config_accepts_custom_values():
    config= AtlasConfig(
        api_key="atlas_test_key",
        base_url="http://localhost:8000/v1",
        timeout=10.0,
    )

    assert config.base_url == "http://localhost:8000/v1"
    assert config.timeout == 10.0
    
    @pytest.mark.parametrize("api_key", ["", " ", "\t", "\n"])
    def test_config_rejects_empty_api_key(api_key: str):
        with pytest.raises(ValueError, match="api_key must not be empty"):
            AtlasConfig(api_key=api_key)

    @pytest.mark.parametrize("timeout", [0, -1, -0.1])
    def test_config_rejects_invalid_timeout(timeout: float):
        with pytest.raises(ValueError, match="timeout must be greater than zero"):
            AtlasConfig(
                api_key="atlas_test_key",
                timeout=timeout,
            )    