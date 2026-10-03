import unittest
from risk_utils import calculate_risk, classify_risk

class TestRiskUtils(unittest.TestCase):

    def test_calculate_risk(self):
        """Test calculation across different combinations of flags."""
        # test_cases format: (reports, warnings, bans, expected_score)
        test_cases = [
            (10, 2, 1, 30),    # 10 + (2*5) + (1*10) = 30
            (50, 3, 2, 85),    # 50 + (3*5) + (2*10) = 85
            (0, 0, 0, 0),      # Minimum inputs
            (30, 12, 5, 140)   # 30 + (12*5) + (5*10) = 140
        ]

        for reports, warnings, bans, expected in test_cases:
            with self.subTest(reports=reports, warnings=warnings, bans=bans):
                result = calculate_risk(reports, warnings, bans)
                self.assertEqual(result, expected)

    def test_classify_risk(self):
        """Test classification boundaries for high, medium, and low risks."""
        # test_cases format: (score, expected_level)
        test_cases = [
            # High Risk Threshold (>= 50)
            (100, "high"),
            (50, "high"),
            
            # Medium Risk Threshold (25 to 49)
            (49, "medium"),
            (25, "medium"),
            
            # Low Risk Threshold (< 25)
            (24, "low"),
            (0, "low"),
        ]

        for score, expected_level in test_cases:
            with self.subTest(score=score):
                self.assertEqual(classify_risk(score), expected_level)


if __name__ == "__main__":
    unittest.main()