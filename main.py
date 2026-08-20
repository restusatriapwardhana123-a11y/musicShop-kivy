from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ProductScreen(Screen):

    def pilih_produk(self, nama_produk):
        detail_screen = self.manager.get_screen("detail")
        detail_screen.nama_produk = nama_produk
        self.manager.current = "detail"


class DetailScreen(Screen):
    nama_produk = StringProperty("Belum ada produk yang dipilih")

    def tambah_keranjang(self):
        cart_screen = self.manager.get_screen("cart")
        cart_screen.nama_produk = self.nama_produk
        self.manager.current = "cart"


class CartScreen(Screen):
    nama_produk = StringProperty("Keranjang masih kosong")


class MusicShopApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProductScreen(name="product"))
        sm.add_widget(DetailScreen(name="detail"))
        sm.add_widget(CartScreen(name="cart"))

        return sm


MusicShopApp().run()