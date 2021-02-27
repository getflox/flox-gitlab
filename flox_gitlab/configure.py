from typing import Tuple

from floxcore.config import Configuration, ParamDefinition


class GitlabConfiguration(Configuration):
    def parameters(self) -> Tuple[ParamDefinition, ...]:
        return (
            ParamDefinition("url", "URL to gitlab", default="https://gitlab.com"),
            ParamDefinition("namespace", "Namespace"),
            ParamDefinition("default_branch", "Default branch", default="develop"),
            ParamDefinition("visibility", "Visibility", default="private"),
            ParamDefinition("issues", "Enable issue management", default="enabled"),
            ParamDefinition("wiki", "Enable wiki", default="enabled"),
            ParamDefinition("snippets", "Enable snippets", default="enabled"),
            ParamDefinition("pages", "Enable pages", default="enabled"),
            ParamDefinition("builds", "Enable builds", default="enabled"),
            ParamDefinition("forking", "Enable forking", default="enabled"),
        )

    def secrets(self) -> Tuple[ParamDefinition, ...]:
        return (
            ParamDefinition("token", "Gitlab Access Token", secret=True),
        )

    def schema(self):
        pass
