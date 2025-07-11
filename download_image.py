import os
import requests

urls = [
    "https://www.dibaramasonry.com/images/photo-gallery/5-Gray-Block-Wall-Accomodating-Existing-Tree.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/6-Standard-Gray-Block-Wall.1).1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/6-Standard-Gray-Block-Wall.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/6-Tan-Block-Wall-with-2-Vinyl-Fence-Topper.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/6-Tan-Block-Wall-with-Balboa-Caps.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/75-Long-Stepped-Block-Wall-With-Stucco-and-Paint.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/75-Long-Stepped-Gray-Block-Wall.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Basket-Weave-Brick-Patio-Patios-Walkways-579x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Brick-and-Pillar-Planter-to-Match-Existing-Brick-Walls-1030x437.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Concerete-Patio-with-Brick-Stair-Tread-1030x359.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Concrete-Patio-1030x398.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Damaged-Stucco-and-Block-Wall.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-New-100-Long-Gray-Block-Wall-1030x527.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-New-Block-Wall-To-Match-Existing-1030x579.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-New-Brick-Retaining-Wall-with-Proper-Drainage-Brick-Walls-1030x453.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Properly-Graded-Driveway-Apron-and-Adjacent-Pavers-1030x417.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Settled-and-Cracked-Concrete-Drvieway-1030x589.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-The-Paramour-Mansion-Replaced-Concrete-Pillar-Cap-1030x764.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Before-After-Tile-Patio-1030x918.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Bel-Air-Estate-Column-Repointing-and-Restoration-Historical-Restoration-1030x773.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Bel-Air-Estate-Pool-Coping-and-Re-Grouting-Restoration-Historical-Restoration-1030x773.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Blue-Stone-Patio-Patios-Walkways-1030x579.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Brick-Patio-Powerwashing-Patios-Walkways-618x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Brick-Patio-with-Basket-Weave-Pattern-2-Patios-Walkways-1030x773.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Brick-Patio-with-Basket-Weave-Pattern-Patios-Walkways-1030x773.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Entryway-Stone-Pillars-Stone-Walls-Veneers-1030x657.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Exterior-Fireplace-Stone-Veener-2-Stone-Walls-Veneers-618x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Exterior-Fireplace-Stone-Veneer-Stone-Walls-Veneers-618x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Flagstone-and-Decomposed-Granite-Approach-Patios-Walkways-1030x579.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Flagstone-Walkway-2-Patios-Walkways-579x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Flagstone-Walkway-Patios-Walkways-1030x579.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Front-Entry-Brick-Pillars-with-Stuccoed-Block-Walls-Brick-Walls-579x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Interior-Fireplace-Stone-Veneer-Stone-Walls-Veneers-773x1030.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Interlocking-Block-Wall-with-Paver-Patio-Patios-Walkways-1030x773.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Patio-with-Boarder-Patios-Walkways-1030x773.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Paver-Driveway-with-Wet-Look-Sealer-2-Patios-Walkways-579x1030.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Paver-Driveway-with-Wet-Look-Sealer-Patios-Walkways-579x1030.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Spanish-Tile-Serpantine-Wall-2-Patios-Walkways-579x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Spanish-Tile-Serpentine-Wall-Patios-Walkways-579x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Step-1-Excavated-Portion-of-Leaking-Foundation.-Step-2-Foundation-Coated-with-Waterproofing-Membrane.-Step-3-Foundation-is-Infilled-and-Landscaped-914x1030.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Tujunga-Malibu-Cobble-Stone-Wall-and-Custom-Cut-Flagstone-Cap-Stone-Walls-Veneers-1030x618.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Tujunga-Malibu-Cobble-Stone-Wall-and-Putting-Green-2-Stone-Walls-Veneers-1030x1030.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/Tujunga-Malibu-Cobble-Stone-Wall-and-Putting-Green-Stone-Walls-Veneers-1030x1030.1811121535550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/1.2108250950140.png",
    "https://www.dibaramasonry.com/images/photo-gallery/10.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/11.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/12.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/13.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/15.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/16.2108250950550.jpg",
    "https://www.dibaramasonry.com/images/photo-gallery/2.2108250950164.png",
    "https://www.dibaramasonry.com/images/photo-gallery/3.2108250950180.png",
    "https://www.dibaramasonry.com/images/photo-gallery/7.2312061431453.jpg"
]

save_dir = r"C:\Users\roy\OneDrive\Documents\Dibara Masonry\recent_project\our_work"
os.makedirs(save_dir, exist_ok=True)

for url in urls:
    filename = os.path.basename(url.split("?")[0])
    save_path = os.path.join(save_dir, filename)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
