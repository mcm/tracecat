"""Pure unit tests for the Exabeam OAuth provider."""

from tracecat.integrations.enums import OAuthGrantType
from tracecat.integrations.providers import PROVIDER_REGISTRY
from tracecat.integrations.providers.exabeam.oauth import ExabeamOAuthProvider
from tracecat.integrations.schemas import ProviderKey


def test_exabeam_registers_client_credentials_only() -> None:
    registered = {key.grant_type for key in PROVIDER_REGISTRY if key.id == "exabeam"}
    assert registered == {OAuthGrantType.CLIENT_CREDENTIALS}
    cls = PROVIDER_REGISTRY[
        ProviderKey(id="exabeam", grant_type=OAuthGrantType.CLIENT_CREDENTIALS)
    ]
    assert cls is ExabeamOAuthProvider
    assert cls.id == cls.metadata.id == "exabeam"


def test_exabeam_accepts_a_regional_token_endpoint() -> None:
    token_endpoint = "https://api.us-west.exabeam.cloud/auth/v1/token"
    provider = ExabeamOAuthProvider(
        client_id="api-key",
        client_secret="api-secret",
        authorization_endpoint=token_endpoint,
        token_endpoint=token_endpoint,
    )

    assert provider.token_endpoint == token_endpoint
    assert provider.requested_scopes == []
