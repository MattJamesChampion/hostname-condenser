from unittest import TestCase

from hostname_condenser import get_default_top_level_domains

class TestHostnameCondenser(TestCase):
    def test_get_default_top_level_domains_returns_results(self):
        top_level_domains = get_default_top_level_domains()
        
        self.assertNotEqual(top_level_domains, None)
