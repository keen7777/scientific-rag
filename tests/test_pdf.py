from pathlib import Path
import pytest
import pymupdf

from scientific_rag.ingestion.pdf import extract_pdf_pages


def test_extract_pdf_pages(tmp_path: Path):
    # 1: Create a PDF with 3 pages    
    # 2: Insert text on pages 1 and 3
    # 3: Save PDF to tmp_path
    # 4: Call extract_pdf_pages()
    # 5: Assert the extracted results
    pdf_path = tmp_path / "test_document.pdf"
    with pymupdf.open() as test_doc:           
        page = test_doc.new_page()          
        page.insert_text((72, 72), "this is the 1st page")    
        page = test_doc.new_page()  
        page = test_doc.new_page()           
        page.insert_text((72, 72), "this is the 3rd page") 
        test_doc.save(pdf_path) 
    
    pages = extract_pdf_pages(pdf_path)
    assert pdf_path.exists()
    assert len(pages) == 3
    assert pages[0].page_number == 1
    assert pages[1].page_number == 2
    assert pages[2].page_number == 3
    assert pages[0].text.strip() == "this is the 1st page"
    # avoid "   \n".strip() == ""
    assert pages[1].text == ""
    assert pages[2].text.strip() == "this is the 3rd page"

def test_extract_pdf_pages_missing_file(tmp_path: Path):
    # Arrange: Construct a path to a nonexistent PDF
    pdf_path = tmp_path / "test_no_document.pdf"        

    # Act & Assert: Verify that extraction raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        extract_pdf_pages(pdf_path)


def test_extract_pdf_pages_invalid_file(tmp_path: Path):
    # Arrange: Create a file with .pdf extension
    # but invalid PDF content
    pdf_path = tmp_path / "invalid.pdf"
    pdf_path.write_text("This is not a PDF", encoding="utf-8")      
    
        # Act & Assert: Verify that extraction raises ValueError
    with pytest.raises(ValueError):
        extract_pdf_pages(pdf_path)
    