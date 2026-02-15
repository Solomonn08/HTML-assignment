import http.server
import socketserver
import webbrowser

# Direct URLs
header_bg = "https://cdn.britannica.com/78/249578-050-01D46C9B/Novak-Djokovic-Serbia-US-Open-2023.jpg"
mid_para_img = "https://usdtoreros.com/images/2026/2/8/20260124_USDTennis_vsMiami_007.jpg?width=1416&height=796&mode=crop"
gallery_img_1 = "https://media.strefatenisa.com.pl/public/media/03/96/c3/1727248727/Bez-nazwy-17cF4ac9KERyWt.png?ts=1727248727"
gallery_img_2 = "https://cdn.shopify.com/s/files/1/0935/3694/4470/files/blog-zoom-sur-la-journee-mondiale-du-tennis.jpg"
gallery_img_3 = "https://www.les-pyramides.com/wp-content/uploads/2022/05/conseils-commencer-tennis-scaled.jpg"
gallery_img_4 = "https://img.lemde.fr/2025/05/25/0/0/4386/2924/1440/960/60/0/ebb9299_ftp-import-images-1-dwguqpjr56fv-2025-05-25t121644z-90135228-up1el5p0y3vkh-rtrmadp-3-tennis-frenchopen.JPG"

# Fixed HTML: Using .format() to avoid triple-quote f-string nesting issues
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Ultimate Tennis Guide</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header id="main-header">
        <div class="header-overlay">
            <h1>Mastering the Court</h1>
            <p>From First Swing to Grand Slam Excellence</p>
        </div>
    </header>

    <main class="container">
        <section>
            <h2>The Basics of the Game</h2>
            <p>Tennis is a sport of precision, endurance, and strategy. Whether you are playing singles or doubles, the objective remains the same: hit the ball over the net into the opponent's court.</p>
            
            <div class="mid-section-image">
                <img src="{mid_img}" alt="Tennis Match Action">
                <p class="caption">High-intensity rally during a professional match.</p>
            </div>

            <p>Mastering your footwork is just as important as mastering your swing. Proper positioning allows you to reach the ball earlier and strike with more power.</p>
        </section>

        <section class="card">
            <h3>Essential Gear</h3>
            <ul>
                <li><strong>Professional Racquet:</strong> Balanced for your skill level.</li>
                <li><strong>Court Shoes:</strong> Non-marking soles with side support.</li>
            </ul>
        </section>

        <section>
            <h2>Pro Action Gallery</h2>
            <div class="gallery">
                <img src="{g1}" alt="Begin Your Journey">
                <img src="{g2}" alt="World Tennis Day">
                <img src="{g3}" alt="Pro Tips">
                <img src="{g4}" alt="Technique">
            </div>
        </section>
    </main>
</body>
</html>
"""

# Fixed CSS: Using % formatting for the background URL to keep it clean
css_template = """
body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    background-color: #f4f7f6;
}}
#main-header {{
    background: url('{bg}') no-repeat center center;
    background-size: cover;
    height: 450px;
    width: 100%;
}}
.header-overlay {{
    background: rgba(0, 0, 0, 0.4);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
}}
.container {{
    max-width: 900px;
    margin: -50px auto 40px;
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}}
.mid-section-image img {{
    width: 100%;
    border-radius: 8px;
    border: 5px solid #2e7d32;
}}
.gallery {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
}}
img {{
    width: 100%;
    border-radius: 8px;
}}
"""

# Write the files
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template.format(mid_img=mid_para_img, g1=gallery_img_1, g2=gallery_img_2, g3=gallery_img_3, g4=gallery_img_4))

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css_template.format(bg=header_bg))

PORT = 8000
print(f"Launching at http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")
socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()