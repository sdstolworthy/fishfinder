#!/usr/bin/env python

import os, sys

if __name__ == "__main__":
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fishfinder.settings")

    # Setup django
    import django

    django.setup()
    from planes.search import run

    run()
