from adapters.amazon_native import AmazonNativeProvider
from adapters.h10_provider import H10ProviderNotConfigured


def test_h10_is_explicitly_unconfigured():
    health = H10ProviderNotConfigured().health()
    assert health["status"] == "NOT_CONFIGURED"
    assert health["paid_dependency"] is True


def test_amazon_native_is_available_without_paid_provider():
    health = AmazonNativeProvider().health()
    assert health["status"] == "READY_FOR_BROWSER_INPUT"
    assert health["paid_dependency"] is False
