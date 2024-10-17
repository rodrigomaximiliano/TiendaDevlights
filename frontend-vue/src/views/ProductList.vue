<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <h1 class="text-center">Lista de Productos</h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        v-for="product in products"
        :key="product.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card class="mx-auto" max-width="344">
          <v-img
            :src="product.image"
            alt="Imagen del producto"
            height="200px"
          ></v-img>

          <v-card-title>{{ product.name }}</v-card-title>
          
          <v-card-subtitle class="mb-2">
            ${{ product.price }}
          </v-card-subtitle>

          <v-card-text>
            {{ product.description }}
          </v-card-text>

          <v-card-actions>
            <v-btn color="primary" @click="addToCart(product)">
              Añadir al carrito
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn text color="secondary" @click="viewProductDetails(product.id)">
              Ver detalles
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: []
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/products');
        this.products = response.data;
      } catch (error) {
        console.error("There was an error fetching the products:", error);
      }
    },
    addToCart(product) {
      // Lógica para agregar el producto al carrito
      alert(`Producto "${product.name}" añadido al carrito.`);
    },
    viewProductDetails(productId) {
      // Lógica para redirigir a la página de detalles del producto
      this.$router.push(`/products/${productId}`);
    }
  }
};
</script>

<style scoped>
h1 {
  margin-bottom: 30px;
}
.v-card {
  border-radius: 16px;
}
.v-card-title {
  font-weight: bold;
}
.v-card-subtitle {
  color: #4caf50;
}
</style>
