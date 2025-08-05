from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["myproducts"]
products = db["products"]

# ✅ Clear existing documents
products.delete_many({})

sample = [
    {
        "name": "Iphone",
        "price": 1299.99,
        "description": "Apple flagship",
        "image": "https://qgzrsclvzqvnbzsdnnsf.supabase.co/storage/v1/object/sign/machine.test/712SuRmHG4L._UF1000,1000_QL80_.jpg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV80Nzc5MTdkOS00NWRiLTRkN2MtYWY1NS0xMmU4ZmNmMWUxYTAiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJtYWNoaW5lLnRlc3QvNzEyU3VSbUhHNEwuX1VGMTAwMCwxMDAwX1FMODBfLmpwZyIsImlhdCI6MTc1NDI4NDIzOCwiZXhwIjoxNzU2ODc2MjM4fQ.UBrAVfvWPT8fkj0sv-swLF5C-EP7u_Op2xRJpZHypBw"
    },
    {
        "name": "Galaxy S23",
        "price": 999.99,
        "description": "Samsung premium",
        "image": "https://example.com/galaxy.jpg"
    },
    {
        "name": "Samsung S23",
        "price": 999.99,
        "description": "Samsung premium",
        "image": "https://qgzrsclvzqvnbzsdnnsf.supabase.co/storage/v1/object/sign/machine.test/712SuRmHG4L._UF1000,1000_QL80_.jpg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV80Nzc5MTdkOS00NWRiLTRkN2MtYWY1NS0xMmU4ZmNmMWUxYTAiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJtYWNoaW5lLnRlc3QvNzEyU3VSbUhHNEwuX1VGMTAwMCwxMDAwX1FMODBfLmpwZyIsImlhdCI6MTc1NDI4NDIzOCwiZXhwIjoxNzU2ODc2MjM4fQ.UBrAVfvWPT8fkj0sv-swLF5C-EP7u_Op2xRJpZHypBw"
    },
    {
        "name": "MacBook Pro 16",
        "price": 2499.99,
        "description": "Apple laptop high-end",
        "image": "https://example.com/macbookpro16.jpg"
    },
    {
        "name": "Dell XPS 13",
        "price": 1399.99,
        "description": "Dell premium ultrabook",
        "image": "https://example.com/dellxps13.jpg"
    },
    {
        "name": "HP Spectre x360",
        "price": 1499.99,
        "description": "HP convertible laptop",
        "image": "https://example.com/hpspectrex360.jpg"
    },
    {
        "name": "Google Pixel 7",
        "price": 699.99,
        "description": "Google flagship phone",
        "image": "https://example.com/pixel7.jpg"
    },
    {
        "name": "OnePlus 11",
        "price": 899.99,
        "description": "OnePlus high performance",
        "image": "https://example.com/oneplus11.jpg"
    },
    {
        "name": "Lenovo ThinkPad X1",
        "price": 1599.99,
        "description": "Business laptop",
        "image": "https://example.com/thinkpadx1.jpg"
    },
    {
        "name": "Asus ROG Zephyrus",
        "price": 1799.99,
        "description": "Gaming laptop",
        "image": "https://example.com/rogzephyrus.jpg"
    },
    {
        "name": "Acer Predator Helios",
        "price": 1899.99,
        "description": "Gaming laptop Acer",
        "image": "https://example.com/predatorhelios.jpg"
    },
    {
        "name": "Sony Xperia 1 V",
        "price": 1099.99,
        "description": "Sony flagship phone",
        "image": "https://example.com/xperia1v.jpg"
    },
    {
        "name": "Motorola Edge 30",
        "price": 699.99,
        "description": "Motorola premium phone",
        "image": "https://example.com/motoedge30.jpg"
    },
    {
        "name": "Surface Laptop 5",
        "price": 1299.99,
        "description": "Microsoft premium laptop",
        "image": "https://example.com/surfacelaptop5.jpg"
    },
    {
        "name": "Razer Blade 15",
        "price": 2199.99,
        "description": "Razer gaming laptop",
        "image": "https://example.com/razerblade15.jpg"
    },
    {
        "name": "LG Gram 17",
        "price": 1499.99,
        "description": "Lightweight laptop LG",
        "image": "https://example.com/lggram17.jpg"
    },
    {
        "name": "Dell Alienware M15",
        "price": 1999.99,
        "description": "Alienware gaming laptop",
        "image": "https://example.com/alienwarem15.jpg"
    },
    {
        "name": "Apple iMac 24",
        "price": 1799.99,
        "description": "Apple desktop",
        "image": "https://example.com/imac24.jpg"
    },
    {
        "name": "Lenovo Legion 5",
        "price": 1499.99,
        "description": "Lenovo gaming laptop",
        "image": "https://example.com/legion5.jpg"
    },
    {
        "name": "MSI Stealth 15M",
        "price": 1699.99,
        "description": "MSI gaming laptop",
        "image": "https://example.com/msistealth15m.jpg"
    },
    {
        "name": "Asus Vivobook 15",
        "price": 799.99,
        "description": "Asus everyday laptop",
        "image": "https://example.com/vivobook15.jpg"
    },
    {
        "name": "Google Pixel 6a",
        "price": 449.99,
        "description": "Google budget phone",
        "image": "https://example.com/pixel6a.jpg"
    },
    {
        "name": "Samsung Galaxy Book 3",
        "price": 1399.99,
        "description": "Samsung laptop",
        "image": "https://example.com/galaxybook3.jpg"
    }
]


products.insert_many(sample)
print("✅ Sample products inserted (old ones cleared).")
