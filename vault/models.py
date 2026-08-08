from django.db import models


class Entry(models.Model):
    """A main item (for example, a server, service, or general account)."""

    title = models.CharField("Title", max_length=200)

    category = models.CharField(
        "Category",
        max_length=100,
        blank=True,
        help_text="For example: Server, Hosting, Email, Bank, Social Network, etc."
    )

    notes = models.TextField("General Notes", blank=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)

    updated_at = models.DateTimeField("Last Updated", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    A section of an entry (for example, SSH of a server,
    hosting panel, database, FTP, etc.).

    Each entry can have multiple sections, and each section
    can have its own URL, username, password, and additional information.
    """

    entry = models.ForeignKey(
        Entry,
        related_name="sections",
        on_delete=models.CASCADE,
        verbose_name="Entry"
    )

    label = models.CharField(
        "Section Title",
        max_length=100,
        help_text="For example: SSH, Admin Panel, Database, FTP, etc."
    )

    url = models.CharField(
        "URL / Address",
        max_length=500,
        blank=True
    )

    username = models.CharField(
        "Username",
        max_length=200,
        blank=True
    )

    password = models.CharField(
        "Password",
        max_length=500,
        blank=True
    )

    extra = models.TextField(
        "Additional Information",
        blank=True,
        help_text="Any additional information, such as port, API key, notes, etc."
    )

    order = models.PositiveIntegerField(
        "Order",
        default=0
    )

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.entry.title} — {self.label}"
