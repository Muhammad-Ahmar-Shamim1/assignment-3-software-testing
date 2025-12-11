"""
Unit Tests for Login System
This module contains unit tests for the login functionality.
"""

import unittest
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from login import LoginSystem


class TestLoginSystem(unittest.TestCase):
    """Test cases for the LoginSystem class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.login_system = LoginSystem()
    
    # POSITIVE TEST CASES
    
    def test_tc01_login_with_valid_credentials_admin(self):
        """
        TC-01: Verify login with valid credentials
        Pre-Conditions: User account exists with username 'admin' and password 'password123'
        Input: username: 'admin' + password: 'password123'
        Expected Result: User should be logged in successfully
        """
        result = self.login_system.login('admin', 'password123')
        
        self.assertTrue(result['success'])
        self.assertEqual(result['user_id'], 'admin')
        self.assertIn('successful', result['message'].lower())
    
    def test_tc02_login_with_valid_credentials_user1(self):
        """
        TC-02: Verify login with another valid user account
        Pre-Conditions: User account exists with username 'user1' and password 'pass1234'
        Input: username: 'user1' + password: 'pass1234'
        Expected Result: User 'user1' should be logged in successfully
        """
        result = self.login_system.login('user1', 'pass1234')
        
        self.assertTrue(result['success'])
        self.assertEqual(result['user_id'], 'user1')
        self.assertIn('successful', result['message'].lower())
    
    def test_tc03_login_with_special_characters_in_password(self):
        """
        TC-03: Verify login with special characters in password
        Pre-Conditions: User account exists with username 'testuser' and password 'test@123'
        Input: username: 'testuser' + password: 'test@123'
        Expected Result: User should be logged in successfully
        """
        result = self.login_system.login('testuser', 'test@123')
        
        self.assertTrue(result['success'])
        self.assertEqual(result['user_id'], 'testuser')
        self.assertIn('successful', result['message'].lower())
    
    def test_tc04_login_response_structure(self):
        """
        TC-04: Verify successful login returns correct response structure
        Pre-Conditions: User account exists with valid credentials
        Input: username: 'admin' + password: 'password123'
        Expected Result: Response should contain all required fields
        """
        result = self.login_system.login('admin', 'password123')
        
        # Check response structure
        self.assertIn('success', result)
        self.assertIn('message', result)
        self.assertIn('user_id', result)
        
        # Check data types
        self.assertIsInstance(result['success'], bool)
        self.assertIsInstance(result['message'], str)
        self.assertIsInstance(result['user_id'], (str, type(None)))
        
        # Check values
        self.assertTrue(result['success'])
        self.assertEqual(result['user_id'], 'admin')
    
    # NEGATIVE TEST CASES
    
    def test_tc05_login_fails_with_invalid_username(self):
        """
        TC-05: Verify login fails with invalid username
        Pre-Conditions: User account with username 'invaliduser' does not exist
        Input: username: 'invaliduser' + password: 'anypassword'
        Expected Result: Login should fail with success status False
        """
        result = self.login_system.login('invaliduser', 'anypassword')
        
        self.assertFalse(result['success'])
        self.assertIsNone(result['user_id'])
        self.assertEqual(result['message'], 'Invalid username or password')
    
    def test_tc06_login_fails_with_incorrect_password(self):
        """
        TC-06: Verify login fails with incorrect password
        Pre-Conditions: User account exists with username 'admin' and password 'password123'
        Input: username: 'admin' + password: 'wrongpassword'
        Expected Result: Login should fail with success status False
        """
        result = self.login_system.login('admin', 'wrongpassword')
        
        self.assertFalse(result['success'])
        self.assertIsNone(result['user_id'])
        self.assertEqual(result['message'], 'Invalid username or password')
    
    # ADDITIONAL EDGE CASE TESTS
    
    def test_empty_username_raises_error(self):
        """Test that empty username raises ValueError."""
        with self.assertRaises(ValueError):
            self.login_system.login('', 'password123')
    
    def test_empty_password_raises_error(self):
        """Test that empty password raises ValueError."""
        with self.assertRaises(ValueError):
            self.login_system.login('admin', '')
    
    def test_none_username_raises_error(self):
        """Test that None username raises ValueError."""
        with self.assertRaises(ValueError):
            self.login_system.login(None, 'password123')
    
    def test_none_password_raises_error(self):
        """Test that None password raises ValueError."""
        with self.assertRaises(ValueError):
            self.login_system.login('admin', None)
    
    def test_non_string_username_raises_error(self):
        """Test that non-string username raises TypeError."""
        with self.assertRaises(TypeError):
            self.login_system.login(123, 'password123')
    
    def test_non_string_password_raises_error(self):
        """Test that non-string password raises TypeError."""
        with self.assertRaises(TypeError):
            self.login_system.login('admin', 123)
    
    def test_user_exists_method(self):
        """Test the user_exists method."""
        self.assertTrue(self.login_system.user_exists('admin'))
        self.assertTrue(self.login_system.user_exists('user1'))
        self.assertFalse(self.login_system.user_exists('nonexistent'))
    
    def test_add_user_method(self):
        """Test adding a new user to the system."""
        result = self.login_system.add_user('newuser', 'newpass123')
        
        self.assertTrue(result['success'])
        self.assertTrue(self.login_system.user_exists('newuser'))
        
        # Verify the new user can login
        login_result = self.login_system.login('newuser', 'newpass123')
        self.assertTrue(login_result['success'])
    
    def test_add_duplicate_user_raises_error(self):
        """Test that adding duplicate user raises ValueError."""
        with self.assertRaises(ValueError):
            self.login_system.add_user('admin', 'newpass')


if __name__ == '__main__':
    unittest.main()
