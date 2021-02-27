from flox_gitlab.configure import GitlabConfiguration
from flox_gitlab.project import create_project, configure_project
from floxcore.command import Stage
from floxcore.context import Flox
from floxcore.plugin import Plugin


class GitlabPlugin(Plugin):
    def configuration(self):
        return GitlabConfiguration()

    def handle_project(self, flox: Flox):
        return [
            Stage(create_project),
            Stage(configure_project),
        ]


def plugin():
    return GitlabPlugin()
