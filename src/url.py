url_mapping = [
    # api
    ("/api/signup", "api.signup"),
    ("/api/login", "api.login"),
    ("/api/logout", "api.logout"),
    ("/api/submit", "api.submit"),
    ("/api/delnews", "api.delete_news"),
    ("/api/updateprofile", "api.update_profile"),
    ("/api/votenews", "api.vote_news"),
    ("/$", "app.top"),
    ("/top$", "app.top"),
    ("/about$", "app.about"),
    ("/signup$", "app.signup"),
    ("/login$", "app.login"),
    ("/logout$", "app.logout"),
    ("/submit$", "app.submit"),
    ("/rss$", "app.rss"),
    ("/login/github$", "github.auth"),
    ("/oauth/github/callback$", "github.callback"),
    (r"/latest(/\d+)?$", "app.latest"),
    (r"/saved(/\d+)?$", "app.saved"),
    ("/comments$", "app.comments"),
    (r"/news/(\d+)$", "app.newspage"),
    (r"/editnews/(\d+)$", "app.editnews"),
    (r"/user/(\w+)$", "app.userpage"),
    (r"/luser/(\w+)$", "app.userpage"),
    ("/lusers$", "app.lusers"),
]
