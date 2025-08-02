import os
import requests

urls = [
   "https://www.windowworksnc.com/wp-content/uploads/2025/06/June-Blog-2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/06/image3.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/06/image4.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/05/Window-Works-Blog-Graphic-2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/05/4-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/04/Mar-Blog2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/02/Feb-blog-2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/06/June-Blog-2-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/05/image2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/05/Window-Works-Blog-Graphic.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/04/Mar-Blog-2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/04/Mar-Blog1-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/02/Feb-blog-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/12/1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/08/pinterest-broken-front-door-glass.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/08/pinterest-The-5-Hidden-Costs-of-Wood-Doors-in-Raleigh-NC.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2025/01/Jan-Blog-2.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-window-sizes.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/07/pinterest-windows-inside-or-outside.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/08/pinterest-right-size-window.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-impact-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-how-long-should-a-front-door-last.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-pre-hung-door-is-better-than-slab.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-door-height.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2021/11/Window-Works-Co.-Black-Windows-Brick-Home.png",
"https://www.windowworksnc.com/wp-content/uploads/2021/11/Springline_Entranceway_5369.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/mod-home-.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/08/featured-dont-do-to-front-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-provia-doors.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/standard-door-shipping.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/provia-doors-shipping.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-storm-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/03/pinterest-reselling-windows-online.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/03/reselling-windows-online-facebook-marketplace-post-image-e1709682403649.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/04/pinterest-grille-mistakes.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-slim-vertical-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-Condensation-Outside-Your-Windows-Separating-Fact-from-Fiction.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-Replacing-Windows-Increase-Home-Value.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-cladding-on-a-window.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/11/money-saving-pin.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-pet-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-interior-dutch.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2024/01/pinterest-multipoint-lock-maintenance.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/07/pinterest-thermal-break-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/02/pinterest-season-for-door-replacement.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/10/pinterest-2023-energy-star-ratings-updates.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/10/2023-Energy-Star-Changes.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/07/pinterest-pass-through-window.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/05/pinterest-bad-window-installation.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/04/pinterest-double-hung.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/11/pinterest-install-own-andersen-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/07/pinterest-door-hardware-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/08/pinterest-prefinished.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/08/pinterest-doors-cost-so-much.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/04/pinterest-love-dsa.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/01/Pinterest-Patio-door-with-built-in-blinds.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/01/Pinterest-arch-top-round-top-front-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-sidelights-and-transoms.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/04/pinterest-energy-windows-new-construction.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/04/pinterest-rookie-assumptions.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/01/Pinterest-window-measure-appointment.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/02/pinterest-japandi-style-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-window-warranty-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-researching-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-full-frame-versus-insert-replacement-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/full-frame-versus-insert-printable.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-2023-door-trends.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/patio-door-featured-.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2021/12/IMG_2090.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-ADA-Compliant-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2023/02/pinterest-door-security.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-replacing-a-window-with-a-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-bad-window-design.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/06/pinterest-brickmould.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/pinterest-3-scary-things.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/window-water-damage.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/window-gourds.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/pinterest-replace-some-of-my-windows.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/plans-blueprints.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/plans-blueprints-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/07/pinterest-vinyl-window-features.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/03/pinterest-so-expensive-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/pinterest-historic-home-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/true-divided-lites.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/two-black-doors-different-sticking.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/09/Blog-Graphic-Dutch-Door-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/05/featured-dutch-1.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/08/pinterest-dont-do-these-door.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/pinterest-sliding-featurers-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Door-parts-printable-png-11-×-8.5-in-1-1024x791.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Pinterest-parts-of-a-door-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Pinterest_dont-install-your-own-door-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/pinterest-patio-door-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2021/11/400_Series_Tilt-Wash_Double-Hung_Windows_Frenchwood_Hinged_Patio_Door_11545.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/200_Series_Hinged_Inswing_Patio_Door_498-769x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2021/11/Anderson-Photo-4-copy-1024x683.png",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/patio-door-featured-.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Pinterest-do-i-have-aw-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/AW-logo-on-windw.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Andersen_Lumber_1903.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/03/pin_5-Steps-to-Get-Ready-for-Window-Installation-Day-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/04/Pinterest_Andersen-window-series-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/04/Capture-1024x684.png",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/E-Series_Double-Hung_Windows_15385-1024x683.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/E-Series_Picture_Windows_17160-1024x683.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/A-Series_Casement_Picture_Windows_Frenchwood_Gliding_Patio_Door_14479-1024x896.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/400_Series_Casement_Picture_Windows_with_Stormwatch_Protection_17334-1024x683.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/200_Series_Double-Hung_Windows_478-1024x806.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/01/100_Series_Single-Hung_Windows_11143-1024x683.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/Pinterest-fog-683x1024.jpg",
"https://www.windowworksnc.com/wp-content/uploads/2022/02/pin_replace-wood-door-683x1024.jpg",
]


save_dir = r"C:\Users\roy\OneDrive\Desktop\Roy\Projects\Workspace\projects\dibara_masonry\image\blogs_post_content"
os.makedirs(save_dir, exist_ok=True)

for url in urls:
    filename = os.path.basename(url.split("?")[0])
    save_path = os.path.join(save_dir, filename)
    if os.path.exists(save_path):
        print(f"Skipped (already exists): {filename}")
        continue
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
