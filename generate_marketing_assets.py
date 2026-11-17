import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = r"K:\3. Android & Flutter Apps\Portbot\docs\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)
ICON_PATH = r"K:\3. Android & Flutter Apps\Portbot\assets\portbot_icon_1024.png"

# Color Palette
BG_DARK = (15, 17, 23)        # #0F1117
BG_CARD = (23, 27, 36)        # #171B24
BG_CARD_LIGHT = (30, 35, 48)  # #1E2330
ACCENT_PURPLE = (99, 102, 241)# #6366F1
ACCENT_CYAN = (6, 182, 212)   # #06B6D4
ACCENT_GREEN = (16, 185, 129) # #10B981
ACCENT_YELLOW = (245, 158, 11)# #F59E0B
ACCENT_RED = (239, 68, 68)    # #EF4444
TEXT_WHITE = (255, 255, 255)
TEXT_MUTED = (148, 163, 184)  # #94A3B8
TEXT_DIM = (100, 116, 139)    # #64748B
BORDER_COLOR = (45, 55, 72)   # #2D3748

def get_font(name="segoeui.ttf", size=20, bold=False):
    font_file = "segoeuib.ttf" if bold else "segoeui.ttf"
    path = os.path.join(r"C:\Windows\Fonts", font_file)
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def get_mono_font(size=18):
    try:
        return ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def create_banner():
    W, H = 1280, 640
    img = Image.new("RGBA", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Ambient glow in background
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse([W//2 - 350, -100, W//2 + 350, 400], fill=(99, 102, 241, 45))
    glow_draw.ellipse([W - 300, H - 300, W + 200, H + 200], fill=(6, 182, 212, 35))
    glow_draw.ellipse([-100, H - 300, 400, H + 200], fill=(245, 158, 11, 25))
    glow = glow.filter(ImageFilter.GaussianBlur(60))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)

    # Grid overlay lines for high-tech aesthetic
    for x in range(0, W, 64):
        draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, H, 64):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)

    # Icon
    if os.path.exists(ICON_PATH):
        icon = Image.open(ICON_PATH).convert("RGBA")
        icon = icon.resize((150, 150), Image.Resampling.LANCZOS)
        # Drop shadow behind icon
        shadow = Image.new("RGBA", (170, 170), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(shadow)
        s_draw.ellipse([10, 10, 160, 160], fill=(99, 102, 241, 100))
        shadow = shadow.filter(ImageFilter.GaussianBlur(15))
        img.alpha_composite(shadow, (W//2 - 85, 75))
        img.alpha_composite(icon, (W//2 - 75, 85))

    # Title
    f_title = get_font(size=64, bold=True)
    title_text = "PORTBOT"
    bbox = f_title.getbbox(title_text)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw)//2, 255), title_text, fill=TEXT_WHITE, font=f_title)

    # Subtitle
    f_sub = get_font(size=26, bold=False)
    sub_text = "Run Uncensored Local LLMs Natively On Any Device"
    bbox = f_sub.getbbox(sub_text)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw)//2, 335), sub_text, fill=(203, 213, 225), font=f_sub)

    # Tagline
    f_tag = get_font(size=18, bold=False)
    tag_text = "No Cloud • Zero Subscriptions • Complete Privacy • Built-in OpenAI API"
    bbox = f_tag.getbbox(tag_text)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw)//2, 380), tag_text, fill=TEXT_MUTED, font=f_tag)

    # Feature badges
    badges = [
        ("⚡ 100% Offline AI", ACCENT_YELLOW),
        ("🔓 Zero Censorship", ACCENT_RED),
        ("🌐 Local OpenAI Server", ACCENT_CYAN),
        ("📦 GGUF Model Manager", ACCENT_PURPLE),
        ("📱 Android & Desktop", ACCENT_GREEN)
    ]
    f_badge = get_font(size=16, bold=True)
    total_w = sum(f_badge.getbbox(b[0])[2] - f_badge.getbbox(b[0])[0] + 36 for b in badges) + (len(badges)-1)*12
    cur_x = (W - total_w) // 2
    for text, color in badges:
        bw = f_badge.getbbox(text)[2] - f_badge.getbbox(text)[0] + 32
        draw_rounded_rect(draw, [cur_x, 440, cur_x + bw, 478], radius=19, fill=(color[0], color[1], color[2], 35), outline=(color[0], color[1], color[2], 120), width=1)
        draw.text((cur_x + 16, 448), text, fill=(241, 245, 249), font=f_badge)
        cur_x += bw + 12

    # Developer info footer
    f_dev = get_font(size=16, bold=False)
    dev_text = "Created by NoishiXzen  •  noishixzen@gmail.com  •  aivorygen.netlify.app"
    bbox = f_dev.getbbox(dev_text)
    tw = bbox[2] - bbox[0]
    draw_rounded_rect(draw, [(W - tw)//2 - 24, 535, (W + tw)//2 + 24, 575], radius=12, fill=(23, 27, 36, 200), outline=BORDER_COLOR, width=1)
    draw.text(((W - tw)//2, 544), dev_text, fill=TEXT_MUTED, font=f_dev)

    out_path = os.path.join(OUTPUT_DIR, "portbot-hero-banner.png")
    img.save(out_path, "PNG")
    print("Saved banner to", out_path)

def create_phone_frame(W=800, H=1200):
    img = Image.new("RGBA", (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Ambient back light
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([W//2 - 250, 200, W//2 + 250, 700], fill=(99, 102, 241, 35))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)

    # Phone dimensions
    PW, PH = 540, 1040
    PX, PY = (W - PW)//2, (H - PH)//2

    # Phone drop shadow
    pshadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ps_draw = ImageDraw.Draw(pshadow)
    ps_draw.rounded_rectangle([PX - 15, PY - 10, PX + PW + 15, PY + PH + 25], radius=48, fill=(0, 0, 0, 160))
    pshadow = pshadow.filter(ImageFilter.GaussianBlur(30))
    img.alpha_composite(pshadow)
    draw = ImageDraw.Draw(img)

    # Phone outer bezel
    draw.rounded_rectangle([PX - 8, PY - 8, PX + PW + 8, PY + PH + 8], radius=44, fill=(40, 45, 60), outline=(70, 80, 105), width=2)
    # Phone screen surface
    draw.rounded_rectangle([PX, PY, PX + PW, PY + PH], radius=38, fill=(15, 17, 23))

    # Punch-hole camera & speaker notch
    draw.ellipse([PX + PW//2 - 7, PY + 14, PX + PW//2 + 7, PY + 28], fill=(5, 5, 10))

    # Status Bar
    f_status = get_font(size=14, bold=True)
    draw.text((PX + 32, PY + 14), "9:41", fill=TEXT_MUTED, font=f_status)
    draw.text((PX + PW - 85, PY + 14), "5G  100%", fill=TEXT_MUTED, font=f_status)

    return img, draw, (PX, PY, PW, PH)

def create_chat_screenshot():
    img, draw, (PX, PY, PW, PH) = create_phone_frame()

    # App Header
    # Icon miniature
    if os.path.exists(ICON_PATH):
        icon = Image.open(ICON_PATH).convert("RGBA").resize((38, 38), Image.Resampling.LANCZOS)
        img.alpha_composite(icon, (PX + 24, PY + 52))

    f_appname = get_font(size=22, bold=True)
    draw.text((PX + 72, PY + 50), "Portbot", fill=TEXT_WHITE, font=f_appname)
    
    # Model status badge
    f_modelbadge = get_font(size=13, bold=True)
    draw_rounded_rect(draw, [PX + 72, PY + 76, PX + 245, PY + 98], radius=11, fill=(99, 102, 241, 40), outline=(99, 102, 241, 150), width=1)
    draw.text((PX + 84, PY + 79), "Gemma 2 2B Abliterated", fill=(199, 210, 254), font=f_modelbadge)

    # Speed metrics on right
    f_speed = get_mono_font(size=13)
    draw_rounded_rect(draw, [PX + PW - 135, PY + 60, PX + PW - 24, PY + 88], radius=8, fill=(16, 185, 129, 30), outline=(16, 185, 129, 100), width=1)
    draw.text((PX + PW - 124, PY + 66), "⚡ 28.4 t/s", fill=(52, 211, 153), font=f_speed)

    draw.line([(PX + 20, PY + 112), (PX + PW - 20, PY + 112)], fill=BORDER_COLOR, width=1)

    # Chat Bubbles
    # 1. User Message
    u_y = PY + 130
    draw_rounded_rect(draw, [PX + 120, u_y, PX + PW - 24, u_y + 60], radius=18, fill=(79, 70, 229), outline=(99, 102, 241), width=1)
    f_msg = get_font(size=16)
    draw.text((PX + 140, u_y + 18), "Write an unconstrained fast port scanner in Python.", fill=TEXT_WHITE, font=f_msg)

    # 2. Assistant Response Bubble
    a_y = u_y + 80
    draw_rounded_rect(draw, [PX + 24, a_y, PX + PW - 40, a_y + 570], radius=20, fill=BG_CARD, outline=BORDER_COLOR, width=1)
    
    # Assistant Header
    draw.ellipse([PX + 42, a_y + 18, PX + 62, a_y + 38], fill=ACCENT_YELLOW)
    f_asst = get_font(size=14, bold=True)
    draw.text((PX + 72, a_y + 19), "Portbot (Local Engine)", fill=(241, 245, 249), font=f_asst)
    f_time = get_font(size=12)
    draw.text((PX + PW - 130, a_y + 21), "0.38s to first token", fill=TEXT_DIM, font=f_time)

    f_text = get_font(size=15)
    intro = "Here is a multithreaded socket scanner for maximum speed:"
    draw.text((PX + 42, a_y + 52), intro, fill=(226, 232, 240), font=f_text)

    # Code Block Box
    code_y = a_y + 85
    draw_rounded_rect(draw, [PX + 38, code_y, PX + PW - 54, code_y + 350], radius=12, fill=(13, 15, 20), outline=(51, 65, 85), width=1)
    f_mono = get_mono_font(size=13)
    code_lines = [
        ("# High-concurrency socket port scanner", (100, 116, 139)),
        ("import socket, concurrent.futures", (147, 197, 253)),
        ("", (255, 255, 255)),
        ("def scan_port(target, port):", (244, 114, 182)),
        ("    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)", (226, 232, 240)),
        ("    s.settimeout(0.4)", (226, 232, 240)),
        ("    if s.connect_ex((target, port)) == 0:", (52, 211, 153)),
        ("        print(f'[+] Port {port} OPEN')", (52, 211, 153)),
        ("    s.close()", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("with concurrent.futures.ThreadPoolExecutor(100) as ex:", (244, 114, 182)),
        ("    for p in range(1, 1024):", (226, 232, 240)),
        ("        ex.submit(scan_port, '127.0.0.1', p)", (226, 232, 240)),
    ]
    for idx, (line, col) in enumerate(code_lines):
        draw.text((PX + 52, code_y + 16 + idx * 24), line, fill=col, font=f_mono)

    # Post code text
    draw.text((PX + 42, code_y + 365), "✓ Full multi-core execution", fill=TEXT_MUTED, font=f_text)
    draw.text((PX + 42, code_y + 395), "✓ Completely unfiltered output with no disclaimers", fill=(245, 158, 11), font=f_text)
    draw.text((PX + 42, code_y + 425), "✓ Completed in 2.1s (62 tokens total)", fill=TEXT_DIM, font=f_text)

    # Bottom Input Bar
    in_y = PY + PH - 110
    draw_rounded_rect(draw, [PX + 24, in_y, PX + PW - 85, in_y + 54], radius=27, fill=BG_CARD_LIGHT, outline=BORDER_COLOR, width=1)
    f_placeholder = get_font(size=16)
    draw.text((PX + 48, in_y + 16), "Ask anything with zero restrictions...", fill=TEXT_DIM, font=f_placeholder)

    # Send button
    draw.ellipse([PX + PW - 75, in_y, PX + PW - 21, in_y + 54], fill=(99, 102, 241))
    # Arrow icon
    draw.polygon([(PX + PW - 53, in_y + 19), (PX + PW - 53, in_y + 35), (PX + PW - 38, in_y + 27)], fill=TEXT_WHITE)

    # Bottom home indicator
    draw.rounded_rectangle([PX + PW//2 - 65, PY + PH - 20, PX + PW//2 + 65, PY + PH - 15], radius=3, fill=(100, 116, 139))

    out_path = os.path.join(OUTPUT_DIR, "portbot-screenshot-chat.png")
    img.save(out_path, "PNG")
    print("Saved chat screenshot to", out_path)

def create_models_screenshot():
    img, draw, (PX, PY, PW, PH) = create_phone_frame()

    # Header
    f_title = get_font(size=24, bold=True)
    draw.text((PX + 28, PY + 48), "Model Catalog", fill=TEXT_WHITE, font=f_title)
    f_sub = get_font(size=13)
    draw.text((PX + 28, PY + 80), "Download and run local GGUF weights directly", fill=TEXT_MUTED, font=f_sub)

    # Filters
    filters = [("All", True), ("Downloaded", False), ("Uncensored", False), ("Custom GGUF", False)]
    fx = PX + 28
    f_filt = get_font(size=14, bold=True)
    for name, active in filters:
        fw = f_filt.getbbox(name)[2] - f_filt.getbbox(name)[0] + 28
        col = (99, 102, 241) if active else (30, 35, 48)
        border = (129, 140, 248) if active else BORDER_COLOR
        draw_rounded_rect(draw, [fx, PY + 115, fx + fw, PY + 148], radius=16, fill=col, outline=border, width=1)
        draw.text((fx + 14, PY + 122), name, fill=TEXT_WHITE if active else TEXT_MUTED, font=f_filt)
        fx += fw + 10

    # Model Cards
    cards_data = [
        {
            "name": "Gemma 2 2B Abliterated",
            "tag": "RECOMMENDED · FASTEST",
            "type": "UNCENSORED",
            "size": "1.6 GB",
            "ram": "4 GB RAM min",
            "status": "LOADED & ACTIVE",
            "color": ACCENT_GREEN
        },
        {
            "name": "Gemma 4 E4B Heretic",
            "tag": "HERETIC EDITION",
            "type": "UNCENSORED",
            "size": "5.3 GB",
            "ram": "8 GB RAM min",
            "status": "DOWNLOADED",
            "color": ACCENT_PURPLE
        },
        {
            "name": "Dolphin 2.9 Llama 3 8B",
            "tag": "CREATIVE & LOGIC",
            "type": "UNCENSORED",
            "size": "4.9 GB",
            "ram": "8 GB RAM min",
            "status": "DOWNLOAD",
            "color": ACCENT_CYAN
        },
        {
            "name": "Phi-3.5 Mini 3.8B",
            "tag": "LIGHTWEIGHT REASONING",
            "type": "STANDARD",
            "size": "2.2 GB",
            "ram": "4 GB RAM min",
            "status": "DOWNLOAD",
            "color": TEXT_MUTED
        }
    ]

    cy = PY + 170
    for c in cards_data:
        draw_rounded_rect(draw, [PX + 24, cy, PX + PW - 24, cy + 175], radius=18, fill=BG_CARD, outline=BORDER_COLOR, width=1)
        
        # Tag
        f_tag = get_font(size=11, bold=True)
        draw_rounded_rect(draw, [PX + 40, cy + 16, PX + 40 + f_tag.getbbox(c['tag'])[2] + 16, cy + 36], radius=6, fill=(99, 102, 241, 30), outline=(99, 102, 241, 100), width=1)
        draw.text((PX + 48, cy + 19), c['tag'], fill=(165, 180, 252), font=f_tag)

        # Uncensored Pill
        f_pill = get_font(size=11, bold=True)
        tx = PX + PW - 40 - (f_pill.getbbox(c['type'])[2] + 16)
        pill_col = ACCENT_RED if c['type'] == "UNCENSORED" else (71, 85, 105)
        draw_rounded_rect(draw, [tx, cy + 16, tx + f_pill.getbbox(c['type'])[2] + 16, cy + 36], radius=6, fill=(pill_col[0], pill_col[1], pill_col[2], 40), outline=pill_col, width=1)
        draw.text((tx + 8, cy + 19), c['type'], fill=(254, 202, 202) if c['type'] == "UNCENSORED" else TEXT_MUTED, font=f_pill)

        # Model Title
        f_mtitle = get_font(size=18, bold=True)
        draw.text((PX + 40, cy + 46), c['name'], fill=TEXT_WHITE, font=f_mtitle)

        # Specs
        f_spec = get_font(size=13)
        specs = f"💾 Size: {c['size']}   •   🧠 Min: {c['ram']}"
        draw.text((PX + 40, cy + 76), specs, fill=TEXT_MUTED, font=f_spec)

        # Action Button / Status
        f_btn = get_font(size=13, bold=True)
        btn_w = 150
        btn_x = PX + PW - 40 - btn_w
        btn_y = cy + 115
        
        if "ACTIVE" in c['status']:
            draw_rounded_rect(draw, [btn_x, btn_y, btn_x + btn_w, btn_y + 40], radius=10, fill=(16, 185, 129, 35), outline=ACCENT_GREEN, width=1)
            draw.text((btn_x + 18, btn_y + 11), "● ACTIVE MODEL", fill=(52, 211, 153), font=f_btn)
        elif c['status'] == "DOWNLOADED":
            draw_rounded_rect(draw, [btn_x, btn_y, btn_x + btn_w, btn_y + 40], radius=10, fill=(99, 102, 241), outline=(129, 140, 248), width=1)
            draw.text((btn_x + 36, btn_y + 11), "LOAD MODEL", fill=TEXT_WHITE, font=f_btn)
        else:
            draw_rounded_rect(draw, [btn_x, btn_y, btn_x + btn_w, btn_y + 40], radius=10, fill=BG_CARD_LIGHT, outline=BORDER_COLOR, width=1)
            draw.text((btn_x + 34, btn_y + 11), "DOWNLOAD", fill=(203, 213, 225), font=f_btn)

        # Storage indicator
        draw.text((PX + 40, cy + 125), "llama.cpp GGUF Q4_K_M", fill=TEXT_DIM, font=get_mono_font(size=12))

        cy += 195

    # Floating Action: Import custom GGUF
    fab_y = PY + PH - 80
    draw_rounded_rect(draw, [PX + 32, fab_y, PX + PW - 32, fab_y + 48], radius=24, fill=(99, 102, 241), outline=(129, 140, 248), width=1)
    f_fab = get_font(size=15, bold=True)
    draw.text((PX + PW//2 - 90, fab_y + 14), "➕ Import Custom .GGUF File", fill=TEXT_WHITE, font=f_fab)

    out_path = os.path.join(OUTPUT_DIR, "portbot-screenshot-models.png")
    img.save(out_path, "PNG")
    print("Saved models screenshot to", out_path)

def create_api_screenshot():
    img, draw, (PX, PY, PW, PH) = create_phone_frame()

    # Header
    f_title = get_font(size=24, bold=True)
    draw.text((PX + 28, PY + 48), "Local OpenAI Server", fill=TEXT_WHITE, font=f_title)
    f_sub = get_font(size=13)
    draw.text((PX + 28, PY + 80), "Connect Open-WebUI, Cursor, Obsidian & scripts", fill=TEXT_MUTED, font=f_sub)

    # Server Status Card
    sy = PY + 120
    draw_rounded_rect(draw, [PX + 24, sy, PX + PW - 24, sy + 140], radius=18, fill=BG_CARD, outline=(16, 185, 129, 120), width=1)
    
    # Pulse status icon
    draw.ellipse([PX + 44, sy + 24, PX + 64, sy + 44], fill=ACCENT_GREEN)
    f_status = get_font(size=18, bold=True)
    draw.text((PX + 74, sy + 22), "Server Running", fill=TEXT_WHITE, font=f_status)
    f_port = get_mono_font(size=15)
    draw.text((PX + 74, sy + 50), "http://127.0.0.1:4891/v1", fill=ACCENT_CYAN, font=f_port)

    # Toggle Button
    draw_rounded_rect(draw, [PX + PW - 90, sy + 24, PX + PW - 44, sy + 50], radius=13, fill=ACCENT_GREEN)
    draw.ellipse([PX + PW - 66, sy + 27, PX + PW - 47, sy + 47], fill=TEXT_WHITE)

    # Server stats bar
    draw.line([(PX + 40, sy + 88), (PX + PW - 40, sy + 88)], fill=BORDER_COLOR, width=1)
    f_stat = get_font(size=12)
    draw.text((PX + 40, sy + 102), "Active Requests: 1", fill=TEXT_MUTED, font=f_stat)
    draw.text((PX + 210, sy + 102), "Uptime: 04h 12m", fill=TEXT_MUTED, font=f_stat)
    draw.text((PX + PW - 150, sy + 102), "Latency: 12ms", fill=TEXT_MUTED, font=f_stat)

    # API Endpoints list
    ey = sy + 160
    draw.text((PX + 28, ey), "Supported Endpoints", fill=(241, 245, 249), font=get_font(size=18, bold=True))

    endpoints = [
        ("GET", "/v1/models", "List loaded models & weights"),
        ("POST", "/v1/chat/completions", "OpenAI streaming & standard chat"),
        ("POST", "/v1/completions", "Legacy text completion format")
    ]
    ey += 35
    f_ep = get_mono_font(size=13)
    f_desc = get_font(size=12)
    for m, p, d in endpoints:
        draw_rounded_rect(draw, [PX + 24, ey, PX + PW - 24, ey + 60], radius=12, fill=BG_CARD, outline=BORDER_COLOR, width=1)
        # Method badge
        m_col = ACCENT_CYAN if m == "GET" else ACCENT_PURPLE
        draw_rounded_rect(draw, [PX + 36, ey + 15, PX + 92, ey + 45], radius=6, fill=(m_col[0], m_col[1], m_col[2], 35), outline=m_col, width=1)
        draw.text((PX + 46, ey + 21), m, fill=m_col, font=get_font(size=12, bold=True))
        draw.text((PX + 105, ey + 15), p, fill=TEXT_WHITE, font=f_ep)
        draw.text((PX + 105, ey + 36), d, fill=TEXT_MUTED, font=f_desc)
        ey += 72

    # Quick cURL snippet box
    draw.text((PX + 28, ey + 10), "Quick Test Command", fill=(241, 245, 249), font=get_font(size=18, bold=True))
    box_y = ey + 42
    draw_rounded_rect(draw, [PX + 24, box_y, PX + PW - 24, box_y + 240], radius=14, fill=(10, 12, 16), outline=BORDER_COLOR, width=1)
    
    curl_code = [
        ("curl http://127.0.0.1:4891/v1/chat/completions \\", (245, 158, 11)),
        ("  -H 'Content-Type: application/json' \\", (148, 163, 184)),
        ("  -d '{", (226, 232, 240)),
        ("    \"model\": \"local\",", (147, 197, 253)),
        ("    \"stream\": true,", (244, 114, 182)),
        ("    \"messages\": [", (226, 232, 240)),
        ("      {\"role\": \"user\", \"content\": \"Analyze...\"}", (52, 211, 153)),
        ("    ]", (226, 232, 240)),
        ("  }'", (226, 232, 240))
    ]
    for idx, (cl, ccol) in enumerate(curl_code):
        draw.text((PX + 38, box_y + 16 + idx * 23), cl, fill=ccol, font=get_mono_font(size=13))

    # Bottom notice
    draw.text((PX + 32, box_y + 255), "🔒 Requests processed completely offline on localhost", fill=TEXT_MUTED, font=get_font(size=12))

    out_path = os.path.join(OUTPUT_DIR, "portbot-screenshot-api.png")
    img.save(out_path, "PNG")
    print("Saved API screenshot to", out_path)

if __name__ == "__main__":
    create_banner()
    create_chat_screenshot()
    create_models_screenshot()
    create_api_screenshot()
    print("All marketing images generated successfully!")
