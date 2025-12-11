"""
Login System Module
This module provides authentication functionality for user login.
"""

class LoginSystem:
    """A simple login system for user authentication."""
    
    def __init__(self):
        """Initialize the login system with valid user credentials."""
        # Simulated user database
        self.users = {
            "admin": "password123",
            "user1": "pass1234",
            "testuser": "test@123"
        }
    
    def login(self, username, password):
        """
        Authenticate a user with provided credentials.
        
        Args:
            username (str): The username of the user
            password (str): The password of the user
        
        Returns:
            dict: A dictionary containing:
                - 'success' (bool): Whether login was successful
                - 'message' (str): A message describing the result
                - 'user_id' (str or None): The user ID if successful, None otherwise
        
        Raises:
            ValueError: If username or password is empty or None
            TypeError: If username or password is not a string
        """
        
        # Input validation
        if not isinstance(username, str) or not isinstance(password, str):
            raise TypeError("Username and password must be strings")
        
        if not username or not password:
            raise ValueError("Username and password cannot be empty")
        
        # Check if user exists and password matches
        if username in self.users and self.users[username] == password:
            return {
                'success': True,
                'message': f'Login successful for user {username}',
                'user_id': username
            }
        else:
            return {
                'success': False,
                'message': 'Invalid username or password',
                'user_id': None
            }
    
    def add_user(self, username, password):
        """
        Add a new user to the system.
        
        Args:
            username (str): The username for the new user
            password (str): The password for the new user
        
        Returns:
            dict: A dictionary containing:
                - 'success' (bool): Whether user was added successfully
                - 'message' (str): A message describing the result
        
        Raises:
            ValueError: If username already exists
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists")
        
        self.users[username] = password
        return {
            'success': True,
            'message': f'User {username} created successfully'
        }
    
    def user_exists(self, username):
        """
        Check if a user exists in the system.
        
        Args:
            username (str): The username to check
        
        Returns:
            bool: True if user exists, False otherwise
        """
        return username in self.users
