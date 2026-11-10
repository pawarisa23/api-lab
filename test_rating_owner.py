def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to read the rating.
    res = api.get(path, headers=other_auth)
    print("READ status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # The owner can still read the rating.
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json() == rating


def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to update the rating.
    res = api.put(
        path,
        json={"stars": 4},
        headers=other_auth
    )
    print("UPDATE status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # Check that the owner's rating has not changed.
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3


def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    # Another user tries to delete the rating.
    res = api.delete(path, headers=other_auth)
    print("DELETE status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # Check that the owner's rating still exists.
    owner_res = api.get(path, headers=auth)
    assert owner_res.status_code == 200
    assert owner_res.json() == rating