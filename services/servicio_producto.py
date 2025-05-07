from fastapi import FastAPI
from models.modelo_producto import Producto
from bs4 import BeautifulSoup
import requests

# Esta funcion hace el scrapping de la pagina web de Esika
def obtener_productos():
    url = "https://esika.tiendabelcorp.com.co/maquillaje/c"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    productos = []

    # Encuentra todos los contenedores principales de productos
    productos_html = soup.find_all("div", class_="vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4")

    for producto_html in productos_html:
        # Título
        titulo_tag = producto_html.find("div", class_="vtex-product-summary-2-x-nameContainer vtex-product-summary-2-x-nameContainer--product-search-name flex items-start justify-center pv6")
        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"
        print(f"Título: {titulo}")

        # Foto
        foto_tag = producto_html.find("div", class_="vtex-product-summary-2-x-imageContainer vtex-product-summary-2-x-imageWrapper vtex-product-summary-2-x-imageWrapper--product-search-image db w-100 center")
        img_tag = foto_tag.find("img") if foto_tag else None
        foto_url = img_tag['src'] if img_tag else "Sin imagen"
        print(f"Foto: {foto_url}")

        # Precio
        precio_tag = producto_html.find("div", class_="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--product-search-price-wrapper")
        precio = precio_tag.text.strip() if precio_tag else "Precio no disponible"
        print(f"Precio: {precio}")

        # Color (opcional, puede no estar)
        color_tag = producto_html.find("div", class_="vtex-store-components-3-x-skuSelectorTextContainer db mb3")
        color = color_tag.text.strip() if color_tag else None
        print(f"Color: {color if color else 'No disponible'}")

        # Crea el objeto Producto
        producto = Producto(
            titulo=titulo,
            foto=foto_url,
            precio=precio,
            color=color
        )

        productos.append(producto)

    return productos

