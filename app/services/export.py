import markdown
import pdfkit
from app.models.models import JournalEntry


def generate_markdown(entry: JournalEntry) -> str:
    return f"# {entry.title}\n{entry.content}\n*Created: {entry.created_at.strftime('%Y-%m-%d')}*"


def generate_pdf(entry: JournalEntry) -> bytes:
    html = markdown.markdown(generate_markdown(entry))
    pdf = pdfkit.from_string(html, False)
    return pdf
