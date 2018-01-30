from unittest import TestCase

from hostname_condenser import (get_top_level_domains,
                                TLDProcessingError,
                                get_default_top_level_domains,
                                condense_hostname)

class TestHostnameCondenser(TestCase):
    def test_get_top_level_domains_returns_expected_results(self):
        file_path = r"tests\test_data\example_tlds.txt"
        actual_top_level_domains = get_top_level_domains(file_path)
        
        expected_top_level_domains = ["test", "tld", "other", "words"]
        
        self.assertEqual(expected_top_level_domains, actual_top_level_domains)
    
    def test_get_top_level_domains_throws_TLDProcessingError_for_missing_file(self):
        file_path = r"this_file_does_not_exist.txt"
        
        with self.assertRaises(TLDProcessingError):
            get_top_level_domains(file_path)
    
    def test_get_default_top_level_domains_returns_results(self):
        top_level_domains = get_default_top_level_domains()
        
        self.assertNotEqual(top_level_domains, None)

    def test_condense_hostname_returns_expected_results(self):
        hostname_result_tuples = [
            ("badger", ["badg.er"]),
            ("boat", ["bo.at"]),
            ("pencil", ["penc.il"]),
            ("grandad", ["gran.dad", "grand.ad"]),
        ]
        
        for hostname_result_tuple in hostname_result_tuples:
            actual_hostname, expected_results = hostname_result_tuple
            
            with self.subTest(actual_hostname=actual_hostname):
                actual_results = condense_hostname(actual_hostname)
                self.assertEqual(expected_results, actual_results)

    def test_condense_hostname_with_custom_tlds_returns_expected_results(self):
        hostname_result_tuples = [
            ("water", ("r", "er", "ter"), ["wa.ter", "wat.er", "wate.r"]),
            ("pilot", ("ot", "ilot"), ["p.ilot", "pil.ot"])
        ]
        
        for hostname_result_tuple in hostname_result_tuples:
            actual_hostname, top_level_domains, expected_results = hostname_result_tuple
            
            with self.subTest(actual_hostname=actual_hostname):
                actual_results = condense_hostname(actual_hostname, top_level_domains)
                self.assertEqual(expected_results, actual_results)
