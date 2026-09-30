from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty


class LoginScreen(Screen):

    def hapus_username(self):
        self.ids.username.text = ""

    def hapus_password(self):
        self.ids.password.text = ""

    def toggle_password(self):
        self.ids.password.password = not self.ids.password.password

    def login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if username and password:
            self.manager.current = "welcome"


class WelcomeScreen(Screen):
    pass


class ProductScreen(Screen):

    def pilih_produk(self, nama_produk):
        detail_screen = self.manager.get_screen("detail")
        detail_screen.nama_produk = nama_produk
        detail_screen.merek_dipilih = ""
        self.manager.current = "detail"


class DetailScreen(Screen):

    nama_produk = StringProperty("Belum ada produk yang dipilih")
    merek_dipilih = StringProperty("")

    def pilih_merek(self, nama_merek):
        self.merek_dipilih = nama_merek

    def tambah_keranjang(self):
        if self.merek_dipilih:
            cart_screen = self.manager.get_screen("cart")
            cart_screen.nama_produk = self.nama_produk
            cart_screen.merek_produk = self.merek_dipilih
            self.manager.current = "cart"


class CartScreen(Screen):

    nama_produk = StringProperty("")
    merek_produk = StringProperty("")


class MusicShopApp(App):

    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(ProductScreen(name="product"))
        sm.add_widget(DetailScreen(name="detail"))
        sm.add_widget(CartScreen(name="cart"))

        return sm


MusicShopApp().run()
