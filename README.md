# api-lab
# API lab results

## Part 0
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Sad Bolognese
- Step 0.12: A test without a session

Run 1: FAILED (401 Unauthorized)
Run 2: PASSED (200 OK)
Run 3: PASSED (200 OK)

The test is flaky because the login request may be sent to a different server without the session cookie.