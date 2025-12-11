# SE Assignment 3 - Login System Testing

## Project Structure

```
SE_Assgn_3/
├── src/
│   └── login.py                 # Login system implementation
├── tests/
│   ├── unit/
│   │   └── test_login.py        # Unit tests
│   └── integration/
│       └── test_login_integration.py  # Integration tests
├── docs/
│   └── TEST_CASES.md            # Test case documentation
└── README.md                    # This file
```

## Test Cases (6 Required)

### Positive Test Cases (4)
- **TC-01**: Login with valid credentials (admin)
- **TC-02**: Login with another valid user (user1)
- **TC-03**: Login with special characters in password
- **TC-04**: Verify response structure of successful login

### Negative Test Cases (2)
- **TC-05**: Login fails with invalid username
- **TC-06**: Login fails with incorrect password

See [docs/TEST_CASES.md](docs/TEST_CASES.md) for detailed test cases.

## Test Credentials

| Username | Password |
|----------|----------|
| admin | password123 |
| user1 | pass1234 |
| testuser | test@123 |

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Assignment Requirements

✓ GitHub Repository folder structure created  
✓ src/ - Main system code  
✓ tests/unit/ - Unit tests (16 test cases)  
✓ tests/integration/ - Integration tests (7 test cases)  
✓ docs/ - Test case documentation  
✓ 6 test cases (4 positive + 2 negative)  
✓ Test case template used  
✓ Automated test code implemented
