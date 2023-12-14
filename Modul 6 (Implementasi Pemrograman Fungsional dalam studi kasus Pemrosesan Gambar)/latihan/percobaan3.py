from PIL import Image, ImageEnhance

# TODO 1: Buka gambar menggunakan Pillow
image_path = "assets/cek.png"
original_image = Image.open(image_path)

# TODO 2: Buat nilai contrast dan brightness baru yang berbeda
enhancer = ImageEnhance.Brightness(original_image)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
result_image_path = "assets/percobaan3.png"
final_image.save(result_image_path)

# TODO 4: Tampilkan hasilnya
final_image.show()
