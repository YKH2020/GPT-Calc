import main


def test_invalid_function():
    main.invalid("google.com")


def test_create_urls():
    result = main.create_urls("google.com", "bing.com", "yahoo.com")
    assert sorted(result) == sorted(['https://google.com/', 'https://bing.com/', 'https://yahoo.com/'])


def test_social_media_is_verified():
    result = main.social_media_user("johnmasters", verified=True)
    assert result == {"username": "johnmasters", "verified": True}


def test_social_media_verified_default():
    result = main.social_media_user("johnmasters")
    assert result == {"username": "johnmasters", "verified": False}


def test_social_media_metadata():
    result = main.social_media_user("johnmasters", bar=1, status='offline')
    assert result == {"username": "johnmasters", "verified": False, 'bar': 1, 'status': 'offline'}


def test_fahrenheit():
    temp = main.Fahrenheit(98)
    assert int(temp.as_celsius()) == 36


# for instance in TwitterUser.__mro__: print(instance.__name__)
def test_twitter_user_url():
    user = main.TwitterUser("marcusaurelius")
    assert user.url() == "https://twitter.com/marcusaurelius"


def test_twitter_verified():
    user = main.TwitterUser("marcusaurelius")
    assert user.verified() is True


def test_linkedin_user_url():
    user = main.LinkedInUser("marcusaurelius")
    assert user.url() == "https://linkedin.com/in/marcusaurelius"


def test_linkedin_verified():
    user = main.LinkedInUser("marcusaurelius")
    assert user.verified() is True


def test_twitter_has_parent_class():
    result = len(main.TwitterUser.__mro__)
    assert result == 3, "the TwitterUser class needs to have a parent class"


def test_linkedin_has_parent_class():
    result = len(main.LinkedInUser.__mro__)
    assert result == 3, "the LinkedInUser class needs to have a parent class"


def test_twitteruser_parent_class_has_url():
    methods = []
    for instance in main.TwitterUser.__mro__:
        if instance.__name__ not in ["TwitterUser", "object"]:
            methods = dir(instance)
    assert "url" in methods, "The url method was not found in TwitterUser parent class"
    assert "verified" in methods, "The verified method was not found in TwitterUser parent class"


def test_linkedinuser_parent_class_has_url():
    methods = []
    for instance in main.LinkedInUser.__mro__:
        if instance.__name__ not in ["LinkedInUser", "object"]:
            methods = dir(instance)
    assert "url" in methods, "The url method was not found in LinkedInUser parent class"
    assert "verified" in methods, "The verified method was not found in LinkedInUser parent class"


def test_utils_import():
    assert main.convert("y") is not None, "Expected a boolean returned from the function but got a None"
    assert main.convert("y") is True, "Expected a True return value after passing 'y'"