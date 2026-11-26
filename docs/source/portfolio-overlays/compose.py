import sys, pymupdf as f
src, out, d = sys.argv[1], sys.argv[2], sys.argv[3]
doc = f.open(src)
snip = lambda n: f.open(f"{d}/{n}.pdf")

def content_bottom(s):
    p = s[0]
    ys = [x['rect'].y1 for x in p.get_drawings() if x['rect'].height < p.rect.height - 1]
    return max(ys)

def place(page, name, target, clip=None):
    s = snip(name)
    page.show_pdf_page(target, s, 0, clip=clip)
    c = clip or s[0].rect
    sx = target.width / c.width; sy = target.height / c.height
    for l in s[0].get_links():
        if l.get('kind') == f.LINK_URI:
            r = l['from']
            page.insert_link({'kind': f.LINK_URI, 'uri': l['uri'], 'from': f.Rect(
                target.x0 + (r.x0 - c.x0) * sx, target.y0 + (r.y0 - c.y0) * sy,
                target.x0 + (r.x1 - c.x0) * sx, target.y0 + (r.y1 - c.y0) * sy)})

def drop_text(page, rect, white=False):
    page.add_redact_annot(rect, fill=(1, 1, 1) if white else None)
    page.apply_redactions(images=f.PDF_REDACT_IMAGE_NONE, graphics=f.PDF_REDACT_LINE_ART_NONE, text=f.PDF_REDACT_TEXT_REMOVE)

# Page 2: stat 16 -> 17, ERP101 -> Itqan, add row 17
p = doc[1]
drop_text(p, f.Rect(479, 92, 505, 118))
place(p, 'stat', f.Rect(461.8, 90.2, 521.8, 120.2))
drop_text(p, f.Rect(440, 389, 533, 399.5), white=True)
place(p, 'idx', f.Rect(305.8 + 100, 386, 305.8 + 226, 400), clip=f.Rect(100, 30, 226, 44))
place(p, 'idx', f.Rect(42.5, 516.8, 289.3, 540.8), clip=f.Rect(0, 0, 246.8, 24))

# Page 4: replace card 04 with Itqan
p = doc[3]
for l in p.get_links():
    if l['from'].y1 < 296: p.delete_link(l)
drop_text(p, f.Rect(40, 44, 556, 294))
p.draw_rect(f.Rect(36, 40, 560, 296), color=None, fill=(1, 1, 1), overlay=True)
place(p, 'itqan', f.Rect(40, 42, 556, 296))

# Page 8: add IPM as card 17 under card 16
p = doc[7]
s = snip('ipm'); h = content_bottom(s) + 4
place(p, 'ipm', f.Rect(40, 255, 556, 255 + h), clip=f.Rect(0, 0, 516, h))

doc.set_metadata({**doc.metadata, 'modDate': f.get_pdf_now()})
doc.save(out, garbage=3, deflate=True)
print('saved', out, 'ipm card height', round(h, 1))
