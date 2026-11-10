# api-lab
# API lab results

## Part 0

- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Sad Bolognese

### Step 0.12: A test without a session

Run 1: FAILED (401 Unauthorized)

Run 2: PASSED (200 OK)

Run 3: PASSED (200 OK)

The test is flaky because the login request may be sent to a different server without the session cookie.

### Step 0.16: Bug Hunt

#### Defect 1: Excluding All Available Pizza Tools

**Request:**

```json
{
    "excludedTools": ["Knife", "Scissors", "Pizza cutter"]
}
```

**Expected Result:**

The API should return HTTP status code 400 (Bad Request) with a JSON error message because all available pizza tools have been excluded.

**Actual Result:**

The API returns HTTP status code 500 (Internal Server Error) with an empty response body (Content-Length: 0).

**Severity:**

High — The API returns an internal server error instead of properly handling a request that excludes all available pizza tools.