from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Entry


@staff_member_required
def entry_list(request):
    query = request.GET.get("q", "").strip()
    entries = Entry.objects.all().prefetch_related("sections")

    if query:
        entries = entries.filter(
            Q(title__icontains=query)
            | Q(category__icontains=query)
            | Q(notes__icontains=query)
            | Q(sections__label__icontains=query)
            | Q(sections__url__icontains=query)
            | Q(sections__username__icontains=query)
            | Q(sections__extra__icontains=query)
        ).distinct()

    context = {
        "entries": entries,
        "query": query,
        "total_count": Entry.objects.count(),
    }
    return render(request, "vault/entry_list.html", context)


@staff_member_required
def entry_detail(request, pk):
    entry = get_object_or_404(Entry.objects.prefetch_related("sections"), pk=pk)
    return render(request, "vault/entry_detail.html", {"entry": entry})
