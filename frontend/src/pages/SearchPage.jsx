import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function SearchPage() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [allProducts, setAllProducts] = useState([]);
  const navigate = useNavigate();

  // Fetch all products on mount for showing 2-3 products always
  useEffect(() => {
    axios
      .get("https://machine-test-backend-ajw9.onrender.com/products/")
      .then((res) => setAllProducts(res.data))
      .catch(() => setAllProducts([]));
  }, []);

  // Fetch search results as the user types
  useEffect(() => {
    const delay = setTimeout(() => {
      if (query.trim()) {
        setLoading(true);
        axios
          .get(`https://machine-test-backend-ajw9.onrender.com/products/?name=${query}`)
          .then((res) => setResults(res.data))
          .catch(() => setResults([]))
          .finally(() => setLoading(false));
      } else {
        setResults([]);
        setLoading(false);
      }
    }, 300);

    return () => clearTimeout(delay);
  }, [query]);

  // Helper to get product id (handles both _id and id)
  const getProductId = (p) => p._id || p.id;

  return (
    <div className="bg-gradient-to-br from-indigo-100 to-blue-200 min-h-screen px-2 sm:px-4 py-6">
      <div className="bg-white/30 backdrop-blur-md rounded-3xl shadow-xl p-4 sm:p-8 md:p-10 w-full max-w-2xl border border-white/50 mx-auto mt-6 sm:mt-10">
        <h1 className="text-3xl sm:text-4xl font-bold text-gray-800 mb-3 sm:mb-4 text-center">
          Find Your Product
        </h1>
        <p className="text-center text-gray-600 mb-6 sm:mb-8 text-sm sm:text-base">
          Search thousands of items in one place
        </p>

        <input
          className="w-full p-3 sm:p-4 rounded-xl text-base sm:text-lg bg-white/80 border border-gray-200 shadow-inner placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-400"
          placeholder="Search for iphones, samsung, and more..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        {/* Always show 2–3 products below search bar if not searching */}
        {!query.trim() && allProducts.length > 0 && (
          <ul className="mt-6 grid grid-cols-1 xs:grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6">
            {allProducts.slice(0, 3).map((p) => {
              const productId = getProductId(p);
              if (!productId) {
                console.error("Product missing id:", p);
                return null;
              }
              return (
                <button
                  key={productId}
                  className="bg-white rounded-xl p-3 sm:p-4 shadow flex flex-col items-center cursor-pointer hover:bg-blue-50 transition border-0 w-full"
                  style={{ border: "none" }}
                  onClick={() => navigate(`/product/${productId}`)}
                >
                  <img
                    src={p.image}
                    alt={p.name}
                    className="w-20 h-20 sm:w-24 sm:h-24 rounded-lg object-cover mb-2"
                  />
                  <div className="font-medium text-gray-800 text-center">{p.name}</div>
                  <div className="text-sm text-gray-500 text-center">₹{p.price}</div>
                </button>
              );
            })}
          </ul>
        )}

        {/* Search results (suggestions) */}
        {query.trim() && (
          <>
            {loading && (
              <div className="text-center text-gray-600 mt-4">Searching...</div>
            )}

            {!loading && results.length === 0 && (
              <div className="text-center text-gray-500 mt-6 bg-white/90 p-4 rounded-xl shadow">
                ❌ No products found for "<strong>{query}</strong>"
              </div>
            )}

            {results.length > 0 && (
              <ul className="mt-6 bg-white rounded-xl shadow-lg divide-y overflow-hidden">
                {results.slice(0, 3).map((p) => {
                  const productId = getProductId(p);
                  if (!productId) {
                    console.error("Product missing id:", p);
                    return null;
                  }
                  return (
                    <button
                      key={productId}
                      className="w-full text-left p-3 sm:p-4 flex items-center gap-3 sm:gap-4 hover:bg-gray-50 cursor-pointer"
                      style={{ border: "none" }}
                      onClick={() => navigate(`/product/${productId}`)}
                    >
                      <img
                        src={p.image}
                        alt={p.name}
                        className="w-12 h-12 sm:w-14 sm:h-14 rounded-lg object-cover"
                      />
                      <div>
                        <div className="font-medium text-gray-800">{p.name}</div>
                        <div className="text-sm text-gray-500">₹{p.price}</div>
                      </div>
                    </button>
                  );
                })}
              </ul>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default SearchPage;
