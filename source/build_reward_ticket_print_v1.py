"""Place the unmodified reward-ticket artwork on a home-printable Letter sheet."""
from pathlib import Path
import json
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "assets/moon-and-beyond-reward-ticket-v1.png"
OUT = ROOT / "output/pdf/moon-and-beyond-reward-ticket-letter-v1.pdf"
TICKET_WIDTH, TICKET_HEIGHT = 7.5 * 72, 2.5 * 72


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(ART) as image:
        pixel_width, pixel_height = image.size
    ratio = pixel_width / pixel_height
    if abs(ratio - 3.0) > 0.005:
        raise ValueError("Ticket artwork must have a 3:1 aspect ratio; do not distort it.")
    page = canvas.Canvas(str(OUT), pagesize=letter, pageCompression=1)
    page.setTitle("Space Exploration - Moon and beyond reward ticket")
    page.setAuthor("Escape Backpack")
    page.setFillColor(HexColor("#18304A"))
    page.setFont("Helvetica-Bold", 13)
    page.drawString(36, 744, "SPACE EXPLORATION")
    page.setFont("Helvetica", 10)
    page.drawString(36, 724, "Final reward ticket - draft print layout")
    page.setFillColor(HexColor("#515A64"))
    page.setFont("Helvetica", 9)
    page.drawString(36, 696, "Print at actual size (100%). Turn off Fit to page.")
    page.drawString(36, 681, "Ticket size: 7.5 x 2.5 in (190.5 x 63.5 mm). Cut at the crop marks.")
    x, y = 36, 414
    page.drawImage(str(ART), x, y, width=TICKET_WIDTH, height=TICKET_HEIGHT,
                   preserveAspectRatio=True, anchor="c", mask="auto")
    page.setStrokeColor(HexColor("#77828D"))
    page.setLineWidth(0.45)
    gap, length = 3, 6
    for cx in (x, x + TICKET_WIDTH):
        sx = -1 if cx == x else 1
        for cy in (y, y + TICKET_HEIGHT):
            sy = -1 if cy == y else 1
            page.line(cx + sx * gap, cy, cx + sx * (gap + length), cy)
            page.line(cx, cy + sy * gap, cx, cy + sy * (gap + length))
    page.setStrokeColor(HexColor("#18304A"))
    page.setLineWidth(0.75)
    page.line(36, 348, 108, 348)
    page.line(36, 344, 36, 352)
    page.line(108, 344, 108, 352)
    page.setFont("Helvetica", 8)
    page.drawString(36, 330, "Size check: this line should measure 1 inch / 25.4 mm.")
    page.setFont("Helvetica", 8)
    page.setFillColor(HexColor("#68727D"))
    page.drawString(36, 66, "One-sided ticket. Dotted stub line is decorative; no passenger name or travel date.")
    page.showPage()
    page.save()
    reader = PdfReader(OUT)
    assert len(reader.pages) == 1
    assert tuple(float(v) for v in reader.pages[0].mediabox) == (0.0, 0.0, 612.0, 792.0)
    print(json.dumps({
        "pdf": str(OUT), "pages": len(reader.pages),
        "artwork_pixels": [pixel_width, pixel_height],
        "ticket_size_inches": [7.5, 2.5],
        "effective_image_dpi": [pixel_width / 7.5, pixel_height / 2.5],
        "physical_print_test": False
    }))


if __name__ == "__main__":
    build()
