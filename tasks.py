"""Invoke tasks for the LOB repository management tool."""

from invoke import task

from lob_management.validate import validate_repository
from lob_management.argo import cmp
from lob_management.generate import generate_content


@task
def validate(c, path=None):
    result = validate_repository(path)
    if result:
        print("✅ Repository validation successful")
    else:
        print("❌ Repository validation failed")


@task
def argo_cmp(c):
    result = cmp()
    if result:
        print("✅ Argo CMP successful")
    else:
        print("❌ Argo CMP failed")


@task
def generate(c, template=None, output=None):
    result = generate_content(template, output)
    if result:
        print("✅ Content generation successful")
    else:
        print("❌ Content generation failed")
