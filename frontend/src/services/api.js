
import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

// Get all ice creams
export const getProducts = async () => {
    const response = await API.get("/products");
    return response.data;
};

// Add ice cream
export const addProduct = async (product) => {
    const response = await API.post("/products", product);
    return response.data;
};

export default API;
