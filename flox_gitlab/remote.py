from functools import wraps

from gitlab import Gitlab, GitlabError

from floxcore.exceptions import PluginException


def handle_exceptions(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except GitlabError as e:
            raise PluginException(f'[Gitlab API] [{f.__name__}] [{e.response_code}] "{e.error_message}".')

    return wrapper


def with_gitlab(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        flox = kwargs.get("flox")

        gl = Gitlab(flox.settings.gitlab.url, private_token=flox.secrets.getone("gitlab_token", required=True))
        kwargs["gl"] = gl

        return f(*args, **kwargs)

    return wrapper
