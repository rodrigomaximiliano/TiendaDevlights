<template>
  <v-app>
    <!-- Barra de navegación -->
    <v-app-bar app color="#f5f5f5" elevated>
      <v-toolbar-title class="d-flex align-center">
        <v-img src="@/assets/logo.png" height="40" contain class="mr-2"></v-img>
        <span class="custom-title align-self-center">Tienda Devlights</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- Texto de envíos -->
      <div class="d-flex align-center light-purple--text ml-4">
        <v-icon color="#6a1b9a">mdi-truck-delivery</v-icon>
        <span class="ml-2 subtitle-text">Envíos a Domicilio</span>
      </div>

      <!-- Botones de navegación -->
      <div class="d-flex align-center">
        <v-btn
          v-for="(item, index) in navItems"
          :key="index"
          text
          @click="item.action"
          class="nav-btn light-purple--text ml-4"
          aria-label="Ir a {{ item.text }}"
        >
          {{ item.text }}
        </v-btn>
      </div>

      <!-- Campo de búsqueda -->
      <v-text-field
        v-model="search"
        placeholder="Buscar productos..."
        append-inner-icon="mdi-magnify"
        clearable
        outlined
        hide-details
        class="mx-4"
        color="#6a1b9a"
        dense
        solo-inverted
        rounded
        :style="{ maxWidth: '250px' }"
        aria-label="Campo de búsqueda"
      ></v-text-field>
    </v-app-bar>

    <!-- Carrusel de imágenes debajo del navbar -->
    <v-carousel hide-delimiters height="400px" cycle>
      <v-carousel-item
        v-for="(image, i) in images"
        :key="i"
        :src="image"
      ></v-carousel-item>
      <v-carousel-control left>
        <v-icon>mdi-chevron-left</v-icon>
      </v-carousel-control>
      <v-carousel-control right>
        <v-icon>mdi-chevron-right</v-icon>
      </v-carousel-control>
    </v-carousel>

    <!-- Sección de Destacados -->
    <v-container class="my-5">
      <h2 class="text-center font-weight-bold light-purple--text">Productos Destacados</h2>
      <v-row class="mt-4">
        <v-col v-for="(product, index) in featuredProducts" :key="index" cols="12" md="4">
          <v-card>
            <v-img :src="product.image" height="200px"></v-img>
            <v-card-title>{{ product.title }}</v-card-title>
            <v-card-subtitle>{{ product.price }}</v-card-subtitle>
            <v-card-actions>
              <v-btn color="primary" @click="addToCart(product)">Añadir al carrito</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <!-- Footer -->
    <v-footer color="purple lighten-5" elevated>
      <v-container>
        <v-row>
          <v-col class="text-center">
            <p class="footer-text">&copy; 2024 Tienda Devlights. Todos los derechos reservados.</p>
            <div>
              <v-icon class="mx-2 light-purple--text">mdi-facebook</v-icon>
              <v-icon class="mx-2 light-purple--text">mdi-twitter</v-icon>
              <v-icon class="mx-2 light-purple--text">mdi-instagram</v-icon>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
  name: 'HomePage',
  setup() {
    const router = useRouter();
    const search = ref('');

    const navItems = [
      { text: 'Inicio', action: () => router.push('/') },
      { text: 'Productos', action: () => router.push('/products') },
      { text: 'Iniciar Sesión', action: () => router.push('/login') },
      { text: 'Registrarse', action: () => router.push('/register') },
    ];

    // Rutas de imágenes
    const images = [
      require('@/assets/img1.webp'),
      require('@/assets/img2.webp'),
      require('@/assets/img3.webp'),
      require('@/assets/img4.webp')
    ];

    // Productos destacados
    const featuredProducts = [
      { title: 'Producto 1', price: '$10', image: require('@/assets/img1.webp') },
      { title: 'Producto 2', price: '$20', image: require('@/assets/img2.webp') },
      { title: 'Producto 3', price: '$30', image: require('@/assets/img5.jpg') }
    ];

    const addToCart = (product) => {
      console.log(`Añadido al carrito: ${product.title}`);
    };

    return { search, navItems, images, featuredProducts, addToCart };
  },
};
</script>

<style scoped>
.v-toolbar-title {
  display: flex;
  align-items: center;
}

.custom-title {
  font-size: 1rem; /* Tamaño del texto del título */
  font-weight: 800; /* Grosor del texto */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); /* Sombreado del texto */
  margin-left: 10px; /* Espacio a la izquierda del texto */
}

.align-self-center {
  align-self: center; /* Centrar verticalmente el texto */
}

.subtitle-text {
  font-size: 0.9rem; /* Tamaño del texto del subtítulo */
}

.footer-text {
  margin: 16px 0;
  font-weight: bold;
}

.light-purple--text {
  color: #9d78dd !important; 
  font-weight: 700;
}

.nav-btn {
  font-size: 0.9rem; /* Tamaño del texto de los botones de navegación */
  transition: color 0.3s, transform 0.3s; /* Transición suave para el color y la transformación */
}

.nav-btn:hover {
  color: #6a1b9a; /* Color al pasar el mouse */
  transform: scale(1.05); /* Efecto de elevar */
}

.v-btn {
  border: 1px solid transparent;
  font-size: 0.9rem; /* Tamaño de texto más pequeño */
  font-weight: 500;
}

.v-btn:hover {
  background-color: rgba(209, 196, 233, 0.3); /* Efecto hover con morado claro */
  border-color: rgba(209, 196, 233, 0.5);
}

.v-carousel {
  height: 200px;
  margin-top: 40px;
}

@media (max-width: 600px) {
  .v-toolbar-title {
    justify-content: center;
  }
  .v-carousel {
    margin-top: 10px;
  }
}
</style>
