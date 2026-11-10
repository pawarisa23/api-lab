import pytest


@pytest.mark.parametrize("excluded", [
    [],
    ["Knife"],
    ["Scissors"],
    ["Knife", "Pizza cutter"]
])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


@pytest.mark.xfail(
    reason="Defect 1: Excluding all three tools returns HTTP 500 instead of HTTP 400 with a JSON error message.",
    strict=True
)
def test_all_tools_excluded_is_refused(api, auth):
    body = {
        "excludedTools": ["Knife", "Scissors", "Pizza cutter"]
    }
    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()