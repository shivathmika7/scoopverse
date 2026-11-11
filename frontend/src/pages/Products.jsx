
import { useEffect, useState } from "react";
import { getProducts } from "../services/api";

function Products() {

    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        getProducts()
            .then(data => setProducts(data))
            .catch(err => {
                console.error(err);
                setError("Unable to load ice creams");
            })
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <h2>Loading ice creams...</h2>;

    if (error) return <h2>{error}</h2>;

    return (
        <div>
            <h1>🍦 Welcome to ScoopVerse</h1>
            <h2>Explore Our Ice Creams</h2>

            <div>
                {products.map(product => (
                    <div key={product._id}>
                        <img
                            src={product.image}
                            alt={product.name}
                            width="200"
                        />

                        <h2>{product.name}</h2>
                        <p>{product.description}</p>
                        <h3>₹{product.price}</h3>
                        <p>Stock: {product.stock}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Products;
