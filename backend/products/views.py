from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson import ObjectId
from .mongo import product_collection

@api_view(['GET'])
def search_products(request):
    q = request.GET.get("q", "")
    products = product_collection.find(
        {"name": {"$regex": q, "$options": "i"}},
        {"_id": 1, "name": 1}
    )
    data = [{"id": str(p["_id"]), "name": p["name"]} for p in products]
    return Response(data)

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = product_collection.find_one({"_id": ObjectId(pk)})
    except Exception:
        return Response({"error": "Invalid ID"}, status=400)

    if not product:
        return Response({"error": "Product not found"}, status=404)

    product["id"] = str(product["_id"])
    del product["_id"]
    return Response(product)

@api_view(['GET'])
def list_products(request):
    name_filter = request.GET.get("name", "")

    query = {}
    if name_filter:
        query["name"] = {"$regex": name_filter, "$options": "i"}

    products = product_collection.find(query)
    result = []
    for p in products:
        p["id"] = str(p["_id"])
        del p["_id"]
        result.append(p)

    return Response(result)
