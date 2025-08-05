import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

function ProductDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    axios
      .get(`https://machine-test-backend-ajw9.onrender.com/product/${id}`)
      .then((res) => setProduct(res.data))
      .catch(console.error);
  }, [id]);

  if (!product)
    return <p className="p-4 text-center text-lg sm:text-xl">Loading...</p>;

  return (
    <div className="min-h-screen bg-gradient-to-tr from-gray-50 to-gray-200 flex items-center justify-center px-2 sm:px-4 py-6">
      <div className="bg-white rounded-2xl shadow-2xl overflow-hidden w-full max-w-lg sm:max-w-2xl lg:max-w-6xl flex flex-col lg:flex-row relative">
        {/* 🔙 Back Button inside the card */}
        <button
          onClick={() => navigate(-1)}
          className="absolute top-2 left-2 sm:top-4 sm:left-4 p-2 rounded-full bg-white border border-gray-300 shadow-md hover:bg-gray-100 transition z-10"
        >
          <svg
            className="w-5 h-5 text-gray-700"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>

        {/* Left: Product Image */}
        <div className="w-full lg:w-1/2 bg-white p-4 sm:p-8 flex flex-col justify-center items-center">
          <img
            src={product.image}
            alt={product.name}
            className="w-48 h-48 sm:w-64 sm:h-64 md:w-80 md:h-80 object-contain mb-4 sm:mb-6 drop-shadow-xl rounded-xl"
          />
          <div className="flex gap-2">
            {[...Array(1)].map((_, i) => (
              <div
                key={i}
                className="w-10 h-10 sm:w-16 sm:h-16 bg-gray-100 rounded-lg border flex items-center justify-center"
              >
                <img
                  src={product.image}
                  alt={`thumb-${i}`}
                  className="w-8 h-8 sm:w-12 sm:h-12 object-contain"
                />
              </div>
            ))}
          </div>
        </div>

        {/* Right: Product Info */}
        <div className="w-full lg:w-1/2 p-4 sm:p-8 flex flex-col justify-between">
          <div>
            <h1 className="text-2xl sm:text-3xl font-bold text-gray-800 mb-2">
              {product.name}
            </h1>

            <p className="text-xl sm:text-2xl font-bold text-green-600 mb-1">
              ₹{product.price}
            </p>

            <p className="text-gray-500 text-sm sm:text-base mb-4">{product.description}</p>

            <p className="text-xs text-gray-500 mb-6">(Inclusive of all taxes)</p>

            <button className="bg-green-600 hover:bg-green-700 transition-all duration-200 text-white font-semibold px-4 py-2 sm:px-6 sm:py-3 rounded-xl shadow-md w-full sm:w-auto">
              🛒 Add to Cart
            </button>
          </div>

          {/* Why shop from us */}
          <div className="mt-8 sm:mt-10 border-t pt-4 sm:pt-6">
            <h2 className="text-lg font-semibold mb-4">Why shop from us?</h2>
            <ul className="space-y-4 sm:space-y-5">
              <li className="flex gap-3 sm:gap-4 items-start">
                <span className="text-yellow-500 text-xl sm:text-2xl">⚡</span>
                <div>
                  <p className="font-medium">Superfast Delivery</p>
                  <p className="text-sm text-gray-600">
                    Delivered in minutes from local stores.
                  </p>
                </div>
              </li>
              <li className="flex gap-3 sm:gap-4 items-start">
                <span className="text-yellow-500 text-xl sm:text-2xl">💰</span>
                <div>
                  <p className="font-medium">Best Prices & Offers</p>
                  <p className="text-sm text-gray-600">
                    Deals straight from manufacturers.
                  </p>
                </div>
              </li>
              <li className="flex gap-3 sm:gap-4 items-start">
                <span className="text-yellow-500 text-xl sm:text-2xl">🛍️</span>
                <div>
                  <p className="font-medium">Wide Assortment</p>
                  <p className="text-sm text-gray-600">
                    5,000+ items across essentials and food.
                  </p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProductDetails;
