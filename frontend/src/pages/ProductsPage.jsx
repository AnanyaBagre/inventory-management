import { useEffect, useState } from "react";
import API from "../api";

function ProductsPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    API.get("/products")
      .then((res) => setProducts(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>Products</h1>

      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>SKU: {product.sku}</p>
          <p>Price: ₹{product.price}</p>
          <p>Quantity: {product.quantity}</p>
        </div>
      ))}
    </div>
  );
}

export default ProductsPage;
