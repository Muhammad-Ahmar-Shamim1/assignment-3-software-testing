# Test Case Documentation - Login Functionality

## System Under Test: User Login System

### Overview
This document outlines the test cases for the login functionality of the authentication system. The login system validates user credentials against a user database and returns appropriate success or failure responses.

---

## Test Cases

### POSITIVE TEST CASES (4 cases)

#### TC-01: Verify login with valid credentials
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-01 |
| **Description** | Verify login with valid credentials |
| **Pre-Conditions** | User account exists with username 'admin' and password 'password123' |
| **Input** | username: 'admin' + password: 'password123' |
| **Steps** | 1. Call login system<br>2. Pass valid username and password<br>3. Submit login request |
| **Expected Result** | User should be logged in successfully with success status True and valid user_id returned |

---

#### TC-02: Verify login with another valid user account
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-02 |
| **Description** | Verify login with another valid user account |
| **Pre-Conditions** | User account exists with username 'user1' and password 'pass1234' |
| **Input** | username: 'user1' + password: 'pass1234' |
| **Steps** | 1. Call login system<br>2. Pass valid username and password for different user<br>3. Submit login request |
| **Expected Result** | User 'user1' should be logged in successfully with success status True and user_id 'user1' returned |

---

#### TC-03: Verify login with special characters in password
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-03 |
| **Description** | Verify login with special characters in password |
| **Pre-Conditions** | User account exists with username 'testuser' and password 'test@123' |
| **Input** | username: 'testuser' + password: 'test@123' |
| **Steps** | 1. Call login system<br>2. Pass username and password containing special characters<br>3. Submit login request |
| **Expected Result** | User should be logged in successfully; system should handle special characters correctly |

---

#### TC-04: Verify successful login returns correct response structure
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-04 |
| **Description** | Verify successful login returns correct response structure |
| **Pre-Conditions** | User account exists with valid credentials |
| **Input** | username: 'admin' + password: 'password123' |
| **Steps** | 1. Call login system<br>2. Pass valid credentials<br>3. Verify response structure contains all required fields |
| **Expected Result** | Response should contain 'success': True, 'message' string, and 'user_id' with correct username |

---

### NEGATIVE TEST CASES (2 cases)

#### TC-05: Verify login fails with invalid username
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-05 |
| **Description** | Verify login fails with invalid username |
| **Pre-Conditions** | User account with username 'invaliduser' does not exist |
| **Input** | username: 'invaliduser' + password: 'anypassword' |
| **Steps** | 1. Call login system<br>2. Pass non-existent username with any password<br>3. Submit login request |
| **Expected Result** | Login should fail with success status False and appropriate error message "Invalid username or password" |

---

#### TC-06: Verify login fails with incorrect password
| Attribute | Value |
|-----------|-------|
| **Test Case ID** | TC-06 |
| **Description** | Verify login fails with incorrect password for existing user |
| **Pre-Conditions** | User account exists with username 'admin' and correct password 'password123' |
| **Input** | username: 'admin' + password: 'wrongpassword' |
| **Steps** | 1. Call login system<br>2. Pass valid username with incorrect password<br>3. Submit login request |
| **Expected Result** | Login should fail with success status False and error message "Invalid username or password" returned |

---

## Test Summary

- **Total Test Cases**: 6
- **Positive Test Cases**: 4 (TC-01, TC-02, TC-03, TC-04)
- **Negative Test Cases**: 2 (TC-05, TC-06)

### Coverage Areas:
- Valid user authentication
- Invalid credentials handling
- Special character support
- Response structure validation
- Error handling

