from dataclasses import dataclass
from pathlib import Path
from pymupdf import pymupdf


@dataclass(frozen=True)
class ExtractedPage:
    page_number: int
    text: str


def extract_pdf_pages(pdf_path: Path) -> list[ExtractedPage]:
    """Extract text from each PDF page, preserving page numbers."""
    pages = []
    with pymupdf.open(pdf_path) as doc:
        for idx, page in enumerate(doc, start=1):
            curr_text = page.get_text("text")
            curr_extracted_page = ExtractedPage(
                page_number=idx,
                text=curr_text
            )
            pages.append(curr_extracted_page)

    return pages










    
    return page_context

    

