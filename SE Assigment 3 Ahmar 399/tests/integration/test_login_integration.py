"""
Integration Tests for Login System
This module contains integration tests that verify multiple components work together.
"""

import unittest
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from login import LoginSystem


class TestLoginSystemIntegration(unittest.TestCase):
    """Integration tests for the LoginSystem."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.login_system = LoginSystem()
    
    def test_user_registration_and_login_flow(self):
        """
        Test complete user registration and login workflow.
        User registers with new credentials, then successfully logs in.
        """
        # Step 1: Register a new user
        register_result = self.login_system.add_user('integration_user', 'integ_pass123')
        self.assertTrue(register_result['success'])
        
        # Step 2: Verify user exists
        self.assertTrue(self.login_system.user_exists('integration_user'))
        
        # Step 3: Login with new user
        login_result = self.login_system.login('integration_user', 'integ_pass123')
        self.assertTrue(login_result['success'])
        self.assertEqual(login_result['user_id'], 'integration_user')
    
    def test_multiple_failed_login_attempts(self):
        """
        Test multiple failed login attempts with the same user.
        System should consistently return failure.
        """
        username = 'admin'
        wrong_password = 'wrongpass'
        
        # Attempt login 3 times with wrong password
        for attempt in range(3):
            result = self.login_system.login(username, wrong_password)
            self.assertFalse(result['success'])
            self.assertIsNone(result['user_id'])
            self.assertEqual(result['message'], 'Invalid username or password')
        
        # Verify valid login still works
        valid_result = self.login_system.login(username, 'password123')
        self.assertTrue(valid_result['success'])
    
    def test_login_after_adding_new_user(self):
        """
        Test that newly added users can immediately log in without reinitialization.
        """
        new_username = 'dynamic_user'
        new_password = 'dynamic_pass456'
        
        # Add new user
        add_result = self.login_system.add_user(new_username, new_password)
        self.assertTrue(add_result['success'])
        
        # Immediately attempt login (without reinitializing system)
        login_result = self.login_system.login(new_username, new_password)
        self.assertTrue(login_result['success'])
        self.assertEqual(login_result['user_id'], new_username)
    
    def test_case_sensitivity_in_username(self):
        """
        Test that username matching is case-sensitive.
        Login with different case should fail.
        """
        # Valid login
        valid_result = self.login_system.login('admin', 'password123')
        self.assertTrue(valid_result['success'])
        
        # Login with different case should fail
        case_result = self.login_system.login('Admin', 'password123')
        self.assertFalse(case_result['success'])
        
        case_result2 = self.login_system.login('ADMIN', 'password123')
        self.assertFalse(case_result2['success'])
    
    def test_password_verification_integrity(self):
        """
        Test that password verification is strict and doesn't allow partial matches.
        """
        username = 'user1'
        correct_password = 'pass1234'
        
        # Try passwords that are similar but incorrect
        similar_passwords = [
            'pass123',      # Missing last character
            'pass12345',    # Extra character
            'Pass1234',     # Different case
            'pass1234 ',    # Extra space
            ' pass1234',    # Leading space
        ]
        
        for wrong_pass in similar_passwords:
            result = self.login_system.login(username, wrong_pass)
            self.assertFalse(result['success'], 
                            f"Login should fail with password '{wrong_pass}'")
        
        # Correct password should work
        correct_result = self.login_system.login(username, correct_password)
        self.assertTrue(correct_result['success'])
    
    def test_special_character_password_integrity(self):
        """
        Test that special characters in passwords are preserved and verified correctly.
        """
        test_username = 'special_user'
        test_password = 'P@ssw0rd!#$%'
        
        # Add user with special character password
        self.login_system.add_user(test_username, test_password)
        
        # Login with exact special character password
        result = self.login_system.login(test_username, test_password)
        self.assertTrue(result['success'])
        
        # Login with similar but different special characters should fail
        similar_passwords = [
            'P@ssw0rd!#$',  # Missing %
            'P@ssw0rd!#$&',  # Different last character
        ]
        
        for wrong_pass in similar_passwords:
            result = self.login_system.login(test_username, wrong_pass)
            self.assertFalse(result['success'])
    
    def test_response_consistency(self):
        """
        Test that login responses maintain consistency for same inputs.
        """
        username = 'user1'
        password = 'pass1234'
        
        # Call login multiple times with same credentials
        results = [self.login_system.login(username, password) for _ in range(5)]
        
        # All results should be identical
        for result in results:
            self.assertTrue(result['success'])
            self.assertEqual(result['user_id'], username)
            self.assertEqual(result['message'], f'Login successful for user {username}')


if __name__ == '__main__':
    unittest.main()
