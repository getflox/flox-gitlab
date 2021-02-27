import json

from gitlab import Gitlab, GitlabCreateError

from flox_gitlab.remote import with_gitlab, handle_exceptions
from floxcore.context import Flox


@handle_exceptions
@with_gitlab
def create_project(flox: Flox, gl: Gitlab, out, **kwargs):
    """Create gitlab project"""
    gl_settings = flox.settings.gitlab
    try:
        gl.projects.create(name=flox.id, description=flox.meta.description, default_branch=gl_settings.default_branch,
                           visibility=gl_settings.visibility, issues_access_level=gl_settings.issues,
                           wiki_access_level=gl_settings.wiki, snippets_access_level=gl_settings.snippets,
                           pages_access_level=gl_settings.pages, builds_access_level=gl_settings.builds,
                           forking_access_level=gl_settings.forking)
        out.success(f'Project "{flox.id}" created')
    except GitlabCreateError as e:
        body = json.loads(e.response_body)
        if "message" in body:
            if body["message"]["name"][0] == "has already been taken":
                out.info(f'Skipping, project "{flox.id}" already exists')
            else:
                raise
        else:
            raise


@handle_exceptions
@with_gitlab
def configure_project(flox: Flox, gl: Gitlab, out, **kwargs):
    """Edit gitlab project"""
    gl_settings = flox.settings.gitlab
    project = gl.projects.get(id=f"{gl_settings.namespace}/{flox.id}")

    gl.projects.update(id=project.id, description=flox.meta.description,
                       default_branch=gl_settings.default_branch, visibility=gl_settings.visibility,
                       issues_access_level=gl_settings.issues, wiki_access_level=gl_settings.wiki,
                       snippets_access_level=gl_settings.snippets, pages_access_level=gl_settings.pages,
                       builds_access_level=gl_settings.builds, forking_access_level=gl_settings.forking)
    out.success(f'Project "{flox.id}" updated')
