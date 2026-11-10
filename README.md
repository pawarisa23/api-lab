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

## Part A

| Characteristic | Block | Test value | Test function |
|---|---|---|---|
| C1: Value of stars | Below 1 | 0 | test_stars_out_of_range[0] |
| C1: Value of stars | 1 to 5 (Base) | 3 | test_base_choice_is_saved |
| C1: Value of stars | Above 5 | 6 | test_stars_out_of_range[6] |
| C2: Type of stars | Whole number (Base) | 3 | test_base_choice_is_saved |
| C2: Type of stars | Decimal | 3.5 | test_decimal_stars_are_refused |
| C2: Type of stars | Text | "3" | test_text_stars_are_refused |
| C2: Type of stars | Missing | No stars field | test_missing_stars_are_refused |
| C3: Pizza | Exists (Base) | Existing pizza_id | test_base_choice_is_saved |
| C3: Pizza | Does not exist | 999999999 | test_nonexistent_pizza_is_refused |
| C4: Token | User's own (Base) | Valid auth token | test_base_choice_is_saved |
| C4: Token | None | No Authorization header | test_rating_without_token_is_refused |
| C4: Token | Wrong length | "short" | test_rating_with_short_token_is_refused |

### Step A4: Rating Ownership

Tested whether another user could read, update, or delete a rating owned by someone else.

| Action | HTTP Status Code | Result |
|---|---:|---|
| Read another user's rating (GET) | 404 | Refused |
| Update another user's rating (PUT) | 400 | Refused |
| Delete another user's rating (DELETE) | 400 | Refused |

All three requests were refused with 4xx status codes. The rating owner could still access the rating, and the rating remained unchanged after the unauthorized update and delete attempts.

## Part B: Reflection

### 1. What are two kinds of failure that real-server API tests can find that unit tests with stubs cannot? Why write unit tests with stubs at all?

Real-server API tests can detect problems with the actual server, such as incorrect HTTP responses, authentication problems, and database or integration issues. Unit tests with stubs cannot fully verify these real interactions because they replace external components with simulated responses. However, unit tests with stubs are still useful because they run faster, isolate individual components, and help identify errors in specific units of code.

### 2. Why does each test create its own new user instead of using a public token? How would you apply the same idea to a shared shop or hotel in Project 2?

Each test creates its own user to avoid sharing data and interfering with other tests. A public token could cause tests to depend on shared accounts or existing data, making results unreliable. In Project 2, I would apply the same idea by creating separate test accounts and test data for each test, such as a separate booking or reservation, to prevent tests from affecting one another.

### 3. Why send requests through one session? Describe the three runs in Step 0.12.

Using one requests session allows cookies to be stored and reused automatically between requests. This helps maintain session information when requests are sent to the server. In Step 0.12, the first run failed with HTTP 401, while the second and third runs passed with HTTP 200. This showed that the test result was inconsistent across runs.

### 4. Which excluded-tools block found the defect in Step 0.16? Why is HTTP 500 with an empty body worse than HTTP 400 with an error message? Why keep xfail?

The defect occurred when all three tools (Knife, Scissors, and Pizza cutter) were excluded. The server returned HTTP 500 with an empty response body instead of HTTP 400 with a JSON error message. HTTP 500 indicates an internal server error and provides no useful explanation to the client. HTTP 400 would communicate that the request was invalid and an error message would help the application understand the problem. Keeping the test as xfail documents the known defect and helps detect when it is fixed.

### 5. How many base choices are there in Step A1? How many combinations are there if all blocks are combined?

There is one base choice because each characteristic has one base block. The number of combinations using all blocks is:

3 × 4 × 2 × 3 = 72 combinations.

Therefore, there is 1 base choice and 72 possible combinations in total.

### 6. In Step A4, what exact status codes did another user receive when reading, updating, and deleting a rating? Were they expected? Is there a difference that indicates a defect?

The other user received HTTP 404 when trying to read the rating, HTTP 400 when trying to update it, and HTTP 400 when trying to delete it. All three responses are in the 4xx range, which means the requests were refused as expected by the test requirements. The owner could still access the rating, and the rating remained unchanged.

### 7. What happens when using a made-up token? Is this a defect? What could a stranger do on a real system?

I created a file named `madeup.txt` containing the fake token `0000000000000000` and sent a GET request to `/api/ratings`. The server returned HTTP 200 OK and a list of ratings, including their IDs, star values, and pizza IDs.

This is a potential security defect because the API allowed access to rating data without a valid user token. On a real system, a stranger might be able to access information that should be protected. However, this experiment only tested reading data. It does not prove that the stranger can create, update, or delete ratings.

### 8. What is one thing an API test checks better than a web-page test? What is one thing only a web-page test can check?

An API test is better for checking HTTP status codes, response data, and whether the API follows its expected behavior. A web-page test can check visual elements and user-interface behavior, such as layout, buttons, and how the page appears in a browser.