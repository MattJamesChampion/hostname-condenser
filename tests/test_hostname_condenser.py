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
        input_output_tuples = [
            ("badger", ["badg.er"]),
            ("boat", ["bo.at"]),
            ("pencil", ["penc.il"]),
            ("grandad", ["grand.ad", "gran.dad"]),
        ]
        
        for input_output_tuple in input_output_tuples:
            actual_input, expected_output = input_output_tuple
            
            with self.subTest(input=input):
                actual_output = condense_hostname(actual_input)

            self.assertEqual(expected_output, actual_output)
