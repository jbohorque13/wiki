from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def slug(request, slug):
    if util.get_entry(slug) == None:
        return render(request, "encyclopedia/slug.html", {
            "slug": f"{slug} Not found Page 404"
        })
    else:
        return render(request, "encyclopedia/slug.html", {
            "slug": util.get_entry(slug),
            "title": slug
        })

