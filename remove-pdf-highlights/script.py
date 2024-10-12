import fitz  # PyMuPDF
import os

# Paths for input and output folders
input_folder = "input_pdfs"
output_folder = "output_pdfs"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the input folder
for pdf_file in os.listdir(input_folder):
    if pdf_file.endswith(".pdf"):
        input_path = os.path.join(input_folder, pdf_file)
        output_path = os.path.join(output_folder, pdf_file.replace(".pdf", "_no_highlight.pdf"))    # add '_no_highlight.pdf' suffix to filename
        
        # Open the PDF document
        doc = fitz.open(input_path)
        total_pages = doc.page_count
        
        # Iterate over all pages in the PDF
        for page_num in range(total_pages):
            print(f"Processing Page {page_num+1}/{total_pages}")
            page = doc[page_num]

            # Get all annotations on the page
            annotations = page.annots()
            
            # If the page contains annotations, iterate and delete highlights
            if annotations:
                for annot in annotations:
                    if annot.type[0] == 8:  # 8 corresponds to a Highlight annotation
                        page.delete_annot(annot)

        # Save the modified PDF with '_no_highlight' suffix in the output folder
        doc.save(output_path)

        # Close the PDF document
        doc.close()

        print(f"Processed and saved: {output_path}")

print("All PDFs processed.")
