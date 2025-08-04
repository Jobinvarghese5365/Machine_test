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
    }
]

products.insert_many(sample)
print("✅ Sample products inserted (old ones cleared).")
