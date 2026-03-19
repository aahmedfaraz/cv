from PyPDF2 import PdfMerger
from PIL import Image
import os

# =============================
# Input files
# =============================

# Add your PDF files here (can be 1 or more)
pdf_files = [
    "cv.pdf",
    # pdf_files.append("another_file.pdf")  # <-- example to add more PDFs
]

# Add your image files here (can be 1 or more)
image_files = [
    "transcript.jpg",
    "ielts.jpg",
    # image_files.append("certificate.png")  # <-- example to add more images
]

# =============================
# Settings
# =============================
DPI = 300
A4_SIZE = (2480, 3508)  # A4 at 300 DPI (pixels)

merger = PdfMerger()
temp_pdfs = []

# =============================
# Merge PDFs
# =============================
for pdf in pdf_files:
    merger.append(pdf)

# =============================
# Convert images to proportional A4 PDFs
# =============================
for i, img_path in enumerate(image_files):
    img = Image.open(img_path).convert("RGB")

    # Scale image to fit A4 while keeping aspect ratio
    scale_ratio = min(A4_SIZE[0] / img.width, A4_SIZE[1] / img.height)
    new_size = (int(img.width * scale_ratio), int(img.height * scale_ratio))

    # Resize with high-quality resampling
    img_resized = img.resize(new_size, Image.LANCZOS)

    # Create white A4 background
    a4_img = Image.new("RGB", A4_SIZE, (255, 255, 255))

    # Center the image
    x = (A4_SIZE[0] - img_resized.width) // 2
    y = (A4_SIZE[1] - img_resized.height) // 2
    a4_img.paste(img_resized, (x, y))

    # Save temporary PDF
    temp_pdf = f"temp_{i}.pdf"
    a4_img.save(temp_pdf, "PDF", resolution=DPI)

    # Append to merger
    merger.append(temp_pdf)
    temp_pdfs.append(temp_pdf)

# =============================
# Output final merged PDF
# =============================
output_file = "portfolio.pdf"
merger.write(output_file)
merger.close()

# =============================
# Cleanup temporary files
# =============================
for temp in temp_pdfs:
    os.remove(temp)

print("✅ Created:", output_file)