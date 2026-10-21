"""Exabeam New-Scale OAuth provider using client credentials flow."""

from typing import ClassVar

from tracecat.integrations.providers.base import ClientCredentialsOAuthProvider
from tracecat.integrations.schemas import ProviderMetadata, ProviderScopes

EXABEAM_TOKEN_DOCS_URL = (
    "https://developers.exabeam.com/exabeam/reference/get-access-token"
)
EXABEAM_API_DOCS_URL = "https://developers.exabeam.com/exabeam/reference"
EXABEAM_SETUP_GUIDE_URL = "https://developers.exabeam.com/exabeam/docs/api-keys"
EXABEAM_TOKEN_ENDPOINT = "https://api.{region}.exabeam.cloud/auth/v1/token"


class ExabeamOAuthProvider(ClientCredentialsOAuthProvider):
    """Exabeam OAuth provider using an API key and secret (client credentials)."""

    id: ClassVar[str] = "exabeam"
    scopes: ClassVar[ProviderScopes] = ProviderScopes(default=[])
    metadata: ClassVar[ProviderMetadata] = ProviderMetadata(
        id="exabeam",
        name="Exabeam",
        description=(
            "Exabeam New-Scale OAuth provider using an API key and secret "
            "(client credentials)."
        ),
        requires_config=True,
        enabled=True,
        api_docs_url=EXABEAM_API_DOCS_URL,
        setup_guide_url=EXABEAM_SETUP_GUIDE_URL,
        troubleshooting_url=EXABEAM_TOKEN_DOCS_URL,
    )
    # Exabeam only implements the client credentials grant, so there is no
    # consent URL. The base provider requires both endpoints to be set, so this
    # mirrors the token endpoint and is never used to start a consent flow.
    default_authorization_endpoint: ClassVar[str | None] = EXABEAM_TOKEN_ENDPOINT
    default_token_endpoint: ClassVar[str | None] = EXABEAM_TOKEN_ENDPOINT
    authorization_endpoint_help: ClassVar[str | list[str] | None] = [
        "Unused. Exabeam only supports the client credentials grant, so this "
        "endpoint is never called; leave it matching the token endpoint.",
    ]
    token_endpoint_help: ClassVar[str | list[str] | None] = [
        "Replace {region} with your Exabeam API region, for example:",
        "https://api.us-west.exabeam.cloud/auth/v1/token",
        "\n",
        "Regions: us-west, us-east, ca, eu, uk, ch, sg, jp, au, sa. Create the "
        "API key and secret under Settings > API Keys; this requires an "
        "administrator with full access to the Exabeam subscription.",
    ]
